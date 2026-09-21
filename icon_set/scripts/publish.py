"""Build Python originals into published/ and finalize it as the committed catalog.

There is one build root, published/, and Git tracks it. Publishing builds the
changed originals in place, checks that no runtime state or manual artwork is
embedded, compacts the JSON catalogs for Git, and writes release.json. Production
pulls the branch and serves published/ with its own external database.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from .workspace import PUBLISHED_DIST, output_lock

# Regenerated per-icon QA evidence stays out of Git; everything else in the build root is committed.
UNCOMMITTED_OUTPUT = {'qa', 'build-progress.json'}
RUNTIME_SUFFIXES = {'.sqlite3', '.sqlite', '.db', '.log', '.pid', '.pyc'}
GIT_FILE_LIMIT = 100 * 1024 * 1024


def _is_hidden(relative: Path) -> bool:
    return any(part.startswith('.') or part == '__pycache__' for part in relative.parts)


def finalize_publication(dist: Path = PUBLISHED_DIST) -> dict:
    """Validate and compact a completed build in place, then mark it as the publication."""
    dist = Path(dist).resolve()
    with output_lock(dist):
        catalog = dist / 'gallery/icons.json'
        if not catalog.is_file() or not (dist / 'gallery/index.html').is_file():
            raise ValueError('Build a complete gallery before publishing.')
        data = json.loads(catalog.read_text())
        if not data.get('icons'):
            raise ValueError('Refusing to publish an empty catalog.')
        # The committed catalog must never embed a developer's selected uploads
        # or edits. The production server applies its own state at request time.
        for path in [catalog, *dist.glob('*/manifest.json'), *dist.glob('failed/*/manifest.json')]:
            document = json.loads(path.read_text())
            rows = document.get('icons', []) + document.get('failed_icons', [])
            if any(r.get('artwork_source', 'use_org') != 'use_org' or r.get('uploaded_icon') for r in rows):
                raise ValueError(f'Manual artwork found in {path}; rebuild Python originals first.')
        compacted = []
        for path in sorted(dist.rglob('*')):
            relative = path.relative_to(dist)
            if _is_hidden(relative) or relative.parts[0] in UNCOMMITTED_OUTPUT:
                continue
            if path.is_symlink():
                raise ValueError(f'Publication cannot contain symlinks: {relative}')
            if path.is_dir():
                continue
            if path.suffix.lower() in RUNTIME_SUFFIXES:
                raise ValueError(f'Runtime state cannot be published: {relative}')
            if path.suffix == '.json' and relative.name != 'release.json':
                compacted.append(path)
            if path.stat().st_size >= GIT_FILE_LIMIT:
                raise ValueError(f"Asset exceeds GitHub's file limit: {relative}")
        # Validation passed for the whole tree; now rewrite catalogs so Git diffs stay small.
        for path in compacted:
            text = path.read_text()
            compact = json.dumps(json.loads(text), ensure_ascii=False, separators=(',', ':')) + '\n'
            if compact != text:
                path.write_text(compact)
        marker = {
            'schema_version': 1, 'artwork': 'python-originals',
            'publication': 'git', 'icons': len(data['icons']),
            'release_icons': sum(r.get('release_eligible', True) for r in data['icons']),
            'managed_drafts': sum(not r.get('release_eligible', True) for r in data['icons']),
            'failed_icons': len(data.get('failed_icons', [])),
            'catalog_sha256': hashlib.sha256(catalog.read_bytes()).hexdigest(),
        }
        (dist / 'release.json').write_text(json.dumps(marker, indent=2) + '\n')
    return marker


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, default=PUBLISHED_DIST)
    parser.add_argument('--no-build', action='store_true', help='Finalize an already completed build')
    args = parser.parse_args(argv)
    try:
        if not args.no_build:
            from .build import build
            build(args.dist, args.dist / 'previews-png', write_png=True, report=False, changed_only=True,
                  allow_validation_failures=True)
        marker = finalize_publication(args.dist)
    except (OSError, ValueError) as error:
        parser.exit(1, f'error: {error}\n')
    print(f"Published catalog: {marker['release_icons']} release icons, "
          f"{marker['managed_drafts']} review drafts, {marker['failed_icons']} other failed entries.\n"
          f"Assets: {args.dist}\nCommit {args.dist.name}/ with the source changes, then push.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
