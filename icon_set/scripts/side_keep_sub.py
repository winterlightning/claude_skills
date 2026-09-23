"""Keep one sub for a side pair and list the alternative subs to remove from the set.

A combination needs a single sub. Alternatives are shared: every pair that lists an
alternative loses it, so the plan reports all affected pairs before anything is removed.
"""
import json
from pathlib import Path


def sub_key(item):
    return item.get('model_key') or item['family'] + '/' + item['icon']


def plan(rows, pair_id, keep):
    row = next((r for r in rows if r['id'] == pair_id), None)
    if row is None:
        raise ValueError('Unknown side pair.')
    keys = [sub_key(s) for s in row['subs']]
    if keep not in keys:
        raise ValueError('The kept sub does not belong to this pair.')
    remove = [k for k in keys if k != keep]
    if not remove:
        raise ValueError('This pair has only one sub.')
    usage = {k: [r['id'] for r in rows if any(sub_key(s) == k for s in r['subs'])] for k in remove}
    orphaned = [r['id'] for r in rows if r['subs'] and all(sub_key(s) in remove for s in r['subs'])]
    if orphaned:
        raise ValueError(f'Removing these subs would leave {len(orphaned)} side pair(s) without a sub.')
    affected = sorted({pid for ids in usage.values() for pid in ids})
    return {'pair_id': pair_id, 'keep': keep,
            'remove': [{'key': k, 'icon': k.split('/', 1)[1], 'pairs': len(ids)} for k, ids in usage.items()],
            'affected_pairs': affected}


def strip(rows, removed_keys):
    removed = set(removed_keys)
    for row in rows:
        row['subs'] = [s for s in row['subs'] if sub_key(s) not in removed]
    return rows


def strip_file(path: Path, removed_keys):
    """Drop removed subs from a pair file in place; a missing file is left alone."""
    path = Path(path)
    if not path.exists():
        return
    data = json.loads(path.read_text())
    strip(data['rows'], removed_keys)
    path.write_text(json.dumps(data))
