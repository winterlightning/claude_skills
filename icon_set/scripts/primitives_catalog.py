#!/usr/bin/env python3
"""Catalog every Pictographic primitive and whether it has been remade.

python3 icon_set/scripts/primitives_catalog.py                  # refresh dist/gallery/primitives.json
python3 icon_set/scripts/primitives_catalog.py --primitives DIR

One row per primitive UUID from the original 1024 artwork. Categories are the
top-level folders; the ``_uncategorized_NN`` folders form one ``Uncategorized``
category whose batch is ``NN``. A primitive links to icon models with the same
identity rules as category_report.match_models (source ID, declared source
reuse, source path, then manifest name for models with no identity at all), and
its model state is:

* ``generated``    a linked icon is published in dist
* ``build_failed`` linked icons exist but only in dist/failed
* ``model_only``   linked models exist but were not built
* ``work_only``    no linked model, but a folder-only skill run (icon_set/work/
                   primitive-make-ray, side-main-make-thuan, side-sub-make-thuan)
                   holds a drawing for the uuid; ``work`` records the newest run
* ``none``         no linked model and no work run

TODO/SKIP decisions are not stored here; they live in the gallery database
(primitive_status.py) and are merged by the page, the API and the CLI.

Primitives that are the same drawing (data/primitive-aliases.json, written by
primitive_duplicates.py) fold into one row: the canonical keeps its identity and
lists the others under ``aliases``; models linked to any uuid in the set count.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime, timezone
from urllib.parse import quote

if __package__:
    from .workspace import DEFAULT_DIST
else:
    from workspace import DEFAULT_DIST

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.category_report import UUID, declared_references, source_id  # noqa: E402


ROOT_ENV = 'PICTOGRAPHIC_PRIMITIVES'
UNCATEGORIZED = 'Uncategorized'
ALIASES_PATH = REPO_ROOT / 'icon_set' / 'data' / 'primitive-aliases.json'
WORK_ROOT = REPO_ROOT / 'icon_set' / 'work'
WORK_SKILLS = ('primitive-make-ray', 'side-main-make-thuan', 'side-sub-make-thuan')
_VIEWBOX = re.compile(r'viewBox="([^"]+)"')


def primitives_root(explicit: str | Path | None = None) -> Path:
    """--primitives, then $PICTOGRAPHIC_PRIMITIVES, then the repository's pictographic-primitives
    folder, which holds the original 1024 artwork."""
    value = explicit or os.environ.get(ROOT_ENV)
    if value:
        return Path(value).expanduser().resolve()
    return (REPO_ROOT / 'pictographic-primitives').resolve()


def load_aliases(path: Path | None = None) -> dict[str, str]:
    """alias uuid -> canonical uuid from primitive_duplicates.py; no file means no aliases."""
    path = path or ALIASES_PATH
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except ValueError:
        return {}
    return {str(alias).lower(): str(canonical).lower() for alias, canonical in (data.get('aliases') or {}).items()}


def resolve(uid: str | None, aliases: dict[str, str]) -> str | None:
    """The canonical uuid a primitive id stands for (itself when it is not an alias)."""
    if not uid:
        return uid
    uid = uid.lower()
    return aliases.get(uid, uid)


def fold_aliases(rows: list[dict], aliases: dict[str, str]) -> list[dict]:
    """Attach alias rows to their canonical row as ``aliases``; the canonical keeps its own identity."""
    if not aliases:
        return rows
    by_uuid = {row['uuid']: row for row in rows if row['uuid']}
    folded = []
    for row in rows:
        canonical = by_uuid.get(aliases.get(row['uuid'] or ''))
        if canonical is None or canonical is row:
            folded.append(row)
            continue
        canonical.setdefault('aliases', []).append({key: row[key] for key in ('uuid', 'path', 'concept', 'old_concept', 'category', 'batch')})
        canonical['copies'] = canonical.get('copies', 1) + row.get('copies', 1)
    return folded


def _relative_primitive_path(path: str | Path | None) -> str | None:
    """A model's declared source path relative to its primitives folder, whichever copy it names."""
    if not path:
        return None
    parts = Path(path).parts
    if 'pictographic-primitives' not in parts:
        return None
    index = len(parts) - 1 - parts[::-1].index('pictographic-primitives')
    return Path(*parts[index + 1:]).as_posix() if index + 1 < len(parts) else None


def categorize(relative: Path) -> tuple[str, str]:
    top = relative.parts[0]
    if top.startswith('_uncategorized'):
        batch = top.rsplit('_', 1)[-1]
        return UNCATEGORIZED, batch if batch.isdigit() else ''
    batch = next((part for part in relative.parts[1:-1] if part.startswith('batch-')), '')
    return top, batch


def _metadata(root: Path) -> dict:
    """Concept names: folder manifest.json entries override _manifest.csv only where they add fields."""
    info = collections.defaultdict(dict)
    manifest = root / '_manifest.csv'
    if manifest.is_file():
        with manifest.open(encoding='utf-8', errors='replace', newline='') as handle:
            for row in csv.DictReader(handle):
                uid = (row.get('id') or '').strip().lower()
                if uid:
                    info[uid].update(concept=row.get('concept') or '', old_concept=row.get('old_concept') or '')
    for path in root.rglob('manifest.json'):
        try:
            contents = json.loads(path.read_text(encoding='utf-8'))
        except ValueError:
            continue
        for item in contents if isinstance(contents, list) else contents.get('icons', []):
            if not isinstance(item, dict):
                continue
            uid = source_id(Path(item.get('file', '')))
            if not uid:
                continue
            if item.get('concept') and not info[uid].get('concept'):
                info[uid]['concept'] = item['concept']
            if item.get('icon_id'):
                info[uid]['proposed_icon_id'] = item['icon_id']
    return info


def scan(root: Path) -> list[dict]:
    if not root.is_dir():
        raise FileNotFoundError(f'Primitives folder not found: {root} (pass --primitives or set {ROOT_ENV})')
    metadata = _metadata(root)
    rows = {}
    for path in sorted(root.rglob('*.svg')):
        relative = path.relative_to(root)
        if any(part.startswith('.') for part in relative.parts):
            continue
        uid = source_id(path)
        identity = uid or relative.as_posix()
        if identity in rows:  # the same primitive copied into another batch folder
            rows[identity]['copies'] += 1
            continue
        category, batch = categorize(relative)
        info = metadata.get(uid, {}) if uid else {}
        title = UUID.sub('', path.stem).strip(' _-').replace('_', ' ')
        rows[identity] = dict(uuid=uid, category=category, batch=batch, path=relative.as_posix(),
                              concept=info.get('concept') or title.title(),
                              old_concept=info.get('old_concept') or title,
                              proposed_icon_id=info.get('proposed_icon_id'), copies=1)
    return sorted(rows.values(), key=lambda r: (r['category'].lower(), r['batch'], r['concept'].lower(), r['path']))


def conversion_warning(root: Path, rows: list[dict], sample: int = 40) -> str | None:
    boxes = collections.Counter()
    for row in rows[:: max(1, len(rows) // sample)][:sample]:
        head = (root / row['path']).read_text(encoding='utf-8', errors='replace')[:800]
        match = _VIEWBOX.search(head)
        boxes[match[1].split()[-1] if match else None] += 1
    if boxes and boxes.most_common(1)[0][0] in ('48', '48.0'):
        return (f'{root} looks like 48u conversions, not the original artwork; '
                f'restore the original 1024 artwork or point --primitives at it')
    return None


def model_links() -> dict:
    """Indexes over icon models, applying match_models' precedence without its O(n*m) scan."""
    from icon_set.model.icons.registry import factories
    by_id = collections.defaultdict(list)
    by_reference_id = collections.defaultdict(list)
    by_path = collections.defaultdict(list)
    by_reference_path = collections.defaultdict(list)
    anonymous = {}
    for icon_id, factory in factories().items():
        module = sys.modules[factory.__module__]
        uid = (getattr(module, 'SOURCE_ICON_ID', None) or '').lower() or None
        path = _relative_primitive_path(getattr(module, 'SOURCE_PATH', None))
        references = declared_references(module)
        if uid:
            by_id[uid].append(icon_id)
        if path:
            by_path[path].append((icon_id, uid))
        for ref_id, ref_path in references:
            ref_id = (ref_id or '').lower() or None
            if ref_id:
                by_reference_id[ref_id].append(icon_id)
            relative = _relative_primitive_path(ref_path)
            if relative:
                by_reference_path[relative].append((icon_id, ref_id))
        if not uid and not getattr(module, 'SOURCE_PATH', None) and not references:
            anonymous[icon_id] = factory.family
    families = {icon_id: factory.family for icon_id, factory in factories().items()}
    return dict(by_id=by_id, by_reference_id=by_reference_id, by_path=by_path,
                by_reference_path=by_reference_path, anonymous=anonymous, families=families)


def work_runs(work_root: Path = WORK_ROOT) -> dict[str, dict]:
    """uuid -> newest folder-only skill run: {skill, runs, run, status}.

    Folder-only skills save ``<skill>/<source-uuid>/<run>/result.json`` and never
    register a model, so without this the source would still count as TODO.
    The newest run (by result.json time) supplies ``status`` (its validation_status).
    """
    result = {}
    for skill in WORK_SKILLS:
        skill_dir = work_root / skill
        if not skill_dir.is_dir():
            continue
        for source_dir in skill_dir.iterdir():
            match = UUID.search(source_dir.name) if source_dir.is_dir() else None
            if not match:
                continue
            uid = match.group(0).lower()
            runs = []
            for run in source_dir.iterdir():
                result_path = run / 'result.json'
                if not run.is_dir() or not result_path.is_file():
                    continue
                try:
                    status = str(json.loads(result_path.read_text(encoding='utf-8')).get('validation_status') or 'unknown')
                except (OSError, ValueError):
                    status = 'unknown'
                runs.append((result_path.stat().st_mtime, run.name, status))
            if not runs:
                continue
            runs.sort()
            entry = {'skill': skill, 'runs': len(runs), 'run': f'{skill}/{source_dir.name}/{runs[-1][1]}', 'status': runs[-1][2]}
            previous = result.get(uid)
            if not previous or runs[-1][0] > previous['_time']:
                result[uid] = {**entry, '_time': runs[-1][0]}
    return {uid: {k: v for k, v in entry.items() if k != '_time'} for uid, entry in result.items()}


def row_uuids(row: dict) -> list[str]:
    """The canonical uuid followed by every alias folded into the row."""
    return [uid for uid in [row.get('uuid')] + [alias['uuid'] for alias in row.get('aliases', [])] if uid]


def link(row: dict, links: dict) -> tuple[list[str], str]:
    uids = row_uuids(row)
    for key, method in (('by_id', 'source ID'), ('by_reference_id', 'declared source reuse')):
        matches = [icon for uid in uids for icon in links[key].get(uid, ())]
        if matches:
            return sorted(set(matches)), method
    uid = row['uuid']
    compatible = lambda other: not uid or not other or other in uids  # noqa: E731
    paths = [row['path']] + [alias['path'] for alias in row.get('aliases', [])]
    matches = [icon for path in paths for icon, other in links['by_path'].get(path, ()) if compatible(other)]
    if matches:
        return sorted(set(matches)), 'source path'
    matches = [icon for path in paths for icon, other in links['by_reference_path'].get(path, ()) if compatible(other)]
    if matches:
        return sorted(set(matches)), 'declared source reuse'
    proposed = row.get('proposed_icon_id')
    if proposed and proposed in links['anonymous']:
        return [proposed], 'manifest name'
    return [], 'unmatched'


def build_catalog(root: Path, built: dict, failed: dict, links: dict | None = None,
                  aliases: dict[str, str] | None = None, work: dict[str, dict] | None = None) -> dict:
    """built/failed map icon_id -> gallery record (needs key and preview_url).

    Primitives listed as aliases in data/primitive-aliases.json fold into their canonical row.
    ``work`` maps uuid -> newest folder-only skill run (work_runs()); it only matters for rows
    with no linked model, which become ``work_only`` instead of ``none``.
    """
    aliases = load_aliases() if aliases is None else aliases
    rows = fold_aliases(scan(root), aliases)
    warning = conversion_warning(root, rows)
    links = links or model_links()
    work = work_runs() if work is None else work
    text_by_source = collections.defaultdict(list)
    for icon_id, record in built.items():
        if record.get('family') == 'text':
            for uid in record.get('source_ids', []):
                text_by_source[uid].append(icon_id)
    categories = collections.OrderedDict()
    for row in rows:
        models, method = link(row, links)
        text_models = [icon for uid in row_uuids(row) for icon in text_by_source.get(uid, ())]
        if text_models:
            models = sorted(set(models + text_models))
            method = 'source ID'
        generated = [dict(icon_id=icon_id, key=built[icon_id]['key'], preview_url=built[icon_id]['preview_url'])
                     for icon_id in models if icon_id in built]
        state = ('generated' if generated else 'build_failed' if any(m in failed for m in models)
                 else 'model_only' if models else 'none')
        row.update(models=models, match=method, generated=generated, state=state)
        work_run = next((work[uid] for uid in row_uuids(row) if uid in work), None)
        if state == 'none' and work_run:
            state = 'work_only'
            row.update(state=state, work=work_run)
        else:
            row.pop('work', None)
        row.pop('proposed_icon_id', None)
        if row['copies'] == 1:
            del row['copies']
        summary = categories.setdefault(row['category'], collections.Counter())
        summary['total'] += 1
        summary[state] += 1
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'root_label': root.name,
        'warning': warning,
        'count': len(rows),
        'categories': {name: dict(counts) for name, counts in categories.items()},
        'rows': rows,
    }


def gallery_records(icons_json: Path) -> tuple[dict, dict]:
    data = json.loads(icons_json.read_text(encoding='utf-8'))
    built = {row['icon_id']: row for row in data.get('icons', [])}
    failed = {row['icon_id']: row for row in data.get('failed_icons', [])}
    return built, failed


def write_catalog(target: Path, built: dict, failed: dict, root: Path | None = None) -> dict:
    """Write primitives.json; a missing primitives folder yields an explanatory empty catalog, never a failed build."""
    root = root or primitives_root()
    try:
        catalog = build_catalog(root, built, failed)
    except FileNotFoundError as error:
        catalog = {'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                   'root_label': str(root.name), 'warning': str(error), 'count': 0, 'categories': {}, 'rows': []}
    target.write_text(json.dumps(catalog, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    return catalog


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--primitives', type=Path, help=f'Original primitives folder (default ${ROOT_ENV} or '
                                                        'claude_skills/pictographic-primitives)')
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    args = parser.parse_args(argv)
    icons_json = args.dist / 'gallery' / 'icons.json'
    if not icons_json.is_file():
        parser.exit(1, f'error: {icons_json} is missing; run icon_set/scripts/build.py first\n')
    built, failed = gallery_records(icons_json)
    root = primitives_root(args.primitives)
    if not root.is_dir():
        parser.exit(1, f'error: primitives folder not found: {root}\n')
    catalog = write_catalog(args.dist / 'gallery' / 'primitives.json', built, failed, root)
    totals = collections.Counter()
    for counts in catalog['categories'].values():
        totals.update(counts)
    print(f"{catalog['count']} primitives in {len(catalog['categories'])} categories from {root}")
    print('  ' + ' '.join(f'{state}={totals[state]}' for state in ('generated', 'build_failed', 'model_only', 'work_only', 'none')))
    if catalog['warning']:
        print('warning: ' + catalog['warning'], file=sys.stderr)
    print(f"-> {args.dist / 'gallery' / 'primitives.json'}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
