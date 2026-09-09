"""Isolated Codex candidates; explicit acceptance is the only library write."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import uuid

FAMILIES = ('sub', 'solo', 'container')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class GenerationManager:
    def __init__(self, root, dist, storage):
        self.root, self.dist, self.storage = Path(root), Path(dist), Path(storage)
        self.storage.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()
        self.busy = False
        for path in self.storage.glob('*/job.json'):
            row = json.loads(path.read_text())
            if row['status'] in ('running', 'accepting'):
                row.update(status='failed', error='Server restarted during this job. Start a new request; inspect the library if acceptance was interrupted.')
                self.write(row)

    def folder(self, job_id):
        if not isinstance(job_id, str) or not re.fullmatch('[a-f0-9]{32}', job_id):
            raise ValueError('Invalid generation job.')
        return self.storage / job_id

    def write(self, row):
        folder = self.folder(row['id'])
        folder.mkdir(parents=True, exist_ok=True)
        temporary = folder / 'job.tmp'
        temporary.write_text(json.dumps(row, ensure_ascii=False, indent=2))
        temporary.replace(folder / 'job.json')

    def read(self, job_id):
        try:
            return json.loads((self.folder(job_id) / 'job.json').read_text())
        except FileNotFoundError:
            raise ValueError('Generation job not found.')

    def listing(self):
        with self.lock:
            return [json.loads(p.read_text()) for p in sorted(self.storage.glob('*/job.json'), key=lambda p:p.stat().st_mtime, reverse=True)]

    def start(self, data, catalog):
        mode, name, prompt, family = (data.get(k, '') for k in ('mode', 'name', 'prompt', 'family'))
        model = data.get('model', '')
        if mode not in ('generate', 'fix') or family not in ('auto', *FAMILIES):
            raise ValueError('Choose generate/fix and Auto, sub, solo or container.')
        if not isinstance(name,str) or not 1 <= len(name.strip()) <= 160 or not isinstance(prompt,str) or not 1 <= len(prompt.strip()) <= 10000:
            raise ValueError('Enter an icon name and a prompt (up to 10,000 characters).')
        if not isinstance(model,str) or len(model)>100 or (model and not re.fullmatch(r'[a-zA-Z0-9_.:/-]+',model)):
            raise ValueError('Invalid model name.')
        source = None
        if mode == 'fix':
            source = catalog.get(data.get('icon'))
            if not source or source.get('svg_sha256') != data.get('svg_sha256'):
                raise ValueError('The icon changed. Refresh before fixing it.')
            relative = source.get('python_source',{}).get('path','')
            path = (self.root / relative).resolve()
            if not relative or not path.is_relative_to((self.root/'icon_set/model/icons').resolve()) or not path.is_file():
                raise ValueError('This icon has no available Python source.')
            family = source['family']
        with self.lock:
            if self.busy:
                raise ValueError('An agent or build is already running. Wait for it to finish.')
            if not shutil.which(os.environ.get('CODEX_BIN','codex')):
                raise ValueError('Install Codex CLI on this server and sign in before generating.')
            row = dict(id=uuid.uuid4().hex, mode=mode, name=name.strip(), prompt=prompt.strip(), family=family, model=model, source=source, status='running')
            self.write(row)
            self.busy=True
            threading.Thread(target=self.run, args=(row,), daemon=True).start()
            return row

    def snapshot(self, destination):
        for relative in ('icon_set/model','icon_set/renderers','icon_set/validation','icon_set/schemas','icon_set/skills','icon_set/scripts','icon_set/references','.agents/skills','.claude/skills'):
            source=self.root/relative
            if source.exists():
                shutil.copytree(source,destination/relative,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        shutil.copy2(self.root/'icon_set/__init__.py',destination/'icon_set/__init__.py')
        return {str(p.relative_to(destination)):digest(p) for p in destination.rglob('*') if p.is_file()}

    def command(self, args, cwd, log, timeout=1800):
        with log.open('ab') as stream:
            process = subprocess.Popen(args,cwd=cwd,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
            try:
                code=process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                import signal
                os.killpg(process.pid,signal.SIGKILL)
                process.wait()
                raise ValueError('The agent/build timed out. Try a smaller request.')
            if code:
                raise ValueError(f'Agent/build exited with code {code}. See the job log.')

    def build(self, workspace, family, log, dist=None):
        self.command([sys.executable,str(workspace/'icon_set/scripts/build.py'),'--family',family,'--no-png','--no-report','--dist',str(dist or workspace/'icon_set/dist')],workspace,log)

    def run(self, row):
        folder=self.folder(row['id']); workspace=folder/'workspace'; log=folder/'run.log'
        try:
            baseline=self.snapshot(workspace)
            source=row['source']
            context = '' if not source else '\nFix this icon by creating a NEW variant, never changing its old file:\n'+json.dumps({k:source.get(k) for k in ('key','icon_id','family','python_source')})
            prompt = ('Read .agents/skills/icon-making/SKILL.md and route to the matching icon-sub, icon-solo or icon-container skill. '
                'Create exactly ONE candidate in ONE NEW public Python module under icon_set/model/icons/<family>/. '
                'Do not modify any existing files, contracts, skills, or registry. Choose a unique Python filename and icon_id. '
                'For fixes, preserve the original and set variant_of to its icon_id with a descriptive variant_label. '
                'Use existing dependencies only. Do not publish to any other directory. '
                'Validate the candidate. If the request cannot produce one standalone icon, explain and stop. '
                'Write candidate.json at the workspace root with {"path":"icon_set/model/icons/<family>/<filename>.py","family":"sub|solo|container","icon_id":"..."}.\n'
                +context+'\nUser request:\n'+json.dumps({k:row[k] for k in ('mode','name','prompt','family')},ensure_ascii=False))
            prompt_path=folder/'prompt.txt'; prompt_path.write_text(prompt)
            self.command(['bash',str(self.root/'icon_set/scripts/run_icon_agent.sh'),str(workspace),str(prompt_path),row['model']],workspace,log)
            candidate=json.loads((workspace/'candidate.json').read_text())
            relative=candidate['path']; family=candidate['family']
            if family not in FAMILIES or not re.fullmatch(r'icon_set/model/icons/'+family+r'/[a-z][a-z0-9_]*\.py',relative):
                raise ValueError('Candidate must be one new icon Python file.')
            if row['family']!='auto' and family!=row['family']:
                raise ValueError('Candidate did not honor the requested icon type.')
            path=workspace/relative
            if path.is_symlink() or not path.is_file() or relative in baseline:
                raise ValueError('Candidate must preserve existing Python files.')
            for name,sha in baseline.items():
                existing=workspace/name
                if not existing.is_file() or existing.is_symlink() or digest(existing)!=sha:
                    raise ValueError('Agent changed an existing file; candidate was not published: '+name)
            new_python=[str(p.relative_to(workspace)) for p in workspace.rglob('*.py') if str(p.relative_to(workspace)) not in baseline]
            if sorted(new_python) != [relative]:
                raise ValueError('Expected exactly one new Python module.')
            self.build(workspace,family,log)
            icons=json.loads((workspace/'icon_set/dist/gallery/icons.json').read_text())['icons']
            matches=[icon for icon in icons if icon.get('python_source',{}).get('path')==relative]
            if len(matches)!=1 or matches[0]['icon_id']!=candidate['icon_id']:
                raise ValueError('Candidate metadata does not match its built Python icon.')
            icon=matches[0]
            if source and icon.get('variant_of')!=source['icon_id']:
                raise ValueError('Fix must be a variant of the selected icon.')
            svg=(workspace/'icon_set/dist/gallery'/icon['preview_url']).resolve()
            shutil.copy2(svg,folder/'preview.svg')
            row.update(status='candidate',candidate=icon,path=relative,sha256=digest(path))
        except Exception as error:
            row.update(status='failed',error=str(error))
        finally:
            with self.lock:
                self.write(row); self.busy=False

    def decide(self, job_id, accept):
        with self.lock:
            row=self.read(job_id)
            if row['status'] not in ('candidate','failed') or (accept and row['status']!='candidate'):
                raise ValueError('This job is not awaiting a decision.')
            if not accept:
                shutil.rmtree(self.folder(job_id)/'workspace',ignore_errors=True)
                (self.folder(job_id)/'preview.svg').unlink(missing_ok=True)
                row.update(status='discarded'); self.write(row); return row
            if self.busy:
                raise ValueError('Wait for the current agent/build to finish.')
            self.busy=True;row.update(status='accepting');self.write(row)
            threading.Thread(target=self.accept,args=(row,),daemon=True).start()
            return row

    def accept(self,row):
        folder=self.folder(row['id']); target=self.root/row['path'];created=False
        try:
            candidate=folder/'workspace'/row['path']
            if digest(candidate)!=row['sha256']:
                raise ValueError('Candidate changed after review. Generate again.')
            # Exclusive creation prevents overwriting another accepted candidate.
            with target.open('xb') as output:
                created=True; output.write(candidate.read_bytes())
            self.build(self.root,row['candidate']['family'],folder/'run.log',self.dist)
            row.update(status='accepted')
            shutil.rmtree(folder/'workspace',ignore_errors=True)
        except Exception as error:
            if created and target.exists() and digest(target)==row['sha256']:
                target.unlink()
            row.update(status='candidate',error='Could not add candidate: '+str(error))
        finally:
            with self.lock:
                self.write(row);self.busy=False

    def artifact(self, job_id, kind):
        row=self.read(job_id); folder=self.folder(job_id)
        if kind=='preview' and row['status'] in ('candidate','accepting','accepted'):
            return (folder/'preview.svg').read_bytes(),'image/svg+xml'
        if kind=='log':
            path=folder/'run.log'
            return (path.read_bytes()[-30000:] if path.exists() else b'Preparing workspace...'),'text/plain; charset=utf-8'
        raise ValueError('Artifact unavailable.')
