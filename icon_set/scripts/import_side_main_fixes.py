"""Import completed Ray redraws for the Needs fix main icons in a gallery snapshot.

Defaults to a checked plan. --apply installs only passing or explicitly approved
drawings; --build rebuilds those exact originals. Review state is never changed.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from icon_set.scripts.workspace import REPO_ROOT, primitive_results_dir
from icon_set.validation.library_qa import inspect_icon


def sha(data):
    return hashlib.sha256(data).hexdigest()


def absolute(text):
    return text.replace('from ...keyshapes import Keyshape',
                        'from icon_set.model.keyshapes import Keyshape').replace(
        'from ._base import Solo48', 'from icon_set.model.icons.solo._base import Solo48')


def load(text, filename):
    module = types.ModuleType('_side_fix_' + sha(text.encode())[:16])
    module.__file__ = str(filename)
    module.__package__ = 'icon_set.model.icons.solo'
    exec(compile(absolute(text), str(filename), 'exec'), module.__dict__)
    classes = [c for c in vars(module).values() if isinstance(c, type)
               and c.__module__ == module.__name__ and getattr(c, 'icon_id', None)]
    if len(classes) != 1:
        raise ValueError('Expected exactly one authored icon class')
    return classes[0]


def module_in(run):
    result = run / 'result.json'
    data = json.loads(result.read_text()) if result.exists() else {}
    artifacts = data.get('artifacts', {})
    named = data.get('module') or (artifacts.get('python') if isinstance(artifacts, dict) else None)
    if named and (run / Path(named).name).is_file():
        return run / Path(named).name
    candidates = [p for p in run.glob('*.py') if run.parent.name.replace('-', '_') in p.name]
    if len(candidates) == 1:
        return candidates[0]
    raise ValueError('No unambiguous drawing module')


def newest_run(item):
    candidates = []
    for uid in set([item['id']] + item.get('source_ids', [])):
        for run in (primitive_results_dir() / uid).glob('*'):
            if not run.is_dir():
                continue
            try:
                module = module_in(run)
            except ValueError:
                continue
            # Approval edits to result.json must not make an older drawing win.
            candidates.append((module.stat().st_mtime_ns, str(run), run, module))
    if not candidates:
        raise ValueError('No saved drawing found')
    _, _, run, module = max(candidates)
    if not (run / 'result.json').exists():
        raise ValueError(f'Latest drawing has no completed result: {run}')
    return run, module


def approval_for(run, data, cls):
    approval = getattr(cls, 'exception', None) or data.get('exception') or data.get('approved_exception')
    if isinstance(approval, dict):
        return approval
    p = run / 'gate-exception.json'
    if p.exists():
        approval = json.loads(p.read_text())
        if approval.get('approval_source') == 'user' and approval.get('effective_status') == 'accepted-with-exception':
            return {'approved_by': 'user', 'svg_sha256': approval['svg_sha256'],
                    'reason': approval['user_instruction'] + ' — ' + approval['scope']}
    return None


def override(text, attrs):
    tree = ast.parse(text)
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef))
    lines = text.splitlines(keepends=True)
    # Last assignments override earlier declarations without altering geometry.
    lines.insert(cls.end_lineno, '\n' + ''.join(f'    {k} = {v!r}\n' for k, v in attrs.items()))
    return ''.join(lines)


def prepare(item, output):
    run, module = newest_run(item)
    data = json.loads((run / 'result.json').read_text())
    original = module.read_text()
    cls = load(original, module)
    candidates = [d for d in item['drawings'] if d['family'] == 'solo']
    exact = [d for d in candidates if d['icon_id'] == cls.icon_id]
    named = [d for d in candidates if Path(d['python_source']).name == module.name]
    source_named = [d for d in candidates if run.parent.name.replace('-', '_') in Path(d['python_source']).stem]
    if len(exact) == 1:
        drawing = exact[0]
    elif len(named) == 1:
        drawing = named[0]
    elif len(source_named) == 1:
        drawing = source_named[0]
    elif len(candidates) == 1:
        drawing = candidates[0]
    else:
        raise ValueError('Ambiguous registered target; manual selection needed')
    target = (REPO_ROOT / drawing['python_source']).resolve()
    if not target.is_relative_to(REPO_ROOT / 'icon_set/model/icons/solo'):
        raise ValueError('Target is outside the solo model directory')
    old_text = target.read_text()
    old_cls = load(old_text, target)
    old_qa = inspect_icon(old_cls())
    new_qa = inspect_icon(cls())
    same_identity_svg = load(override(original, {'icon_id': old_cls.icon_id}), module)().to_svg()
    # Refuse to overwrite another task's newer drawing. Metadata-only changes
    # are retained below, and an already imported redraw may gain its exception.
    if old_qa.get('svg_sha256') not in (drawing.get('svg_sha256'), sha(same_identity_svg.encode())):
        raise ValueError('Registered drawing differs from both reviewed revision and saved redraw')
    attrs = {k: getattr(old_cls, k) for k in ('icon_id', 'category', 'aliases', 'keywords',
             'semantic_role', 'semantic_kind') if hasattr(old_cls, k)}
    approval = approval_for(run, data, cls)
    saved_svg = run / (cls.icon_id + '.svg')
    if not saved_svg.is_file() or sha(saved_svg.read_bytes()) != new_qa.get('svg_sha256'):
        raise ValueError('Saved module does not reproduce its completed SVG')
    text = override(original, attrs)
    prepared_svg = load(text, module)().to_svg()
    # Keeping a registered identity changes only SVG <title>, not any artwork.
    strip_title = lambda svg: re.sub(r'<title>[^<]*</title>', '', svg)
    if strip_title(prepared_svg) != strip_title(saved_svg.read_text()):
        raise ValueError('Identity preservation changed artwork beyond the SVG title')
    if approval:
        if approval.get('svg_sha256') != new_qa['svg_sha256']:
            raise ValueError('Approval does not match the completed drawing')
        attrs['exception'] = {**approval, 'svg_sha256': sha(prepared_svg.encode()),
                              'source_svg_sha256': approval['svg_sha256']}
        text = override(original, attrs)
    qa = inspect_icon(load(text, module)())
    if qa['status'] != 'pass':
        raise ValueError('Full build gate ' + qa['status'] + ': ' + '; '.join(qa['errors'] + qa['warnings']))
    if qa['svg_sha256'] != sha(prepared_svg.encode()):
        raise ValueError('Prepared drawing changed during validation')
    stage = output / 'prepared' / target.name
    stage.parent.mkdir(parents=True, exist_ok=True)
    stage.write_text(text)
    return {'source_uuid': item['id'], 'concept': item['concept'], 'run': str(run),
            'target': str(target.relative_to(REPO_ROOT)), 'prepared': str(stage),
            'before_source_sha256': sha(old_text.encode()), 'prepared_sha256': sha(text.encode()),
            'svg_sha256': qa['svg_sha256'], 'icon_id': attrs['icon_id'],
            'exception': qa.get('exception'), 'automatic_status': qa.get('automatic_status', qa['status']),
            'status': qa['status']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--components', type=Path, required=True)
    parser.add_argument('--reviews', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    if args.build and not args.apply:
        parser.error('--build requires --apply')
    data = json.loads(args.components.read_text())
    reviews = json.loads(args.reviews.read_text())
    items = [i for i in data['mains'] if i['drawings'] and not any(
        d['status'] == 'pass' and reviews.get(d['key']) not in ('pending', 'rejected') for d in i['drawings'])]
    args.output.mkdir(parents=True, exist_ok=True)
    report = {'total': len(items), 'ready': [], 'held': [], 'applied': []}
    for item in items:
        try:
            result = prepare(item, args.output)
            report['ready'].append(result)
            print('READY', item['concept'], flush=True)
        except Exception as error:
            report['held'].append({'source_uuid': item['id'], 'concept': item['concept'], 'reason': str(error)})
            print('HELD', item['concept'], str(error)[:150], flush=True)
    if args.apply:
        # Check every target before changing any target.
        for row in report['ready']:
            if sha((REPO_ROOT / row['target']).read_bytes()) != row['before_source_sha256']:
                raise ValueError('Target changed during preparation: ' + row['target'])
            if (args.output / 'before' / Path(row['target']).name).exists():
                raise ValueError('Use a fresh output directory; backup already exists')
        for row in report['ready']:
            target = REPO_ROOT / row['target']
            backup = args.output / 'before' / target.name
            backup.parent.mkdir(parents=True, exist_ok=True)
            if backup.exists():
                raise ValueError('Use a fresh output directory; backup already exists')
            backup.write_bytes(target.read_bytes())
            target.write_bytes(Path(row['prepared']).read_bytes())
            report['applied'].append(row['target'])
    (args.output / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(f"{len(report['ready'])} ready; {len(report['held'])} held; {len(report['applied'])} applied")
    if args.build and report['applied']:
        command = [sys.executable, '-m', 'icon_set', 'build', '--no-report']
        for path in report['applied']:
            command += ['--icon', path]
        return subprocess.call(command, cwd=REPO_ROOT)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
