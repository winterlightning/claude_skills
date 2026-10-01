"""Recombine one released pair with the server's current artwork choices."""
import copy
import hashlib
import json
from . import combination_layouts
from .combination_experiment import custom_item, render


# Measuring a drawing runs a subprocess (seconds on a small machine): each distinct drawing once per process.
_MEASURED = {}


def _measured(kind, svg, measure):
    key = (kind, sha256(svg))
    if key not in _MEASURED:
        if len(_MEASURED) > 2000:
            _MEASURED.clear()
        _MEASURED[key] = measure()
    return copy.deepcopy(_MEASURED[key])


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def published_drawings(item):
    """The catalog drawings a pair item was made from: its own sha, and for a sub combined as a
    normalized SUB32 copy (refresh_combination_pairs), the catalog drawing it was copied from."""
    return {s for s in (item.get('sha256'), item.get('source_sha256')) if s}


# Sizing modes that place a sub 1:1 at its authored canvas_width × canvas_height (combination_experiment.placement).
EXCEPTION_SIZES = ('side-source-fit', 'side-32x48', 'side-one-axis32')


def _normalized_sub(item, svg):
    """A changed sub measured the way refresh_combination_pairs measures one: its ink normalized to
    SUB32 (sub_ink32.normalize_ink32), on the 32 canvas widened only if the ink reaches its edge."""
    from .sub_ink32 import normalize_ink32
    text = item.get('sizing_kind') == 'text'
    document, ink = _measured(('ink32', text), svg, lambda: normalize_ink32(svg, text=text))
    bounds = ink['bounds']
    extent = max(bounds[2] - bounds[0], bounds[3] - bounds[1])
    item.pop('engine_document', None)
    # A redrawn sub is a plain SUB32 now: the old drawing's 1:1 exception size no longer applies.
    if item.get('sizing_mode') in EXCEPTION_SIZES:
        for key in ('sizing_mode', 'canvas_width', 'canvas_height'):
            item.pop(key, None)
    item.update(document=document, bounds=bounds, ink32=ink, canvas=max(32, extent * 32 / 28),
                sha256=sha256(document), source_sha256=sha256(svg))


def pair_with_documents(row, main, sub, documents):
    """The pair with its chosen main and sub measured from their current drawings.

    `documents` maps 'main' / 'sub' to the current catalog SVG; a role left out, or whose drawing is
    one the item was made from, combines as published. Returns (row copy, {'main': icon, 'sub': icon}).
    Shared by deploy.py, the cloud graphics service and cloud/migrate/recombine_side_pairs.py.
    """
    from .build_combination_previews import _inline_class_styles
    current, chosen = copy.deepcopy(row), {}
    for role, group, name in (('main', 'mains', main), ('sub', 'subs', sub)):
        name = name or current[group][0]['icon']
        item = next((i for i in current[group] if i['icon'] == name), None)
        if item is None:
            raise ValueError('The ' + role + ' does not belong to this pair.')
        svg = (documents or {}).get(role)
        if svg and svg != item.get('document') and sha256(svg) not in published_drawings(item) and not item.get('native_text'):
            if role == 'sub' and item.get('ink32') and item.get('family') != 'text':
                _normalized_sub(item, _inline_class_styles(svg))
            else:
                styled = _inline_class_styles(svg)
                measured = _measured(role, styled, lambda: custom_item({'document': styled}, role))
                for field in ('engine_document', 'ink32', 'sizing_kind', 'sub32_status'):
                    item.pop(field, None)
                item.update(measured, icon=name)
        chosen[role] = name
    return current, chosen


def recombine(gallery, data, document, user):
    rows = json.loads((gallery / 'experiment-combination.json').read_text())['rows']
    row = next((r for r in rows if r['id'] == data.get('pair_id')), None)
    if row is None:
        raise ValueError('Choose an available icon pair.')
    documents = {}
    for role, group in (('main', 'mains'), ('sub', 'subs')):
        item = next((i for i in row[group] if i['icon'] == data.get(role)), None)
        if item is None:
            raise ValueError('The ' + role + ' does not belong to this pair.')
        documents[role] = document(item)
    current, chosen = pair_with_documents(row, data['main'], data['sub'], documents)
    result = render({'id': row['id'], **chosen}, row=current)
    # Pin to the published pair so the runtime overlay survives reloads. The SVG
    # is a snapshot of the latest edits; subsequent edits need another recombine.
    combination_layouts.save(row, chosen['main'], chosen['sub'], None, result, user)
    return {'result': result, 'url': None}
