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


# ---- applying one pair's layout to another pair that uses the same main ----

def _union(groups):
    return (min(g['x'] for g in groups), min(g['y'] for g in groups),
            max(g['x'] + g['w'] for g in groups), max(g['y'] + g['h'] for g in groups))


def _corner(w, h, anchor, canvas, padding=2):
    """Top-left centerline corner of a w×h centerline box pushed into `anchor` (as placement() does)."""
    x = round(padding + (canvas - 2 * padding - w - 4) * anchor[0]) + 2
    y = round(padding + (canvas - 2 * padding - h - 4) * anchor[1]) + 2
    return x, y


def _map(groups, box, target):
    """Map groups from `box` onto `target` (x0, y0, x1, y1), rounding edges so touching groups stay touching."""
    x0, y0, x1, y1 = box
    t0, u0, t1, u1 = target
    fx = (t1 - t0) / (x1 - x0) if x1 - x0 > 1e-9 else 1
    fy = (u1 - u0) / (y1 - y0) if y1 - y0 > 1e-9 else 1
    out = []
    for g in groups:
        gx0, gy0 = round(t0 + (g['x'] - x0) * fx), round(u0 + (g['y'] - y0) * fy)
        gx1, gy1 = round(t0 + (g['x'] + g['w'] - x0) * fx), round(u0 + (g['y'] + g['h'] - y0) * fy)
        out.append({'paths': list(g['paths']), 'x': gx0, 'y': gy0,
                    'w': max(1, gx1 - gx0) if g['w'] > 0 else 0, 'h': max(1, gy1 - gy0) if g['h'] > 0 else 0})
    return out


def transfer(layout, source_position, source_sub, target_position, target_sub, target_canvas, target_sub_groups=None):
    """One pair's layout made to fit another pair with the same main.

    Same side: main (and the same sub) copy exactly. Another side: each role keeps its size and
    internal edits and moves into its own corner for that side (the main opposite the sub).
    A different sub cannot reuse path numbers: its own default groups (`target_sub_groups`, boxes
    [x0, y0, x1, y1]) are scaled evenly to fit the edited sub's box and pushed into the sub's corner.
    """
    from .combination_experiment import POSITIONS
    same_side = source_position == target_position
    ax, ay = POSITIONS[target_position]
    out = {}
    for role, anchor in (('main', (1 - ax, 1 - ay)), ('sub', (ax, ay))):
        groups = (layout or {}).get(role)
        if not groups:
            continue
        box = _union(groups)
        w, h = box[2] - box[0], box[3] - box[1]
        if role == 'sub' and target_sub != source_sub:
            if not target_sub_groups:
                continue
            own = [{'paths': g['paths'], 'x': g['box'][0], 'y': g['box'][1],
                    'w': g['box'][2] - g['box'][0], 'h': g['box'][3] - g['box'][1]} for g in target_sub_groups]
            tb = _union(own)
            tw, th = tb[2] - tb[0], tb[3] - tb[1]
            votes = [d / s for s, d in ((tw, w), (th, h)) if s > 1e-9]
            k = min(votes) if votes else 1
            fw, fh = round(tw * k), round(th * k)
            if same_side:
                x, y = round(box[0] + (w - fw) * ax), round(box[1] + (h - fh) * ay)
            else:
                x, y = _corner(fw, fh, anchor, target_canvas)
            out[role] = _map(own, tb, (x, y, x + fw, y + fh))
            continue
        if same_side:
            out[role] = [dict(g, paths=list(g['paths'])) for g in groups]
        else:
            x, y = _corner(w, h, anchor, target_canvas)
            out[role] = [dict(g, paths=list(g['paths']), x=g['x'] + x - box[0], y=g['y'] + y - box[1]) for g in groups]
    return out or None
