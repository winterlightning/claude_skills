#!/usr/bin/env python3
"""Copy every object of one R2 bucket into another, server-side (the source is only read).

    python3 cloud/migrate/copy_bucket.py pictographic-review pictographic-review-next [--prefix site/]

Used to give the test Worker (wrangler.next.toml) its own copy of production's files, and to refresh
it. Objects whose ETag already matches in the target are skipped, so a rerun only copies what changed.
Needs R2_ACCESS_KEY_ID / R2_SECRET_ACCESS_KEY in cloud/.env (see push_files.py).
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import threading

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_files import S3  # noqa: E402


def listing(client, bucket: str, prefix: str) -> dict[str, str]:
    objects = {}
    for page in client.get_paginator('list_objects_v2').paginate(Bucket=bucket, Prefix=prefix):
        for item in page.get('Contents', []):
            objects[item['Key']] = item['ETag']
    return objects


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('source')
    parser.add_argument('target')
    parser.add_argument('--prefix', default='')
    parser.add_argument('--jobs', type=int, default=32)
    args = parser.parse_args()
    if args.source == args.target:
        sys.exit('source and target must differ')

    client = S3().client
    source = listing(client, args.source, args.prefix)
    target = listing(client, args.target, args.prefix)
    todo = [key for key, etag in source.items() if target.get(key) != etag]
    print(f'{len(source)} objects in {args.source}, {len(source) - len(todo)} already in {args.target}, copying {len(todo)}')

    done = 0
    failed = []
    lock = threading.Lock()

    def copy(key: str) -> None:
        nonlocal done
        try:
            client.copy_object(Bucket=args.target, Key=key, CopySource={'Bucket': args.source, 'Key': key})
        except Exception as error:  # noqa: BLE001 - report and continue, a rerun retries
            with lock:
                failed.append((key, str(error)))
        with lock:
            done += 1
            if done % 2000 == 0:
                print(f'  {done}/{len(todo)}', flush=True)

    with ThreadPoolExecutor(args.jobs) as pool:
        list(pool.map(copy, todo))
    print(f'copied {len(todo) - len(failed)}, failed {len(failed)}')
    for key, error in failed[:20]:
        print(f'  {key}: {error}')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
