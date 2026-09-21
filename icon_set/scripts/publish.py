"""Build Python originals locally and refresh the committed published/ catalog.

Production only pulls this directory; its database and manual artwork remain
outside the checkout. Build failures are listed in the review gallery.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

from .workspace import PUBLICATION_BUILD, PUBLISHED_DIST, output_lock


def publish_assets(source: Path, destination: Path = PUBLISHED_DIST) -> dict:
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if source == destination or source.is_relative_to(destination) or destination.is_relative_to(source):
        raise ValueError('Publication and temporary build folders must be separate.')
    with output_lock(source), output_lock(destination):
        catalog = source / 'gallery/icons.json'
        if not catalog.is_file() or not (source / 'gallery/index.html').is_file():
            raise ValueError('Build a complete gallery before publishing.')
        data = json.loads(catalog.read_text())
        if not data.get('icons'):
            raise ValueError('Refusing to publish an empty catalog.')
        # The portable catalog must never embed a developer\'s selected uploads
        # or edits. The production server applies its own state at request time.
        for path in [catalog, *source.glob('*/manifest.json'), *source.glob('failed/*/manifest.json')]:
            document = json.loads(path.read_text())
            rows = document.get('icons', []) + document.get('failed_icons', [])
            if any(r.get('artwork_source', 'use_org') != 'use_org' or r.get('uploaded_icon') for r in rows):
                raise ValueError(f'Manual artwork found in {path}; rebuild Python originals first.')

        from icon_set.model import contracts
        from .build import family_dist_name, _publish
        folders = {'gallery', 'failed', 'compositions'}
        folders.update(family_dist_name(family) for family in contracts.families())
        folders.update(p.name for p in source.glob('text[0-9]*') if p.is_dir())
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.publish-', dir=destination.parent) as temporary:
            staged = Path(temporary) / 'assets'
            staged.mkdir()
            for folder in sorted(folders):
                root = source / folder
                if not root.exists():
                    continue
                if root.is_symlink():
                    raise ValueError(f'Publication inputs cannot contain symlinks: {folder}')
                for path in sorted(root.rglob('*')):
                    relative = path.relative_to(source)
                    if path.is_symlink():
                        raise ValueError(f'Publication inputs cannot contain symlinks: {relative}')
                    if any(part.startswith('.') or part == '__pycache__' for part in relative.parts):
                        continue
                    if path.is_dir():
                        continue
                    if path.suffix.lower() in {'.sqlite3', '.sqlite', '.db', '.log', '.pid', '.pyc'}:
                        raise ValueError(f'Runtime state cannot be published: {relative}')
                    target = staged / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if path.suffix == '.json':
                        # Keep the aggregate catalogs below GitHub\'s file limit.
                        target.write_text(json.dumps(json.loads(path.read_text()), ensure_ascii=False,
                                                     separators=(',', ':')) + '\n')
                    else:
                        shutil.copyfile(path, target)
                    if target.stat().st_size >= 100 * 1024 * 1024:
                        raise ValueError(f'Asset exceeds GitHub\'s file limit: {relative}')
            marker = {
                'schema_version': 1, 'artwork': 'python-originals',
                'publication': 'git', 'icons': len(data['icons']),
                'release_icons': sum(r.get('release_eligible', True) for r in data['icons']),
                'managed_drafts': sum(not r.get('release_eligible', True) for r in data['icons']),
                'failed_icons': len(data.get('failed_icons', [])),
                'catalog_sha256': hashlib.sha256((staged / 'gallery/icons.json').read_bytes()).hexdigest(),
            }
            (staged / 'release.json').write_text(json.dumps(marker, indent=2) + '\n')
            _publish([(staged, destination)])
    return marker


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=PUBLICATION_BUILD)
    parser.add_argument('--no-build', action='store_true', help='Publish an already completed Python-only build')
    args = parser.parse_args(argv)
    try:
        if not args.no_build:
            from .build import build
            build(args.source, None, write_png=False, report=False, changed_only=True,
                  allow_validation_failures=True)
        marker = publish_assets(args.source)
    except (OSError, ValueError) as error:
        parser.exit(1, f'error: {error}\n')
    print(f"Published catalog: {marker['release_icons']} release icons, "
          f"{marker['managed_drafts']} review drafts, {marker['failed_icons']} other failed entries.\n"
          f"Assets: {PUBLISHED_DIST}\nCommit published/ with the source changes, then push.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
