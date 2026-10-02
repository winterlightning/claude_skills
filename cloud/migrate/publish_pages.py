#!/usr/bin/env python3
"""Upload chosen pages from published/gallery to a site's R2 (site/gallery/<name>), and check they are served.

    python3 cloud/migrate/publish_pages.py --bucket pictographic-review-next primitives.html side-pairs-grid.js …
    python3 cloud/migrate/publish_pages.py --bucket pictographic-review --side-pairs        # the Side pairs page set

--side-pairs: the files of Progression › Side pairs (the restored page on D1 and combine-side.js). Each file is
uploaded as it is in published/gallery, then fetched from the site and compared (md5) when --site is given or the
bucket is one of the two known sites.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_files import S3  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
GALLERY = ROOT / 'published' / 'gallery'
SIDE_PAIRS = ['primitives.html', 'side-pairs.html', 'side-pairs-data.js', 'progression-combinations.js', 'side-layout-editor.js',
              'side-pairs-grid.js', 'side-pair-maker.js', 'combine-side.js']
SITES = {'pictographic-review': 'https://pictographic-review.pictographic.workers.dev',
         'pictographic-review-next': 'https://pictographic-review-next.pictographic.workers.dev'}
TYPES = {'html': 'text/html; charset=utf-8', 'js': 'text/javascript; charset=utf-8', 'css': 'text/css; charset=utf-8',
         'json': 'application/json'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('names', nargs='*')
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--side-pairs', action='store_true', help='the Side pairs page set')
    parser.add_argument('--site', help='site URL to check against (default: the bucket\'s known site)')
    args = parser.parse_args()
    names = list(dict.fromkeys(args.names + (SIDE_PAIRS if args.side_pairs else [])))
    if not names:
        parser.error('name the files, or use --side-pairs')
    missing = [n for n in names if not (GALLERY / n).is_file()]
    if missing:
        raise SystemExit('error: not in published/gallery: ' + ', '.join(missing))
    client, site, bad = S3().client, args.site or SITES.get(args.bucket), []
    for name in names:
        body = (GALLERY / name).read_bytes()
        client.put_object(Bucket=args.bucket, Key='site/gallery/' + name, Body=body, ContentType=TYPES.get(name.rsplit('.', 1)[-1], 'application/octet-stream'))
        local = hashlib.md5(body).hexdigest()
        served = ''
        if site:
            request = urllib.request.Request(f'{site}/gallery/{name}', headers={'User-Agent': 'pictographic-migrate/1.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(request, timeout=60) as response:
                served = hashlib.md5(response.read()).hexdigest()
            if served != local:
                bad.append(name)
        print(f'{name:32} {local[:10]}' + (f'  served {served[:10]}' + ('' if served == local else '  DIFFERS') if site else ''))
    if bad:
        print('error: the site serves something else for: ' + ', '.join(bad))
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
