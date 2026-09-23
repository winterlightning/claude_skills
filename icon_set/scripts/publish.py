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
from typing import Callable, Mapping

from .workspace import PUBLISHED_DIST, compact_json_tree, output_lock

# Regenerated per-icon QA evidence stays out of Git; everything else in the build root is committed.
UNCOMMITTED_OUTPUT = {'qa', 'build-progress.json'}
RUNTIME_SUFFIXES = {'.sqlite3', '.sqlite', '.db', '.log', '.pid', '.pyc'}
GIT_FILE_LIMIT = 100 * 1024 * 1024


def _manifest_rows(path: Path) -> dict[str, dict]:
    try:
        document = json.loads(path.read_text(encoding='utf-8'))
        return {row['icon_id']: row for row in document.get('icons', [])}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def _matches(path: Path, digest: str) -> bool:
    try:
        return path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest
    except OSError:
        return False


def publication_plan(
    dist: Path = PUBLISHED_DIST,
    *,
    registered: Mapping[str, type] | None = None,
    folder_for_family: Callable[[str], str] | None = None,
    require_png: bool = True,
) -> dict[str, list[dict]]:
    """Compare registered drawings with the current publication by SVG content.

    ``new`` has no passing or failed manifest record, ``changed`` draws a new
    SVG, and ``missing`` has a current manifest record but lacks one of the
    generated files. The build already uses the same content-based policy;
    this scan makes its decisions visible before publication starts.
    """
    dist = Path(dist).resolve()
    if registered is None:
        from icon_set.model.icons.registry import factories
        registered = factories()
    if folder_for_family is None:
        from .build import family_dist_name
        folder_for_family = family_dist_name

    families = sorted({factory.family for factory in registered.values()})
    passing = {}
    failed = {}
    for family in families:
        folder = folder_for_family(family)
        passing[family] = _manifest_rows(dist / folder / 'manifest.json')
        failed[family] = _manifest_rows(dist / 'failed' / folder / 'manifest.json')

    plan = {name: [] for name in ('new', 'changed', 'missing', 'unchanged', 'failed', 'errors')}
    for icon_id, factory in sorted(registered.items()):
        family = factory.family
        folder = folder_for_family(family)
        row = passing[family].get(icon_id) or failed[family].get(icon_id)
        try:
            document = factory().to_svg()
            digest = hashlib.sha256(document.encode('utf-8')).hexdigest()
        except Exception as error:  # the build will reject this source too
            plan['errors'].append({'icon_id': icon_id, 'family': family, 'reason': str(error)})
            continue
        item = {'icon_id': icon_id, 'family': family, 'svg_sha256': digest}
        if row is None:
            item['reason'] = 'no published or failed-build record'
            plan['new'].append(item)
            continue
        if row.get('svg_sha256') != digest:
            item['reason'] = 'drawing content changed'
            plan['changed'].append(item)
            continue

        absent = []
        if icon_id in passing[family]:
            svg = dist / folder / f'{icon_id}.svg'
            if not _matches(svg, digest):
                absent.append(svg.relative_to(dist).as_posix())
            metadata = dist / folder / f'{icon_id}.metadata.json'
            if not metadata.is_file():
                absent.append(metadata.relative_to(dist).as_posix())
            if require_png:
                png = dist / 'previews-png' / folder / f'{icon_id}.png'
                if not png.is_file():
                    absent.append(png.relative_to(dist).as_posix())
        elif row.get('svg'):
            svg = dist / 'failed' / folder / row['svg']
            if not _matches(svg, digest):
                absent.append(svg.relative_to(dist).as_posix())
        if absent:
            item['reason'] = 'missing or stale generated output'
            item['paths'] = absent
            plan['missing'].append(item)
        elif icon_id in failed[family]:
            item['reason'] = 'current drawing remains in the failed build'
            item['validation'] = row.get('errors') or row.get('warnings') or []
            plan['failed'].append(item)
        else:
            plan['unchanged'].append(item)
    return plan


def _print_plan(plan: dict[str, list[dict]], *, limit: int = 50) -> None:
    pending = sum(len(plan[name]) for name in ('new', 'changed', 'missing'))
    print('Publication scan: '
          f"{len(plan['new'])} new, {len(plan['changed'])} changed, "
          f"{len(plan['missing'])} missing/stale, {len(plan['unchanged'])} unchanged, "
          f"{len(plan['failed'])} validation-failed, {len(plan['errors'])} source errors.")
    rows = [(state, row) for state in ('new', 'changed', 'missing', 'errors', 'failed') for row in plan[state]]
    visible = rows if limit == 0 else rows[:limit]
    for state, row in visible:
        print(f"  {state:7} {row['family']}/{row['icon_id']} — {row['reason']}")
        for path in row.get('paths', []):
            print(f'           {path}')
        for finding in row.get('validation', [])[:2]:
            print(f'           {finding}')
    if len(visible) < len(rows):
        print(f'  … {len(rows) - len(visible)} more; use --list-limit 0 to show every item.')
    if not pending and not plan['errors']:
        print('  Icon outputs are current; the gallery and release metadata will still be refreshed.')


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
            if path.stat().st_size >= GIT_FILE_LIMIT:
                raise ValueError(f"Asset exceeds GitHub's file limit: {relative}")
        # Validation passed for the whole tree; builds already compact, this catches manual edits.
        compact_json_tree(dist)
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
    parser.add_argument('--dry-run', action='store_true',
                        help='detect new, changed, and missing icon outputs without writing anything')
    parser.add_argument('--list-limit', type=int, default=50, metavar='N',
                        help='maximum changed items to list; 0 lists all (default: 50)')
    args = parser.parse_args(argv)
    if args.list_limit < 0:
        parser.error('--list-limit must be zero or greater')
    if args.no_build and args.dry_run:
        parser.error('--no-build and --dry-run cannot be combined')
    try:
        if not args.no_build:
            plan = publication_plan(args.dist)
            _print_plan(plan, limit=args.list_limit)
            if plan['errors']:
                raise ValueError('Fix the source errors above before publishing; no files were changed.')
            if args.dry_run:
                return 0
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
