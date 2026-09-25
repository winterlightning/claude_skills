"""Hand-adjusted side-pair layouts: runtime state of each server, never committed.

The file sits beside the server's review database (development: icon_set/state/; production:
its own state folder), so production keeps the layouts edited there and development keeps its
own. The server exports the path in PICTOGRAPHIC_COMBINATION_LAYOUTS, so the combine jobs it
starts read the same file. An entry pins the exact main and sub drawings it was made for and
keeps the combined result rendered from it:

    {"<pair id>": {"main": {"icon", "sha256"}, "sub": {"icon", "sha256"},
                   "layout": {"main": [...], "sub": [...]}, "result": {...}, "updated_at", "user"}}

When either drawing changes (another sha256, or it left the pair), the entry is stale and the
pair falls back to its automatic placement until someone adjusts it again.
"""
import json
import os
import tempfile
import threading
from datetime import datetime, timezone
from pathlib import Path
from .combination_experiment import ROOT

ENV = 'PICTOGRAPHIC_COMBINATION_LAYOUTS'
_lock = threading.Lock()


def path():
    return Path(os.environ.get(ENV) or ROOT / 'state/combination-layouts.json')


def load():
    try:
        return json.loads(path().read_text())
    except FileNotFoundError:
        return {}


def _write(data):
    file = path()
    file.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', dir=file.parent, prefix='.combination-layouts-', delete=False) as handle:
        json.dump(data, handle, sort_keys=True)
        handle.write('\n')
    os.replace(handle.name, file)


def _pick(items, pin):
    return next((i for i in items if i['icon'] == pin.get('icon') and i.get('sha256') == pin.get('sha256')), None)


def active(row, entry):
    """Render arguments for a saved layout that still matches the pair's drawings, else None."""
    if not entry or not _pick(row['mains'], entry.get('main', {})) or not _pick(row['subs'], entry.get('sub', {})):
        return None
    return {'main': entry['main']['icon'], 'sub': entry['sub']['icon'], 'layout': entry['layout']}


def save(row, main, sub, layout, result, user=''):
    """Pin `layout` (and the `result` rendered from it) to the pair's current `main` and `sub` drawings."""
    pins = {}
    for role, group, icon in (('main', 'mains', main), ('sub', 'subs', sub)):
        item = next((i for i in row[group] if i['icon'] == icon), None)
        if item is None:
            raise ValueError(f'The {role} does not belong to this pair.')
        pins[role] = {'icon': icon, 'sha256': item.get('sha256', '')}
    with _lock:
        data = load()
        data[row['id']] = {**pins, 'layout': layout, 'user': user,
                           'result': {k: v for k, v in result.items() if k != 'elements'},
                           'updated_at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
        _write(data)
    return data[row['id']]


def clear(pair_id):
    with _lock:
        data = load()
        if data.pop(pair_id, None) is not None:
            _write(data)
