"""Hand-adjusted side-pair layouts, saved per pair in data/combination-layouts.json.

An entry pins the exact main and sub drawings it was made for:

    {"<pair id>": {"main": {"icon", "sha256"}, "sub": {"icon", "sha256"},
                   "layout": {"main": [...], "sub": [...]}, "updated_at", "user"}}

When either drawing changes (another sha256, or it left the pair), the entry is stale and
the pair falls back to its automatic placement until someone adjusts it again.
"""
import json
import os
import tempfile
import threading
from datetime import datetime, timezone
from .combination_experiment import ROOT

FILE = ROOT / 'data/combination-layouts.json'
_lock = threading.Lock()


def load():
    try:
        return json.loads(FILE.read_text())
    except FileNotFoundError:
        return {}


def _write(data):
    with tempfile.NamedTemporaryFile('w', dir=FILE.parent, prefix='.combination-layouts-', delete=False) as handle:
        json.dump(data, handle, indent=1, sort_keys=True)
        handle.write('\n')
    os.replace(handle.name, FILE)


def _pick(items, pin):
    return next((i for i in items if i['icon'] == pin.get('icon') and i.get('sha256') == pin.get('sha256')), None)


def active(row, entry):
    """Render arguments for a saved layout that still matches the pair's drawings, else None."""
    if not entry or not _pick(row['mains'], entry.get('main', {})) or not _pick(row['subs'], entry.get('sub', {})):
        return None
    return {'main': entry['main']['icon'], 'sub': entry['sub']['icon'], 'layout': entry['layout']}


def save(row, main, sub, layout, user=''):
    """Pin `layout` to the pair's current `main` and `sub` drawings (icon names)."""
    pins = {}
    for role, group, icon in (('main', 'mains', main), ('sub', 'subs', sub)):
        item = next((i for i in row[group] if i['icon'] == icon), None)
        if item is None:
            raise ValueError(f'The {role} does not belong to this pair.')
        pins[role] = {'icon': icon, 'sha256': item.get('sha256', '')}
    with _lock:
        data = load()
        data[row['id']] = {**pins, 'layout': layout, 'user': user,
                           'updated_at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
        _write(data)
    return data[row['id']]


def clear(pair_id):
    with _lock:
        data = load()
        if data.pop(pair_id, None) is not None:
            _write(data)
