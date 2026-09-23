"""Stage side-components.json: every main and sub icon that side pairs need, with drawing status.

A component is one canonical source reference. Its drawings are found by source UUID across
published *and* failed records, so a sub that was drawn but fails validation shows as failing
rather than missing. Text / number marks are live (/api/primitives/status), not staged here.
"""
from __future__ import annotations
import json
import re
from datetime import datetime, timezone
from pathlib import Path

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist


ROOT = Path(__file__).resolve().parents[2]
DASHED = re.compile(r'([a-z0-9]{8}(?:-[a-z0-9]{4}){3}-[a-z0-9]{12})$', re.I)
UNDERSCORED = re.compile(r'([a-z0-9]{8}(?:_[a-z0-9]{4}){3}_[a-z0-9]{12})$', re.I)
MAIN_FAMILIES = ('solo', 'combination_main')
SUB_FAMILIES = ('sub',)
STATUS_ORDER = {'missing': 0, 'failing': 1, 'done': 2}


def _source_ids(record: dict) -> set[str]:
    ids = set()
    path = (record.get('python_source') or {}).get('path') or ''
    if match := UNDERSCORED.search(Path(path).stem):
        ids.add(match[1].replace('_', '-').lower())
    for source in record.get('original_sources') or []:
        if match := DASHED.search(Path(source.get('source_path') or '').stem):
            ids.add(match[1].lower())
    return ids


def _drawing(record: dict, failed: bool) -> dict:
    validation = record.get('validation') or {}
    if failed or validation.get('status') == 'fail' or record.get('model_validation') == 'fail':
        status = 'fail'
    elif validation.get('status') == 'valid' or record.get('model_validation') == 'pass':
        status = 'pass'
    else:
        status = 'review'
    errors = record.get('errors') or validation.get('errors') or []
    if not errors and status != 'pass' and validation.get('provenance'):
        errors = [validation['provenance']]
    return {'icon_id': record['icon_id'], 'key': record.get('key') or f"{record['family']}/{record['icon_id']}",
            'family': record['family'], 'status': status, 'preview_url': record.get('preview_url'),
            'python_source': (record.get('python_source') or {}).get('path'), 'svg_sha256': record.get('svg_sha256'),
            'errors': errors[:4]}


def _originals(root: Path) -> dict[str, str]:
    found = {}
    for folder in ('pictographic-combinations', 'pictographic-primitives'):
        for path in sorted((root / folder).rglob('*.svg')):
            if match := DASHED.search(path.stem):
                found.setdefault(match[1].lower(), str(path.relative_to(root)))
    return found


def build(combinations: dict, records: list[dict], failed_records: list[dict], root: Path = ROOT) -> dict:
    refs = combinations['references']
    by_source: dict[str, dict[str, dict]] = {}
    by_key: dict[str, dict] = {}
    for failed, group in ((False, records), (True, failed_records)):
        for record in group:
            drawing = _drawing(record, failed)
            # A published record wins over a failed copy of the same key.
            if drawing['key'] in by_key and failed:
                continue
            by_key[drawing['key']] = drawing
            for uuid in _source_ids(record):
                by_source.setdefault(uuid, {})[drawing['key']] = drawing

    items: dict[tuple[str, str], dict] = {}
    for row in combinations['rows']:
        if row.get('kind') != 'side':
            continue
        for role in ('main', 'sub'):
            source = row[role + '_id']
            ref = refs.get(source) or {}
            cid = ref.get('canonical_id') or source
            item = items.setdefault((role, cid), {
                'id': cid, 'role': role, 'concept': (refs.get(cid) or ref).get('concept') or cid,
                'reference_url': (refs.get(cid) or ref).get('reference_url'),
                'source_ids': set(), 'pairs': [], 'keys': set()})
            item['source_ids'].add(source)
            item['pairs'].append({'id': row['id'], 'concept': row['concept']})
            item['keys'].update(g['key'] for g in ref.get('generated') or [] if g.get('key'))
            if role == 'sub':
                item['keys'].update(g['key'] for g in row.get('sub_generated') or [] if g.get('key'))

    originals = _originals(root)
    out = {'main': [], 'sub': []}
    for (role, _), item in items.items():
        drawings = {}
        for uuid in item['source_ids'] | {item['id']}:
            drawings.update(by_source.get(uuid.lower(), {}))
        drawings.update({k: by_key[k] for k in item['keys'] if k in by_key})
        families = MAIN_FAMILIES if role == 'main' else SUB_FAMILIES
        own = sorted((d for d in drawings.values() if d['family'] in families),
                     key=lambda d: ({'pass': 0, 'review': 1, 'fail': 2}[d['status']], d['icon_id']))
        status = 'done' if any(d['status'] == 'pass' for d in own) else 'failing' if own else 'missing'
        entry = {'id': item['id'], 'concept': item['concept'], 'reference_url': item['reference_url'],
                 'source_path': originals.get(item['id'].lower()) or next(
                     (originals[s.lower()] for s in item['source_ids'] if s.lower() in originals), None),
                 'source_ids': sorted(item['source_ids']), 'uses': len(item['pairs']),
                 'pairs': item['pairs'][:6], 'status': status, 'drawings': own,
                 'failing_variants': sum(d['status'] != 'pass' for d in own)}
        if role == 'sub':
            # Passing drawings of the same source in other families, as a starting point for /icon-sub.
            entry['other_drawings'] = sorted({d['family'] for d in drawings.values()
                                              if d['family'] not in families and d['status'] == 'pass'})
        out[role].append(entry)
    for rows in out.values():
        rows.sort(key=lambda r: (STATUS_ORDER[r['status']], -r['uses'], r['concept'].lower()))
    counts = {role: {s: sum(r['status'] == s for r in rows) for s in STATUS_ORDER}
              | {'total': len(rows), 'done_with_failing_variants': sum(r['status'] == 'done' and r['failing_variants'] > 0 for r in rows),
                 'blocked_pairs': sum(r['uses'] for r in rows if r['status'] != 'done')}
              for role, rows in out.items()}
    return {'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'mains': out['main'], 'subs': out['sub'], 'counts': counts}


def write(target: Path, combinations: dict, records: list[dict], failed_records: list[dict], root: Path = ROOT) -> dict:
    result = build(combinations, records, failed_records, root)
    (target / 'side-components.json').write_text(json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n')
    return result


def refresh(gallery: Path) -> dict:
    """Rebuild side-components.json from an existing gallery, e.g. after a discard."""
    icons = json.loads((gallery / 'icons.json').read_text())
    return write(gallery, json.loads((gallery / 'combinations.json').read_text()), icons['icons'], icons['failed_icons'])


if __name__ == '__main__':
    import sys
    gallery = Path(sys.argv[1]) if len(sys.argv) > 1 else build_dist(ROOT) / 'gallery'
    result = refresh(gallery)
    print(f"Staged side components in {gallery}: {json.dumps(result['counts'])}")
