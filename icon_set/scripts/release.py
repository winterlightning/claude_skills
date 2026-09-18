#!/usr/bin/env python3
"""Export a development catalog to a new, isolated production release directory.

This copies built assets only. Review databases, uploads, and browser edits stay
in the production state directory and are overlaid by deploy.py at request time.
"""
from __future__ import annotations

import argparse
import hashlib
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import tempfile

if __package__:
    from .workspace import REPO_ROOT as REPO, DEFAULT_DIST as DEFAULT_SOURCE, output_lock
else:
    from workspace import REPO_ROOT as REPO, DEFAULT_DIST as DEFAULT_SOURCE, output_lock


def export_release(source: Path, destination: Path) -> Path:
    with output_lock(source):
        return _export_release(source, destination)


def _export_release(source: Path, destination: Path) -> Path:
    source, destination = source.resolve(), destination.resolve()
    if destination.is_relative_to(REPO) or destination.is_relative_to(source):
        raise ValueError('Release destination must be outside the source checkout and build folder.')
    if destination.exists():
        raise ValueError('Use a new release directory; existing releases are never overwritten.')
    for filename in ('gallery/index.html', 'gallery/icons.json'):
        if not (source / filename).is_file():
            raise ValueError('Build the development gallery before exporting a release.')
    # Manual selections belong to server state, not the portable baseline.
    for path in source.rglob('manifest.json'):
        document = json.loads(path.read_text())
        if any(row.get('artwork_source', 'use_org') != 'use_org' for row in document.get('icons', [])):
            raise ValueError('Release contains manual artwork. Build Python originals into a fresh directory first.')
    if any(path.is_symlink() for path in source.rglob('*')):
        raise ValueError('Release inputs must not contain symlinks.')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.release-', dir=destination.parent) as temporary:
        staged = Path(temporary) / 'assets'
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns('.icon-build-*', '.DS_Store'))
        catalog = staged / 'gallery/icons.json'
        data = json.loads(catalog.read_text())
        (staged / 'release.json').write_text(json.dumps({
            'schema_version': 1,
            'created_at': datetime.now(timezone.utc).isoformat(),
            'catalog_sha256': hashlib.sha256(catalog.read_bytes()).hexdigest(),
            'icons': len(data.get('icons', [])),
            'failed_icons': len(data.get('failed_icons', [])),
            'artwork': 'python-originals',
        }, indent=2) + '\n')
        # Exclusive reservation protects an existing release, including a competing exporter.
        destination.mkdir()
        try:
            staged.replace(destination)
        except BaseException:
            destination.rmdir()
            raise
    return destination


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path, help='New release directory outside the checkout')
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    args = parser.parse_args(argv)
    try:
        result = export_release(args.source, args.destination)
    except (OSError, ValueError) as error:
        parser.exit(1, f'error: {error}\n')
    print(f'Release: {result}\nServe with deploy.py --production --dist {result} --database /persistent/state/feedback.sqlite3')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
