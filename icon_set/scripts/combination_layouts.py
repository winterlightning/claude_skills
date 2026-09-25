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


# ---- one combined icon per pair: the served files follow the saved layout ----
#
# A saved layout is the pair's combined icon everywhere, not a second icon beside it. The server
# answers every URL of a pair's combined icon (the side preview and, for native text pairs, the
# composition), and the two lists that point at them, with the saved result. Development also
# republishes the files (build_one); production serves them from its own state the same way.

_overlay_cache = {}


def overlay(gallery):
    """{pair_id: (version, result)} for saved layouts that still match the served pairs."""
    import hashlib
    rows_file = Path(gallery) / 'experiment-combination.json'
    try:
        key = (path().stat().st_mtime_ns, rows_file.stat().st_mtime_ns)
    except FileNotFoundError:
        return {}
    cached = _overlay_cache.get(str(gallery))
    if cached and cached[0] == key:
        return cached[1]
    layouts, active_results = load(), {}
    if layouts:
        rows = {r['id']: r for r in json.loads(rows_file.read_text())['rows']}
        for pair_id, entry in layouts.items():
            row = rows.get(pair_id)
            if row and entry.get('result', {}).get('svg') and active(row, entry):
                version = hashlib.sha256((json.dumps(entry['layout'], sort_keys=True) + entry.get('updated_at', '')).encode()).hexdigest()[:12]
                active_results[pair_id] = (version, entry['result'])
    _overlay_cache[str(gallery)] = (key, active_results)
    return active_results


def _merged(gallery, name, mutate):
    """A served list with the saved results merged in, cached until either file changes."""
    file = Path(gallery) / name
    adjusted = overlay(gallery)
    key = (file.stat().st_mtime_ns, _overlay_cache[str(gallery)][0])
    cached = _overlay_cache.get((str(gallery), name))
    if cached and cached[0] == key:
        return cached[1]
    data = json.loads(file.read_text())
    mutate(data, adjusted)
    body = json.dumps(data, ensure_ascii=False).encode()
    _overlay_cache[(str(gallery), name)] = (key, body)
    return body


def served(gallery, request_path):
    """(body, content type) of a combined icon or list that a saved layout overrides, else None."""
    gallery = Path(gallery)
    adjusted = overlay(gallery)
    if not adjusted:
        return None
    # The composition copy of a native text pair sits beside the gallery (/compositions/…).
    name = request_path.removeprefix('/gallery/').removeprefix('/')
    if name.startswith(('combination-previews/', 'compositions/side-text-v2-')) and name.endswith('.svg'):
        pair_id = Path(name).stem.removeprefix('side-text-v2-')
        if pair_id in adjusted:
            return adjusted[pair_id][1]['svg'].encode(), 'image/svg+xml'
        return None
    url = lambda pair_id: f'combination-previews/{pair_id}.svg?v={adjusted[pair_id][0]}'
    if name == 'experiment-combination-results.json':
        def mutate(data, adjusted):
            for pair_id, (_version, result) in adjusted.items():
                data['results'][pair_id] = {**data['results'].get(pair_id, {}), 'url': url(pair_id), 'result': result}
        return _merged(gallery, name, mutate), 'application/json'
    if name == 'preview-combination-icons.json':
        def mutate(data, adjusted):
            for icon in data.get('icons', []):
                if icon.get('icon_id') in adjusted:
                    icon['preview_url'] = url(icon['icon_id'])
        return _merged(gallery, name, mutate), 'application/json'
    return None
