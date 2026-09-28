"""Choose only currently approved drawings for a side combination run."""
import json
import sqlite3
from contextlib import closing

from .icon_artwork import baseline, icon_from_graph, resolve_artwork, sha
from .reviewer_stats import current_reviews


def drawing_key(item):
    return item.get('model_key') or f"{item['family']}/{item['icon']}"


def approved_pairs(rows, catalog, reviews):
    """One approved main and sub per pair, in the gallery's preferred order.

    A drawing that fails the build check counts once a reviewer approves it as an exception:
    the catalog then marks it human-selected and no longer build_failed."""
    selected = {}
    for row in rows:
        choices = {}
        for role, group in (('main', 'mains'), ('sub', 'subs')):
            for item in row[group]:
                key = drawing_key(item)
                record = catalog.get(key)
                if (record and reviews.get(key) == 'approve'
                        and not record.get('build_failed')
                        and record.get('artwork_source') != 'work_fix'
                        and (record.get('validation') or {}).get('status') in ('valid', 'human-selected')):
                    choices[role] = {'icon': item['icon'], 'key': key,
                                     'svg_sha256': record['svg_sha256']}
                    break
        if len(choices) == 2:
            selected[row['id']] = choices
    return selected


def plan(handler):
    rows = json.loads((handler.root / 'gallery/experiment-combination.json').read_text())['rows']
    catalog = handler.catalog(include_failed=True)
    if getattr(handler, 'cloud', None):
        reviews = handler.cloud.get('/api/reviews')  # deploy.py --cloud-api: the review statuses live in the cloud
    else:
        with closing(sqlite3.connect(handler.database, timeout=10)) as connection:
            reviews = current_reviews(connection, catalog)[0]
    selected = approved_pairs(rows, catalog, reviews)
    by_id = {row['id']: row for row in rows}
    for pair_id, roles in selected.items():
        for role, choice in roles.items():
            record = catalog[choice['key']]
            group = 'mains' if role == 'main' else 'subs'
            item = next(item for item in by_id[pair_id][group] if item['icon'] == choice['icon']
                        and drawing_key(item) == choice['key'])
            if record.get('artwork_source', 'use_org') != 'use_org':
                artwork = resolve_artwork(record, handler.server.artwork.get(choice['key']))
                if artwork is None or artwork['svg_sha256'] != choice['svg_sha256']:
                    raise ValueError('An approved artwork selection changed. Reload and try again.')
                choice['document'] = artwork['svg']
            elif item.get('sha256') != choice['svg_sha256']:
                document = icon_from_graph(baseline(record)).to_svg()
                if sha(document) != choice['svg_sha256']:
                    raise ValueError('An approved icon export changed. Reload and try again.')
                choice['document'] = document
    return selected
