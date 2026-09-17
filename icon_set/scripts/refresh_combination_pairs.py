"""Rescan exported components by declared source identity for the combinations grid."""
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from .category_report import REPO_ROOT, model_catalog, source_id
from .combination_experiment import DATA, ROOT


def refresh():
    sys.path.insert(0, str(ROOT / 'vendor/combination'))
    from box_combine import bbox, parse_segments
    old = json.loads(DATA.read_text())['rows'] if DATA.exists() else []
    previous = {item['svg']: item for row in old for role in ('mains', 'subs') for item in row[role]}
    index = defaultdict(list)
    profiles = {'solo': 'solo48', 'sub': 'sub32', 'container': 'container64'}
    for model in model_catalog():
        path = ROOT / 'dist' / profiles[model['family']] / (model['icon_id'] + '.svg')
        if not path.exists():
            continue
        ids = {model['source_id']}
        if model['source_path']:
            ids.add(source_id(model['source_path']))
        for uid, reference in model['source_references']:
            ids.add(uid)
            if reference:
                ids.add(source_id(reference))
        item = {'icon': model['icon_id'], 'family': model['family'], 'svg': path.relative_to(REPO_ROOT).as_posix()}
        for uid in ids:
            if uid:
                index[uid.lower()].append(item)
    measured = {}

    def measure(item):
        key = item['svg']
        if key not in measured:
            path = REPO_ROOT / key
            document = path.read_text()
            digest = hashlib.sha256(document.encode()).hexdigest()
            if previous.get(key, {}).get('sha256') == digest:
                measured[key] = previous[key]
            else:
                viewbox = list(map(float, ET.fromstring(document).attrib['viewBox'].split()))
                measured[key] = dict(item, document=document, sha256=digest,
                                     bounds=bbox(parse_segments(path)), canvas=viewbox[2])
        return measured[key]

    rows = []
    counts = Counter()
    for kind, entries in json.loads((REPO_ROOT / 'combination_data.json').read_text()).items():
        for row in entries:
            mains = [m for m in index.get((row.get('main_id') or '').lower(), [])
                     if m['family'] == ('container' if kind == 'container' else 'solo')]
            subs = [m for m in index.get((row.get('sub_id') or '').lower(), []) if m['family'] == 'sub']
            if mains and subs:
                counts[kind] += 1
                # This experiment currently implements side placement only.
                if kind == 'side':
                    rows.append(dict(row, type=kind, mains=list(map(measure, mains)), subs=list(map(measure, subs))))
    DATA.write_text(json.dumps({'rows': rows}))
    (ROOT / 'dist/gallery/experiment-combination.json').write_text(DATA.read_text())
    catalog = ROOT / 'dist/gallery/experiments.json'
    totals = json.loads(catalog.read_text())
    totals['combination'] = len(rows)
    catalog.write_text(json.dumps(totals))
    print(f'Available: {dict(counts)}; grid: {len(old)} → {len(rows)}')


if __name__ == '__main__':
    refresh()
    if '--previews' in sys.argv:
        from .build_combination_previews import build
        build()
