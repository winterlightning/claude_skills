"""Incrementally update a persistent cache and alternate two bounded release slots."""
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
    target.mkdir(parents=True, exist_ok=True)
    seen = set()
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
                    seen.add(path)
                    if member.isdir():
                        path.mkdir(parents=True, exist_ok=True)
                    elif member.isfile():
                        path.parent.mkdir(parents=True, exist_ok=True)
                        with archive.extractfile(member) as stream:
                            content = stream.read()
                        if path.is_file() and not path.is_symlink() and path.read_bytes() == content:
                            path.chmod(member.mode & 0o777)
                            continue
                        if path.is_symlink():
                            raise ValueError('Symlink found in build workspace.')
                        path.write_bytes(content)
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
    # Remove sources deleted by the commit, but keep the persistent output cache.
    for path in sorted(target.rglob('*'), reverse=True):
        relative = path.relative_to(target)
        if '.local' in relative.parts:
            continue
        if path.is_file() and path not in seen:
            path.unlink()
        elif path.is_dir() and path not in seen and not any(path.iterdir()):
            path.rmdir()


def sync_tree(source, target, excluded=()):
    """Overwrite changed files only, prune deleted files, and never use hardlinks."""
    source, target = Path(source), Path(target)
    target.mkdir(parents=True, exist_ok=True)
    names = set()
    for item in source.iterdir():
        if item.name in excluded or item.name.startswith('.icon-build-'):
            continue
        if item.is_symlink():
            raise ValueError(f'Symlink is not allowed in published output: {item}')
        names.add(item.name)
        dest = target / item.name
        if dest.is_symlink():
            raise ValueError(f'Symlink is not allowed in release storage: {dest}')
        if dest.exists() and dest.is_dir() != item.is_dir():
            shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
        if item.is_dir():
            sync_tree(item, dest, excluded)
        elif not dest.exists() or not filecmp.cmp(item, dest, shallow=False):
            shutil.copy2(item, dest)
    for item in target.iterdir():
        if item.name not in names:
            shutil.rmtree(item) if item.is_dir() and not item.is_symlink() else item.unlink()


def publish_cache(build, assets, revision, identity):
    import hashlib
    catalog = json.loads((build / 'gallery/icons.json').read_text())
    if not (build / 'gallery/index.html').is_file() or not (catalog.get('icons') or catalog.get('failed_icons')):
        raise ValueError('Refusing an empty release.')
    for path in build.rglob('manifest.json'):
        if any(row.get('artwork_source', 'use_org') != 'use_org'
               for row in json.loads(path.read_text()).get('icons', [])):
            raise ValueError('Baseline contains manual artwork; preserve it in production state instead.')
    sync_tree(build, assets, excluded=('release.json', '__pycache__', '.DS_Store'))
    (assets / 'release.json').write_text(json.dumps({
        'schema_version': 1, 'commit': revision, 'deployment_id': identity,
        'catalog_sha256': hashlib.sha256((assets / 'gallery/icons.json').read_bytes()).hexdigest(),
        'icons': len(catalog.get('icons', [])), 'failed_icons': len(catalog.get('failed_icons', [])),
        'artwork': 'python-originals',
    }, indent=2) + '\n')


def prepare(repo, releases, revision, python, previous=None, runner=subprocess.run, seed=None):
    """Reuse a persistent build cache and overwrite only the inactive release slot."""
    releases = Path(releases)
    workspace = releases / 'workspace'
    source = workspace / 'source'
    snapshot(repo, revision, source, previous / 'source' if previous else None)
    build = source / 'icon_set/.local/dist'
    if not (build / 'gallery/icons.json').is_file():
        baseline = previous / 'assets' if previous else seed
        if baseline is None:
            for path in (Path(repo) / 'icon_set/.local/dist', Path(repo) / 'icon_set/dist'):
                if (path / 'gallery/icons.json').is_file():
                    baseline = path
                    break
        if baseline is None or not (Path(baseline) / 'gallery/icons.json').is_file():
            raise ValueError('No existing gallery to reuse. Pass --seed-dist PATH to your old built gallery; no full build was started.')
        baseline = Path(baseline).resolve()
        if build.resolve().is_relative_to(baseline) or baseline.is_relative_to(build.resolve()):
            raise ValueError('Seed gallery must be separate from the build cache.')
        print(f'Reusing existing gallery: {baseline}', flush=True)
        sync_tree(baseline, build, excluded=('release.json', '.DS_Store'))
    else:
        print(f'Reusing build cache: {build}', flush=True)
    environment = dict(os.environ, PYTHONUNBUFFERED='1')
    environment.pop('PYTHONPATH', None)
    command = [python, '-m', 'icon_set', 'build', '--no-png', '--no-report',
               '--changed-only', '--allow-validation-failures']
    with (workspace / 'build.log').open('w') as log:
        result = runner(command, cwd=source, env=environment, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            log.flush()
            shutil.copy2(workspace / 'build.log', releases / 'last-failed.log')
            raise RuntimeError(f'Release preparation failed; current production kept. See {releases / "last-failed.log"}')
    active_name = (read_active(releases) or {}).get('release')
    slot = 'slot-b' if (previous and previous.name == 'slot-a') or active_name == 'slot-a' else 'slot-a'
    candidate = bundle_path(releases, slot)
    candidate.mkdir(exist_ok=True)
    identity = revision + '-' + str(time.time_ns())
    publish_cache(build, candidate / 'assets', revision, identity)
    sync_tree(source, candidate / 'source', excluded=('.local', '__pycache__', '.DS_Store'))
    (candidate / 'deployment.json').write_text(json.dumps({'commit': revision}) + '\n')
    shutil.copy2(workspace / 'build.log', candidate / 'build.log')
    return candidate


def cleanup_releases(releases):
    """Bound storage; remove only recognisable retired deployment artifacts."""
    import re
    active = read_active(releases) or {}
    keep = {active.get('release'), active.get('previous'), 'workspace', 'slot-a', 'slot-b'}
    for path in Path(releases).iterdir():
        if path.name in keep or path.is_symlink():
            continue
        old_release = re.fullmatch(r'[0-9a-f]{40}-[a-zA-Z0-9_-]+', path.name)
        abandoned = path.name.startswith('.preparing-') and (path / 'source').is_dir()
        if path.is_dir() and ((old_release and (path / 'deployment.json').is_file()) or abandoned):
            shutil.rmtree(path)
        elif path.is_file() and re.fullmatch(r'failed-[0-9a-f]{40}\.log', path.name):
            path.unlink()


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
            # Readiness must not serialize the entire library and merge manual edits.
            with urlopen(f'http://{address}:{port}/gallery/index.html', timeout=2) as response:
                gallery_ready = bool(response.read(1024))
            release = {}
            if expected_release is not None:
                with urlopen(f'http://{address}:{port}/release.json', timeout=1) as response:
                    release = json.load(response)
            if (runtime.get('mode') == 'production' and gallery_ready
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


def select_baseline(repo, releases, seed=None):
    active = read_active(releases)
    candidates = ([bundle_path(releases, active['release']) / 'assets'] if active else [])
    candidates += ([Path(seed)] if seed else [])
    candidates += [Path(releases)/'workspace/source/icon_set/.local/dist',
                   Path(repo)/'icon_set/.local/dist', Path(repo)/'icon_set/dist']
    for path in candidates:
        if (path/'gallery/index.html').is_file() and (path/'gallery/icons.json').is_file():
            return path.resolve()
    raise ValueError('No existing gallery. Restore the old gallery or pass --seed-dist; no full build started.')


def write_marker(releases, marker):
    temporary = Path(releases) / '.active.json.tmp'
    temporary.write_text(json.dumps(marker, indent=2) + '\n')
    temporary.replace(Path(releases) / 'active.json')


def bootstrap(releases, baseline):
    """Freeze the existing gallery before the build cache is modified."""
    if read_active(releases):
        return
    candidate = bundle_path(releases, 'slot-a')
    assets = candidate / 'assets'
    if baseline.resolve() != assets.resolve():
        sync_tree(baseline, assets)
    (assets/'release.json').write_text(json.dumps({'deployment_id': 'bootstrap'}) + '\n')
    (candidate/'deployment.json').write_text('{"commit": null}\n')
    write_marker(releases, {'release': 'slot-a', 'commit': None, 'previous': None})


def promote_live(releases, candidate, current, health):
    """Atomically select finished data; retain the same serving process and state."""
    old = read_active(releases)
    revision = json.loads((candidate/'deployment.json').read_text())['commit']
    identity = json.loads((candidate/'assets/release.json').read_text())['deployment_id']
    write_marker(releases, {'release': candidate.name, 'commit': revision,
                            'previous': old['release'] if old else None})
    try:
        health(current, identity)
    except BaseException:
        if old is not None:
            write_marker(releases, old)
        else:
            (Path(releases)/'active.json').unlink()
        raise


def supervised_build(command, stop, **kwargs):
    """Permit shutdown while a build runs in the background."""
    import signal
    proc = subprocess.Popen(command, start_new_session=True, **kwargs)
    try:
        while proc.poll() is None:
            if stop.wait(0.25):
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait()
                break
        return subprocess.CompletedProcess(command, proc.returncode)
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, signal.SIGTERM)
            proc.wait()


def _watch(args, repo, releases, database, deployment_class, remote_head, log):
    import signal
    from concurrent.futures import ThreadPoolExecutor
    from threading import Event
    stop = Event()
    previous_handlers = {sig: signal.signal(sig, lambda *_: stop.set())
                         for sig in (signal.SIGINT, signal.SIGTERM)}
    current = None
    executor = ThreadPoolExecutor(max_workers=1)
    pending = None
    attempted = None
    next_poll = 0
    health = lambda server, identity=None: wait_healthy(server, args.host, args.port, args.health_timeout, identity)
    try:
        baseline = select_baseline(repo, releases, getattr(args, 'seed_dist', None))
        # Legacy galleries inside the checkout must be copied out once before production serves them.
        if baseline.is_relative_to(Path(repo).resolve()):
            bootstrap(releases, baseline)
            baseline = bundle_path(releases, read_active(releases)['release'])/'assets'
        command = [args.python, str(Path(repo)/'icon_set/scripts/deploy.py'), '--production',
                   '--dist', str(baseline), '--database', str(database), '--live-release-root', str(releases),
                   '--host', args.host, '--port', str(args.port)]
        if args.primitives:
            command += ['--primitives', str(args.primitives)]
        current = deployment_class(command, cwd=repo)
        current.start()
        health(current)
        log(f'Server is online on port {args.port}. Existing gallery and production data are available.')
        bootstrap(releases, baseline)
        while not stop.is_set():
            if current.died() and not args.no_restart_on_crash:
                log('Server exited; restarting it while background preparation continues.')
                current.start()
            if pending is not None and pending.done():
                try:
                    candidate = pending.result()
                    if stop.is_set():
                        break
                    promote_live(releases, candidate, current, health)
                    cleanup_releases(releases)
                    log(f'Gallery updated to {attempted[:12]}. Server stayed running.')
                except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                    log(f'Update failed; existing gallery stays online: {error}')
                pending = None
            if pending is None and time.monotonic() >= next_poll:
                next_poll = time.monotonic() + args.interval
                try:
                    revision = remote_head(args.remote, args.branch)
                    active = read_active(releases)
                    if revision != (active or {}).get('commit') and revision != attempted:
                        attempted = revision
                        previous = bundle_path(releases, active['release']) if active else None
                        log(f'Preparing {revision[:12]} in the background; server remains online.')
                        pending = executor.submit(prepare, repo, releases, revision, args.python, previous,
                            runner=lambda cmd, **kw: supervised_build(cmd, stop, **kw),
                            seed=getattr(args, 'seed_dist', None))
                except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                    log(f'Could not check for updates; server stays online: {error}')
            stop.wait(0.5)
    finally:
        stop.set()
        if current:
            current.stop()
        executor.shutdown(wait=True)
        for sig, handler in previous_handlers.items():
            signal.signal(sig, handler)
    return 0
