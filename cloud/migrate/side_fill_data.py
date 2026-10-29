#!/usr/bin/env python3
"""The fill side pairs snapshot (icon_set/data/side-fill): data, kept in R2, never in git.

Its files (layouts, review decisions, region recipes, the source / fill / backup SVGs) are stored by content, each
once: references/side-fill-data/objects/<sha256>, never overwritten. references/side-fill-data/manifest.json maps each
path to its sha256 and is written last, so a push that fails part way leaves the previous snapshot whole and
restorable, and a checkout restores exactly the snapshot the scripts were run on. The folder is ignored by git.

    python3 cloud/migrate/side_fill_data.py pull                           # a fresh checkout: everything from R2
    python3 cloud/migrate/side_fill_data.py check                          # local files against the manifest
    python3 cloud/migrate/side_fill_data.py manifest                       # after changing files: write manifest.json
    python3 cloud/migrate/side_fill_data.py push --backend s3              # then send what R2 lacks (cloud/.env R2 keys)
    python3 cloud/migrate/side_fill_data.py push --backend http --base-url http://localhost:8821   # a local Worker

push sends only the contents R2 does not hold yet, then the manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import push_files  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / 'icon_set/data/side-fill'
PREFIX = 'references/side-fill-data'
OBJECTS = f'{PREFIX}/objects'


def manifest_path() -> Path:
    return DATA / 'manifest.json'


def local_files() -> dict[str, Path]:
    """Every snapshot file but the manifest itself and dotfiles (.gitignore)."""
    return {p.relative_to(DATA).as_posix(): p for p in sorted(DATA.rglob('*'))
            if p.is_file() and p != manifest_path() and not any(part.startswith('.') for part in p.relative_to(DATA).parts)}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest() -> dict[str, str]:
    path = manifest_path()
    return json.loads(path.read_text())['files'] if path.is_file() else {}


class S3Store:
    """R2 through its S3 API (cloud/.env keys)."""
    def __init__(self):
        self.s3 = push_files.S3()

    def existing(self, prefix):
        return self.s3.existing(prefix)

    def put(self, key, content, content_type):
        self.s3.put(key, content, content_type)

    def get(self, key):
        return self.s3.client.get_object(Bucket=push_files.BUCKET, Key=key)['Body'].read()


class HttpStore:
    """A Worker's PUT /api/files (push only)."""
    def __init__(self, base_url):
        self.http = push_files.Http(base_url)

    def existing(self, prefix):
        return self.http.existing(prefix)

    def put(self, key, content, content_type):
        self.http.put(key, content, content_type)

    def get(self, key):
        raise SystemExit('error: pull reads R2 through its S3 API (--backend s3)')


def write_manifest() -> int:
    files = {name: sha(path) for name, path in local_files().items()}
    manifest_path().write_text(json.dumps({'schema': 'side-fill-data/v2', 'prefix': PREFIX, 'objects': OBJECTS, 'files': files},
                                          indent=0, sort_keys=True) + '\n')
    print(f'{len(files)} files in {manifest_path().relative_to(REPO) if manifest_path().is_relative_to(REPO) else manifest_path()}')
    return 0


def check() -> int:
    want, have = manifest(), local_files()
    if not want:
        print('no manifest here: `pull` fetches it (and the files) from R2')
        return 1
    missing = [n for n in want if n not in have]
    changed = [n for n in want if n in have and sha(have[n]) != want[n]]
    extra = [n for n in have if n not in want]
    print(f'{len(want)} in the manifest: {len(want) - len(missing) - len(changed)} here, {len(missing)} missing, '
          f'{len(changed)} changed; {len(extra)} not in the manifest')
    for name in (missing + changed + extra)[:10]:
        print('  ', name)
    return 1 if missing or changed or extra else 0


def push(store, jobs: int = 16) -> int:
    """Each content once under objects/<sha256> (never overwritten), then the manifest: a push that fails part way
    leaves the manifest R2 had, and every object it names, as they were."""
    want, have = manifest(), local_files()
    if set(want) != set(have) or any(sha(have[n]) != want[n] for n in want):
        raise SystemExit('error: the files differ from manifest.json; run `manifest` first (or `check` to see how)')
    stored = {key.rsplit('/', 1)[-1] for key in store.existing(OBJECTS)}
    todo = {digest: have[name] for name, digest in want.items() if digest not in stored}
    print(f'{len(want)} files, {len(set(want.values()))} contents; {len(todo)} to send', flush=True)
    failures = []

    def send(job):
        digest, path = job
        try:
            store.put(f'{OBJECTS}/{digest}', path.read_bytes(), 'application/octet-stream')
        except Exception as error:  # report every failure, keep sending the rest
            failures.append(f'{digest} ({path.name}): {error}')
    with ThreadPoolExecutor(jobs) as pool:
        for n, _ in enumerate(pool.map(send, todo.items()), 1):
            if n % 1000 == 0 or n == len(todo):
                print(f'  sent {n}/{len(todo)} ({len(failures)} failed)', flush=True)
    for line in failures[:10]:
        print('  failed', line)
    if failures:
        print('the manifest was not replaced: R2 still holds the previous snapshot')
        return 1
    store.put(f'{PREFIX}/manifest.json', manifest_path().read_bytes(), 'application/json')
    return 0


def pull(store, jobs: int = 16) -> int:
    body = store.get(f'{PREFIX}/manifest.json')
    want = json.loads(body)['files']
    have = local_files()
    todo = [n for n, digest in want.items() if n not in have or sha(have[n]) != digest]
    print(f'{len(want)} files in the manifest; {len(todo)} to download', flush=True)
    failures = []

    def fetch(name):
        data = store.get(f'{OBJECTS}/{want[name]}')
        if hashlib.sha256(data).hexdigest() != want[name]:
            failures.append(f'{name}: R2 holds another content under its sha')
            return
        target = DATA / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    with ThreadPoolExecutor(jobs) as pool:
        list(pool.map(fetch, todo))
    for line in failures[:10]:
        print('  failed', line)
    if failures:
        return 1
    DATA.mkdir(parents=True, exist_ok=True)
    manifest_path().write_bytes(body)          # last: the local manifest names only files that are here
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=['manifest', 'check', 'push', 'pull'])
    parser.add_argument('--backend', choices=('http', 's3'), default='s3')
    parser.add_argument('--base-url')
    parser.add_argument('--jobs', type=int, default=16)
    args = parser.parse_args(argv)
    if args.command == 'manifest':
        return write_manifest()
    if args.command == 'check':
        return check()
    if args.backend == 'http' and not args.base_url:
        parser.error('--backend http needs --base-url')
    store = HttpStore(args.base_url) if args.backend == 'http' else S3Store()
    return push(store, args.jobs) if args.command == 'push' else pull(store, args.jobs)


if __name__ == '__main__':
    raise SystemExit(main())
