#!/usr/bin/env python3
"""Upload folders of files that never change (references, the built site) to R2.

    # Local rehearsal through `wrangler dev` (small folders; each file is one request):
    python3 cloud/migrate/push_files.py --backend http --base-url http://127.0.0.1:8787 \\
        published/gallery=site/gallery

    # Remote bulk upload straight to R2's S3 API (no Worker requests used):
    python3 cloud/migrate/push_files.py --backend s3 \\
        published=site pictographic-primitives=references/primitives \\
        pictographic-combinations=references/combinations icon_set/references=references/library

Each argument is SOURCE=PREFIX. Only .html .json .svg .png .css .js files are sent. The S3 backend
skips objects whose MD5 already matches (safe to rerun after an interruption); it needs
R2 credentials in cloud/.env: R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY (create an R2 API token in
the Cloudflare dashboard) and uses the account id from CLOUDFLARE_ACCOUNT_ID or wrangler.toml.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import mimetypes
from pathlib import Path
import sys
import threading
import urllib.parse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

ROOT = cloudapi.ROOT
BUCKET = 'pictographic-review'
SUFFIXES = {'.html', '.json', '.svg', '.png', '.css', '.js'}
TYPES = {'.svg': 'image/svg+xml', '.json': 'application/json', '.js': 'text/javascript; charset=utf-8',
         '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.png': 'image/png'}


def files(source: Path, prefix: str, skip: set[str]):
    for path in sorted(source.rglob('*')):
        relative = path.relative_to(source)
        if not path.is_file() or path.suffix.lower() not in SUFFIXES or any(p.startswith('.') for p in relative.parts):
            continue
        key = f'{prefix.rstrip("/")}/{relative.as_posix()}'
        if key in skip:
            continue
        yield path, key


def account_id() -> str:
    config = cloudapi.settings()
    if config.get('CLOUDFLARE_ACCOUNT_ID'):
        return config['CLOUDFLARE_ACCOUNT_ID']
    for line in (ROOT / 'cloud' / 'worker' / 'wrangler.toml').read_text().splitlines():
        if line.startswith('account_id'):
            return line.split('=', 1)[1].strip().strip('"')
    raise SystemExit('error: set CLOUDFLARE_ACCOUNT_ID in cloud/.env')


class S3:
    def __init__(self):
        import boto3
        from botocore.config import Config
        config = cloudapi.settings()
        if not config.get('R2_ACCESS_KEY_ID') or not config.get('R2_SECRET_ACCESS_KEY'):
            raise SystemExit('error: add R2_ACCESS_KEY_ID and R2_SECRET_ACCESS_KEY to cloud/.env (R2 API token, Object Read & Write)')
        self.client = boto3.client('s3', endpoint_url=f'https://{account_id()}.r2.cloudflarestorage.com',
                                   aws_access_key_id=config['R2_ACCESS_KEY_ID'],
                                   aws_secret_access_key=config['R2_SECRET_ACCESS_KEY'],
                                   region_name='auto', config=Config(max_pool_connections=64, retries={'max_attempts': 5}))

    def existing(self, prefix: str) -> dict[str, str]:
        """key -> ETag (the MD5 of single-part uploads)."""
        found = {}
        for page in self.client.get_paginator('list_objects_v2').paginate(Bucket=BUCKET, Prefix=prefix.rstrip('/') + '/'):
            for item in page.get('Contents', []):
                found[item['Key']] = item['ETag'].strip('"')
        return found

    def put(self, key: str, content: bytes, content_type: str) -> None:
        self.client.put_object(Bucket=BUCKET, Key=key, Body=content, ContentType=content_type)


class Http:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token = cloudapi.push_token(base_url)

    def existing(self, prefix: str) -> dict[str, str]:
        return {}

    def put(self, key: str, content: bytes, content_type: str) -> None:
        status, body = cloudapi.request(self.base_url, 'PUT', '/api/files/' + urllib.parse.quote(key), body=content,
                                        content_type=content_type, token=self.token, timeout=300)
        if status >= 400:
            raise RuntimeError(f'{key}: HTTP {status} {body[:120]!r}')


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mappings', nargs='+', help='SOURCE=PREFIX, e.g. published=site')
    parser.add_argument('--backend', choices=('http', 's3'), required=True)
    parser.add_argument('--base-url', help='Worker URL for --backend http')
    parser.add_argument('--jobs', type=int, default=16)
    parser.add_argument('--skip', action='append', default=['site/gallery/icons.json'],
                        help='keys to leave alone (icons.json is written by push_catalog.py)')
    args = parser.parse_args(argv)
    if args.backend == 'http' and not args.base_url:
        parser.error('--backend http needs --base-url')
    backend = S3() if args.backend == 's3' else Http(args.base_url)
    skip = set(args.skip)
    total_sent = total_same = 0
    for mapping in args.mappings:
        source, _, prefix = mapping.partition('=')
        source_path = (ROOT / source).resolve() if not Path(source).is_absolute() else Path(source)
        if not prefix or not source_path.is_dir():
            parser.error(f'{mapping}: expected an existing SOURCE folder and a PREFIX')
        existing = backend.existing(prefix)
        todo = []
        for path, key in files(source_path, prefix, skip):
            content = path.read_bytes()
            if existing.get(key) == hashlib.md5(content).hexdigest():
                total_same += 1
                continue
            todo.append((key, path))
        lock, done = threading.Lock(), [0]
        failures = []

        def send(key, path):
            content = path.read_bytes()
            backend.put(key, content, TYPES.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or 'application/octet-stream')
            with lock:
                done[0] += 1
                if done[0] % 500 == 0 or done[0] == len(todo):
                    print(f'  {prefix}: {done[0]}/{len(todo)}', flush=True)

        print(f'{source} -> {prefix}: {len(todo)} to send, {len(existing)} already stored', flush=True)
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {pool.submit(send, key, path): key for key, path in todo}
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as error:  # report every failure, keep going
                    failures.append(f'{futures[future]}: {error}')
        total_sent += len(todo) - len(failures)
        if failures:
            print(f'{len(failures)} failed in {prefix}; rerun to retry:', *failures[:20], sep='\n  ', file=sys.stderr)
            return 1
    print(f'done: {total_sent} sent, {total_same} unchanged')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
