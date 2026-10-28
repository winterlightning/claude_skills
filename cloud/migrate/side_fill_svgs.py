#!/usr/bin/env python3
"""The SVG drawings of the fill side pairs snapshot (icon_set/data/side-fill): kept in R2, not in git.

The JSON of the snapshot (layouts, review decisions, region recipes) is tracked; its 8,000-odd SVG drawings (sources,
fills, the preserved backup) are R2 objects under references/side-fill-data/<path>, and svg-manifest.json (tracked)
names each one with its sha256, so a checkout knows exactly which drawings its JSON was made from.

    python3 cloud/migrate/side_fill_svgs.py manifest                       # write svg-manifest.json from the files
    python3 cloud/migrate/side_fill_svgs.py check                          # local files against the manifest
    python3 cloud/migrate/side_fill_svgs.py push --backend http --base-url http://localhost:8821   # through a Worker
    python3 cloud/migrate/side_fill_svgs.py push --backend s3              # straight to R2 (cloud/.env R2 keys)
    python3 cloud/migrate/side_fill_svgs.py pull                           # missing or changed files from R2 (S3 API)

push sends only what R2 does not hold already (S3: by MD5; through a Worker every file is sent).
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
MANIFEST = DATA / 'svg-manifest.json'
PREFIX = 'references/side-fill-data'


def local_svgs() -> dict[str, Path]:
    return {p.relative_to(DATA).as_posix(): p for p in sorted(DATA.rglob('*.svg'))
            if not any(part.startswith('.') for part in p.relative_to(DATA).parts)}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest() -> dict[str, str]:
    return json.loads(MANIFEST.read_text())['files'] if MANIFEST.is_file() else {}


def write_manifest() -> int:
    files = {name: sha(path) for name, path in local_svgs().items()}
    MANIFEST.write_text(json.dumps({'schema': 'side-fill-svgs/v1', 'prefix': PREFIX, 'files': files}, indent=0, sort_keys=True) + '\n')
    print(f'{len(files)} SVGs in {MANIFEST.relative_to(REPO)}')
    return 0


def check() -> int:
    want, have = manifest(), local_svgs()
    missing = [n for n in want if n not in have]
    changed = [n for n in want if n in have and sha(have[n]) != want[n]]
    extra = [n for n in have if n not in want]
    print(f'{len(want)} in the manifest: {len(want) - len(missing) - len(changed)} here, {len(missing)} missing, '
          f'{len(changed)} changed; {len(extra)} not in the manifest')
    for name in (missing + changed + extra)[:10]:
        print('  ', name)
    return 1 if missing or changed or extra else 0


def push(backend_name: str, base_url: str | None, jobs: int) -> int:
    want, have = manifest(), local_svgs()
    if set(want) != set(have) or any(sha(have[n]) != want[n] for n in want):
        raise SystemExit('error: the files differ from svg-manifest.json; run `manifest` first (or `check` to see how)')
    backend = push_files.S3() if backend_name == 's3' else push_files.Http(base_url)
    existing = backend.existing(PREFIX)
    todo = [(f'{PREFIX}/{name}', path) for name, path in have.items()
            if existing.get(f'{PREFIX}/{name}') != hashlib.md5(path.read_bytes()).hexdigest()]
    print(f'{len(have)} SVGs; {len(have) - len(todo)} in R2 already; {len(todo)} to send', flush=True)
    failures = []

    def send(job):
        key, path = job
        try:
            backend.put(key, path.read_bytes(), 'image/svg+xml')
        except Exception as error:  # report every failure, keep sending the rest
            failures.append(f'{key}: {error}')
    with ThreadPoolExecutor(jobs) as pool:
        for n, _ in enumerate(pool.map(send, todo), 1):
            if n % 1000 == 0 or n == len(todo):
                print(f'  sent {n}/{len(todo)} ({len(failures)} failed)', flush=True)
    for line in failures[:10]:
        print('  failed', line)
    return 1 if failures else 0


def pull(jobs: int) -> int:
    want, have = manifest(), local_svgs()
    todo = [n for n, digest in want.items() if n not in have or sha(have[n]) != digest]
    print(f'{len(want)} SVGs in the manifest; {len(todo)} to download', flush=True)
    if not todo:
        return 0
    client = push_files.S3().client
    failures = []

    def fetch(name):
        body = client.get_object(Bucket=push_files.BUCKET, Key=f'{PREFIX}/{name}')['Body'].read()
        if hashlib.sha256(body).hexdigest() != want[name]:
            failures.append(f'{name}: R2 holds another drawing')
            return
        target = DATA / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
    with ThreadPoolExecutor(jobs) as pool:
        list(pool.map(fetch, todo))
    for line in failures[:10]:
        print('  failed', line)
    return 1 if failures else 0


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
    if args.command == 'push':
        if args.backend == 'http' and not args.base_url:
            parser.error('push --backend http needs --base-url')
        return push(args.backend, args.base_url, args.jobs)
    return pull(args.jobs)


if __name__ == '__main__':
    raise SystemExit(main())
