#!/usr/bin/env python3
"""Ask a read-only AI agent for icon feedback; never publish or submit it.

CLI: python3 icon_set/scripts/review_icon.py --icon acoustic-guitar --out /tmp/guitar-review
The gallery uses FeedbackReviewManager to run this work in the background.
"""
from datetime import datetime, timezone
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import sys
import threading
import uuid
import xml.etree.ElementTree as ET

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from icon_set.scripts.generation import GenerationManager, digest

RESULT_SCHEMA = {
    'type': 'object', 'additionalProperties': False,
    'properties': {
        'verdict': {'type': 'string', 'enum': ['keep', 'repair', 'uncertain']},
        'feedback': {'type': 'string'},
    },
    'required': ['verdict', 'feedback'],
}


def validate_result(result):
    if (not isinstance(result, dict) or result.get('verdict') not in ('keep', 'repair', 'uncertain')
            or not isinstance(result.get('feedback'), str) or not 1 <= len(result['feedback'].strip()) <= 6000):
        raise ValueError('The agent did not return usable feedback. Please try again.')
    return dict(verdict=result['verdict'], feedback=result['feedback'].strip())


def review_sheet(document, record, output):
    import cairosvg
    from PIL import Image, ImageDraw
    size = record['canvas_size']
    if size not in (32, 48, 64):
        raise ValueError('Unknown icon profile size.')
    sheet = Image.new('RGB', (800, 510), '#edf0f4')
    pen = ImageDraw.Draw(sheet)
    pen.text((16, 10), f"{record['icon_id']} | {record['profile']} | {record['keyshape']}", fill='black')
    for index, (bg, fg, theme) in enumerate([('#ffffff', '#172033', 'Light'), ('#172033', '#ffffff', 'Dark')]):
        root = ET.fromstring(document)
        root.set('color', fg)
        x = 16+400*index
        for pixels, y in [(size, 58), (360, 150)]:
            png = cairosvg.svg2png(bytestring=ET.tostring(root), output_width=pixels,
                                  output_height=pixels, background_color=bg)
            sheet.paste(Image.open(io.BytesIO(png)).convert('RGB'), (x, y))
        pen.text((x, 38), f'{theme}: native {size}px', fill='black')
        pen.text((x, 130), 'Enlarged', fill='black')
    sheet.save(output)


def run_review(runner, record, document, output):
    """Freeze inputs, prepare visual evidence, then run Codex against that copy."""
    if hashlib.sha256(document.encode()).hexdigest() != record['svg_sha256']:
        raise ValueError('The artwork changed. Refresh the icon before asking for feedback.')
    output = Path(output).resolve()
    workspace = output/'workspace'
    baseline = runner.snapshot(workspace)
    # Only copy this icon's source references; the complete reference corpus is large.
    for reference in record.get('original_sources', []):
        relative = reference.get('source_path', '')
        source = (runner.root/relative).resolve()
        if relative and source.is_relative_to(runner.root.resolve()) and source.is_file():
            target = workspace/source.relative_to(runner.root.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    evidence = workspace/'review-input'
    evidence.mkdir()
    (evidence/'selected.svg').write_text(document)
    (evidence/'selected.json').write_text(json.dumps(record, indent=2))
    review_sheet(document, record, evidence/'selected.png')
    log = output/'run.log'
    # Model QA is separate evidence: selected uploads need not match Python.
    try:
        runner.command([sys.executable, str(workspace/'icon_set/scripts/prepare_icon_review.py'),
                        '--icon', record['icon_id'], '--out', str(evidence/'python')], workspace, log, timeout=180)
    except Exception as error:
        (evidence/'python-qa-unavailable.txt').write_text(str(error))
    schema = output/'result-schema.json'
    schema.write_text(json.dumps(RESULT_SCHEMA))
    result_path = output/'result.json'
    template = runner.root/'icon_set/scripts/templates/review_icon_prompt.md'
    prompt = template.read_text().replace('{{ICON_JSON}}', json.dumps({k: record.get(k) for k in
        ('key', 'icon_id', 'name', 'description', 'aliases', 'keywords', 'category',
         'semantic_kind', 'profile', 'keyshape', 'artwork_source', 'svg_sha256', 'python_source')}, indent=2))
    (output/'prompt.txt').write_text(prompt)
    args = [os.environ.get('CODEX_BIN', 'codex'), '-a', 'never', 'exec', '--sandbox', 'read-only',
            '--skip-git-repo-check', '-C', str(workspace), '--output-schema', str(schema),
            '--output-last-message', str(result_path), prompt, '--image='+str(evidence/'selected.png')]
    reference_png = evidence/'python/reference.png'
    if reference_png.is_file():
        args.append('--image='+str(reference_png))
    runner.command(args, workspace, log, timeout=900)
    for relative, expected in baseline.items():
        path = workspace/relative
        if not path.is_file() or path.is_symlink() or digest(path) != expected:
            raise ValueError('Review unexpectedly changed source files. Feedback was not accepted.')
    result = validate_result(json.loads(result_path.read_text()))
    (output/'feedback.txt').write_text(result['feedback']+'\n')
    return result


class FeedbackReviewManager:
    def __init__(self, runner, storage):
        self.runner, self.storage = runner, Path(storage)
        self.storage.mkdir(parents=True, exist_ok=True)
        for path in self.storage.glob('*/job.json'):
            row = json.loads(path.read_text())
            if row['status'] == 'running':
                row.update(status='failed', error='Server restarted during this review. Please try again.')
                self.write(row)

    def folder(self, job_id):
        if not isinstance(job_id, str) or not re.fullmatch('[a-f0-9]{32}', job_id):
            raise ValueError('Invalid AI review job.')
        return self.storage/job_id

    def write(self, row):
        folder = self.folder(row['id'])
        folder.mkdir(parents=True, exist_ok=True)
        temp = folder/'job.tmp'
        temp.write_text(json.dumps(row, indent=2))
        temp.replace(folder/'job.json')

    def read(self, job_id):
        try:
            return json.loads((self.folder(job_id)/'job.json').read_text())
        except FileNotFoundError:
            raise ValueError('AI review not found.')

    def start(self, data, record, document, user):
        if not record or record.get('svg_sha256') != data.get('svg_sha256'):
            raise ValueError('The icon changed. Refresh before asking for feedback.')
        if hashlib.sha256(document.encode()).hexdigest() != record['svg_sha256']:
            raise ValueError('The displayed artwork is out of date. Rebuild or refresh it first.')
        with self.runner.lock:
            # Repeated clicks/retries reconnect to the same in-flight review.
            for path in self.storage.glob('*/job.json'):
                job = json.loads(path.read_text())
                if (job['status'] == 'running' and job['icon'] == record['key']
                        and job['svg_sha256'] == record['svg_sha256'] and job['created_by'] == user):
                    return job
            if self.runner.busy:
                raise ValueError('An agent or build is already running. Wait for it to finish.')
            if not shutil.which(os.environ.get('CODEX_BIN', 'codex')):
                raise ValueError('Install Codex CLI on this server and sign in to ask for AI feedback.')
            row = dict(id=uuid.uuid4().hex, status='running', icon=record['key'],
                       svg_sha256=record['svg_sha256'], created_by=user,
                       created_at=datetime.now(timezone.utc).isoformat())
            self.write(row)
            self.runner.busy = True
            try:
                threading.Thread(target=self.run, args=(row, record, document), daemon=True).start()
            except Exception:
                self.runner.busy = False
                row.update(status='failed', error='Could not start AI review. Please try again.')
                self.write(row)
                raise
            return dict(row)

    def run(self, row, record, document):
        try:
            result = run_review(self.runner, record, document, self.folder(row['id']))
            row.update(status='completed', **result)
        except Exception as error:
            row.update(status='failed', error=str(error))
        finally:
            row['completed_at'] = datetime.now(timezone.utc).isoformat()
            with self.runner.lock:
                self.write(row)
                self.runner.busy = False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--icon', required=True)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args(argv)
    from icon_set.model.icons.registry import create
    from icon_set.scripts.icon_artwork import sha
    icon = create(args.icon)
    record = dict(icon_id=icon.icon_id, name=icon.icon_id, aliases=list(icon.aliases),
                  keywords=list(icon.keywords), category=icon.category, semantic_kind=icon.semantic_kind,
                  key=icon.family+'/'+icon.icon_id, family=icon.family,
                  canvas_size=icon.profile.spec.canvas_size, profile=icon.profile.name,
                  keyshape=icon.keyshape.name, svg_sha256=sha(icon.to_svg()), artwork_source='use_org')
    runner = GenerationManager(ROOT, build_dist(ROOT), args.out/'runner')
    print(json.dumps(run_review(runner, record, icon.to_svg(), args.out), indent=2))


if __name__ == '__main__':
    main()
