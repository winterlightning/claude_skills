"""Prepare immutable code/assets together, then health-check before promotion."""
from __future__ import annotations

import filecmp
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tarfile
import tempfile
import time
from urllib.request import urlopen

from .workspace import output_lock


def validate_paths(repo, releases, database):
    repo, releases, database = map(lambda p: Path(p).resolve(), (repo, releases, database))
    if releases == repo or releases.is_relative_to(repo) or repo.is_relative_to(releases):
        raise ValueError('Release storage and the repository must be separate directories.')
    state = database.parent
    if (state == repo or state.is_relative_to(repo) or repo.is_relative_to(state)
            or state == releases or state.is_relative_to(releases) or releases.is_relative_to(state)):
        raise ValueError('Production state must be separate from source and release storage.')
    return releases, database


def read_active(releases):
    path = Path(releases) / 'active.json'
    return json.loads(path.read_text()) if path.exists() else None


def bundle_path(releases, name):
    if not isinstance(name, str) or not name or Path(name).name != name or name in ('.', '..'):
        raise ValueError('Invalid release name.')
    path = Path(releases) / name
    if path.is_symlink():
        raise ValueError('Release bundles must not be symlinks.')
    return path


def snapshot(repo, revision, target, previous=None):
    """Extract only committed files; preserve timestamps for identical build inputs."""
    target.mkdir()
    started = time.time()
    with tempfile.TemporaryFile() as errors:
        proc = subprocess.Popen(['git', 'archive', '--format=tar', revision], cwd=repo,
                                stdout=subprocess.PIPE, stderr=errors)
        try:
            with tarfile.open(fileobj=proc.stdout, mode='r|') as archive:
                for member in archive:
                    relative = PurePosixPath(member.name)
                    if relative.is_absolute() or '..' in relative.parts:
                        raise ValueError('Unsafe path in committed archive.')
                    path = target / member.name
                    if member.isdir():
                        path.mkdir(parents=True, exist_ok=True)
                    elif member.isfile():
                        path.parent.mkdir(parents=True, exist_ok=True)
                        with archive.extractfile(member) as source, path.open('wb') as dest:
                            shutil.copyfileobj(source, dest)
                        path.chmod(member.mode & 0o777)
                        old = previous / member.name if previous else None
                        stamp = old.stat().st_mtime if old and old.is_file() and filecmp.cmp(old, path, shallow=False) else started
                        os.utime(path, (stamp, stamp))
                    else:
                        raise ValueError(f'Unsupported link or special file in release: {member.name}')
            if proc.wait() != 0:
                errors.seek(0)
                raise RuntimeError(errors.read().decode(errors='replace'))
        finally:
            proc.stdout.close()
            if proc.poll() is None:
                proc.kill()
                proc.wait()


def pipeline_changed(source, previous):
    """Conservatively invalidate validation cache when build/schema/dependencies change."""
    def inputs(root):
        paths = set()
        for directory in ('icon_set/scripts', 'icon_set/schemas', 'icon_set/validation',
                          'icon_set/renderers', 'icon_set/model/contracts'):
            paths.update(p.relative_to(root) for p in (root / directory).rglob('*')
                         if p.is_file() and p.suffix in ('.py', '.json', '.cjs'))
        paths.update(p.relative_to(root) for p in (root / 'icon_set/model').glob('*.py'))
        paths.update(p.relative_to(root) for p in (root / 'icon_set/model/icons').rglob('_*.py'))
        paths.update(p.relative_to(root) for pattern in ('*requirements*.txt', '*lock*', 'pyproject.toml', 'package.json')
                     for p in root.glob(pattern) if p.is_file())
        return paths
    before, after = inputs(previous), inputs(source)
    return before != after or any(not filecmp.cmp(previous / p, source / p, shallow=False) for p in after)


def prepare(repo, releases, revision, python, previous=None, runner=subprocess.run):
    """A failed build leaves active code/assets untouched; no state is copied."""
    releases = Path(releases)
    releases.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.preparing-', dir=releases) as temporary:
        bundle = Path(temporary)
        source = bundle / 'source'
        snapshot(repo, revision, source, previous / 'source' if previous else None)
        build = source / 'icon_set/.local/dist'
        if previous:
            shutil.copytree(previous / 'assets', build, ignore=shutil.ignore_patterns('release.json'))
        environment = dict(os.environ, PYTHONNOUSERSITE='1')
        # Never inherit Python import paths from the author's workspace.
        environment.pop('PYTHONPATH', None)
        command = [python, '-m', 'icon_set', 'build', '--no-png', '--allow-validation-failures']
        if previous and pipeline_changed(source, previous / 'source'):
            command.append('--all')
        with (bundle / 'build.log').open('w') as log:
            for command in (command,
                            [python, '-m', 'icon_set', 'release', str(bundle / 'assets')]):
                result = runner(command, cwd=source, env=environment, stdout=log, stderr=subprocess.STDOUT)
                if result.returncode:
                    failed = releases / f'failed-{revision}.log'
                    log.flush()
                    shutil.copy2(bundle / 'build.log', failed)
                    raise RuntimeError(f'Release preparation failed; current production kept. See {failed}')
        catalog = json.loads((bundle / 'assets/gallery/icons.json').read_text())
        if not catalog.get('icons') and not catalog.get('failed_icons'):
            raise ValueError('Refusing an empty release.')
        shutil.rmtree(source / 'icon_set/.local', ignore_errors=True)
        (bundle / 'deployment.json').write_text(json.dumps({'commit': revision}, indent=2) + '\n')
        # Unique names allow retrying an older commit without overwriting a release.
        name = revision + '-' + bundle.name.removeprefix('.preparing-')
        result = releases / name
        manifest = bundle / 'assets/release.json'
        release = json.loads(manifest.read_text())
        release.update(commit=revision, deployment_id=name)
        manifest.write_text(json.dumps(release, indent=2) + '\n')
        bundle.rename(result)
        return result


def server_command(bundle, python, database, host, port, primitives=None):
    command = [python, str(bundle / 'source/icon_set/scripts/deploy.py'), '--production',
               '--dist', str(bundle / 'assets'), '--database', str(database),
               '--host', host, '--port', str(port)]
    if primitives:
        command += ['--primitives', str(primitives)]
    return command


def wait_healthy(deploy, host, port, timeout=30, expected_release=None):
    address = '127.0.0.1' if host in ('0.0.0.0', '') else ('[::1]' if host == '::' else host)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if deploy.died():
            raise RuntimeError('New production server exited before becoming healthy.')
        try:
            with urlopen(f'http://{address}:{port}/api/runtime', timeout=1) as response:
                runtime = json.load(response)
            with urlopen(f'http://{address}:{port}/gallery/icons.json', timeout=1) as response:
                catalog = json.load(response)
            with urlopen(f'http://{address}:{port}/release.json', timeout=1) as response:
                release = json.load(response)
            if (runtime.get('mode') == 'production' and (catalog.get('icons') or catalog.get('failed_icons'))
                    and (expected_release is None or release.get('deployment_id') == expected_release)
                    and not deploy.died()):
                return
        except (OSError, ValueError):
            pass
        time.sleep(0.2)
    raise RuntimeError('Production startup health check timed out.')


def activate(releases, candidate, current, factory, health):
    """Restore the old server on failure; commit the active pointer only when ready."""
    old = read_active(releases)
    if current:
        current.stop()
    new = None
    try:
        new = factory(candidate)
        new.start()
        health(new)
        marker = {'release': candidate.name, 'commit': json.loads((candidate/'deployment.json').read_text())['commit'],
                  'previous': old['release'] if old else None}
        temporary = Path(releases) / '.active.json.tmp'
        temporary.write_text(json.dumps(marker, indent=2) + '\n')
        temporary.replace(Path(releases) / 'active.json')
        return new
    except BaseException:
        if new:
            new.stop()
        if current:
            current.start()
        raise


def run(args, repo, deployment_class, remote_head, log):
    releases, database = validate_paths(repo, args.release_root, args.database)
    if args.interval <= 0 or not 1 <= args.port <= 65535:
        raise ValueError('Use a positive polling interval and a port from 1 to 65535.')
    releases.mkdir(parents=True, exist_ok=True)
    # Also prevents concurrent watcher processes from racing over the shared state.
    with output_lock(releases / 'watcher'), output_lock(database.parent / 'production-server'):
        return _watch(args, repo, releases, database, deployment_class, remote_head, log)


def _watch(args, repo, releases, database, deployment_class, remote_head, log):
    import signal
    def factory(bundle):
        server = deployment_class(server_command(bundle, args.python, database, args.host, args.port, args.primitives),
                                  cwd=bundle / 'source')
        server.release_id = bundle.name
        return server
    health = lambda deploy: wait_healthy(deploy, args.host, args.port, args.health_timeout, deploy.release_id)
    stopping = False
    def shutdown(signum, frame):
        nonlocal stopping
        stopping = True
    previous_handlers = {sig: signal.signal(sig, shutdown) for sig in (signal.SIGINT, signal.SIGTERM)}
    current = None
    attempted = None
    try:
        active = read_active(releases)
        if active:
            current = factory(bundle_path(releases, active['release']))
            current.start()
            health(current)
        while not stopping:
            try:
                revision = remote_head(args.remote, args.branch)
                active = read_active(releases)
                if revision != (active or {}).get('commit') and revision != attempted:
                    attempted = revision
                    previous = bundle_path(releases, active['release']) if active else None
                    log(f'Preparing release {revision[:12]}; ' +
                        ('current server stays available during the build.' if current else 'first build; server starts after preparation.'))
                    candidate = prepare(repo, releases, revision, args.python, previous)
                    manifest = json.loads((candidate / 'assets/release.json').read_text())
                    if manifest.get('failed_icons'):
                        log(f"{manifest['failed_icons']} drawings need review; continuing deployment with the Failed build gallery.")
                    if stopping:
                        break
                    current = activate(releases, candidate, current, factory, health)
                    log(f'Production now serves {revision[:12]}. Previous release retained.')
            except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                log(str(error))
                if current is None:
                    return 1
            if current and current.died() and not args.no_restart_on_crash:
                current.start()
            deadline = time.monotonic() + args.interval
            while not stopping and time.monotonic() < deadline:
                time.sleep(min(1, max(0, deadline-time.monotonic())))
    finally:
        if current:
            current.stop()
        for sig, handler in previous_handlers.items():
            signal.signal(sig, handler)
    return 0
