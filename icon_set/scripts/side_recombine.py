"""Recombine one released pair with the server's current artwork choices."""
import copy
import json
from . import combination_layouts
from .combination_experiment import custom_item, render


def recombine(gallery, data, document, user):
    rows = json.loads((gallery / 'experiment-combination.json').read_text())['rows']
    row = next((r for r in rows if r['id'] == data.get('pair_id')), None)
    if row is None:
        raise ValueError('Choose an available icon pair.')
    current = copy.deepcopy(row)
    chosen = {}
    for role, group in (('main', 'mains'), ('sub', 'subs')):
        name = data.get(role)
        item = next((i for i in current[group] if i['icon'] == name), None)
        if item is None:
            raise ValueError('The ' + role + ' does not belong to this pair.')
        chosen[role] = name
        svg = document(item)
        if svg != item['document']:
            measured = custom_item({'document': svg}, role)
            for field in ('engine_document', 'ink32', 'sizing_kind', 'sub32_status'):
                item.pop(field, None)
            item.update(measured, icon=name)
    result = render({'id': row['id'], **chosen}, row=current)
    # Pin to the published pair so the runtime overlay survives reloads. The SVG
    # is a snapshot of the latest edits; subsequent edits need another recombine.
    combination_layouts.save(row, chosen['main'], chosen['sub'], None, result, user)
    return {'result': result, 'url': None}
