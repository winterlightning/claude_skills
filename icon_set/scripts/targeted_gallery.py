"""Update selected gallery entries without regenerating unrelated assets."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from urllib.parse import quote


def read(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def write(path, value):
    text = json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n'
    if not path.exists() or read(path, None) != value:
        path.write_text(text)


def stage_targeted_gallery(staged: Path, published: Path, folders, only) -> Path:
    from . import gallery as g
    from icon_set.model.icons.registry import factories
    from .primitives_catalog import model_links, link, row_uuids

    target = staged / 'gallery'
    old_gallery = published / 'gallery'
    if old_gallery.exists():
        shutil.copytree(old_gallery, target)
    else:
        target.mkdir()
        # Bootstrap static UI only; experiments and other families remain explicit builds.
        templates = Path(g.__file__).with_name('templates')
        for path in templates.iterdir():
            if path.is_file() and path.suffix in ('.html', '.css', '.js'):
                shutil.copyfile(path, target / ('index.html' if path.name == 'gallery.html' else path.name))
    data = read(target / 'icons.json', {'icons': [], 'failed_icons': []})
    old_selected = [r for field in ('icons', 'failed_icons') for r in data.get(field, []) if r['icon_id'] in only]
    registered = factories()
    sources, authoring = g.original_sources(only), g.python_sources(only)
    changed, failed = [], []
    for folder in folders:
        for is_failed, rows in ((False, changed), (True, failed)):
            relative = Path('failed') / folder if is_failed else Path(folder)
            manifest = staged / relative / 'manifest.json'
            if not manifest.exists():
                manifest = published / relative / 'manifest.json'
            for raw in read(manifest, {'icons': []})['icons']:
                icon_id = raw['icon_id']
                if icon_id not in only:
                    continue
                factory = registered[icon_id]
                row = dict(raw)
                row.update(key=f'{factory.family}/{icon_id}',
                           preview_url='../' + relative.as_posix() + '/' + quote(icon_id, safe='') + '.svg',
                           original_sources=g.copy_originals(sources.get(icon_id, []), target),
                           python_source=authoring.get(icon_id),
                           author=getattr(sys.modules[factory.__module__], 'AUTHOR', ''))
                if is_failed:
                    row.update(name=icon_id, build_failed=True,
                               category=getattr(factory, 'category', ''), keywords=list(getattr(factory, 'keywords', ())))
                else:
                    ancestor = factory
                    while getattr(ancestor, 'variant_of', None):
                        ancestor = registered[ancestor.variant_of]
                    row.update(variant_of=getattr(factory, 'variant_of', None),
                               variant_label=getattr(factory, 'variant_label', ''), variant_root=ancestor.icon_id)
                rows.append(row)
    for field, rows in (('icons', changed), ('failed_icons', failed)):
        data[field] = [r for r in data.get(field, []) if r['icon_id'] not in only] + rows
        data[field].sort(key=lambda r: (r['family'], r['icon_id']))

    catalog = read(target / 'primitives.json', {'rows': [], 'categories': {}})
    links = model_links()
    built = {r['icon_id']: r for r in data['icons']}
    failed_ids = {r['icon_id'] for r in data['failed_icons']}
    affected = {}
    for row in catalog['rows']:
        models, method = link(row, links)
        if not only.intersection(models + row.get('models', [])):
            continue
        before = row.get('state', 'none')
        # Preserve existing editorial/model associations outside this selection.
        models = sorted(set(row.get('models', [])) - only | (set(models) & only))
        generated = [dict(icon_id=i, key=built[i]['key'], preview_url=built[i]['preview_url']) for i in models if i in built]
        state = 'generated' if generated else 'build_failed' if failed_ids.intersection(models) else 'model_only' if models else 'none'
        row.update(models=models, generated=generated, state=state)
        if only.intersection(models):
            row['match'] = method
        if state != before:
            counts = catalog['categories'].setdefault(row['category'], {})
            counts[before] = counts.get(before, 0) - 1
            counts[state] = counts.get(state, 0) + 1
        for uid in row_uuids(row):
            affected[uid] = generated
    if (target / 'primitives.json').exists():
        write(target / 'primitives.json', catalog)
    g.remap_categories(changed + failed, catalog)
    g.add_creation_times(changed + failed, published)
    g.add_modification_times(changed + failed, published)
    from .sub_reference_fidelity import annotate_sub_references
    from .sub_usage_categories import annotate_records
    from .profile_links import annotate
    annotate_sub_references(changed + failed)
    annotate_records(changed + failed)
    annotate(changed + failed)
    write(target / 'icons.json', data)

    preview = read(target / 'preview-icons.json', {'icons': []})
    preview['icons'] = [r for r in preview['icons'] if r['icon_id'] not in only]
    preview['icons'] += [{k: r.get(k, '') for k in ('icon_id', 'name', 'family', 'preview_url', 'category')} for r in changed]
    preview['icons'].sort(key=lambda r: (r['family'], r['icon_id']))
    write(target / 'preview-icons.json', preview)
    authors = read(target / 'authors.json', {})
    for row, delta in [(r, -1) for r in old_selected] + [(r, 1) for r in changed + failed]:
        if row.get('author'):
            author = row['author']
            authors[author] = max(0, authors.get(author, 0) + delta)
    write(target / 'authors.json', authors)

    # Refresh selected facets; retain every unrelated measurement verbatim.
    facets = read(target / 'review-facets.json', {})
    for row in old_selected + changed + failed:
        facets.pop(row['key'], None)
    facet_dir = staged / 'selected-facets'
    facet_dir.mkdir()
    g.stage_review_facets(changed, staged, published, facet_dir)
    facets.update(read(facet_dir / 'review-facets.json', {}))
    if facets or (target / 'review-facets.json').exists():
        write(target / 'review-facets.json', facets)

    combinations = read(target / 'combinations.json', None)
    if combinations is not None:
        for uid, generated in affected.items():
            if uid in combinations.get('references', {}):
                combinations['references'][uid]['generated'] = generated
        for row in combinations.get('rows', []):
            for role in ('main', 'sub'):
                if row.get(role + '_id') in affected and role + '_generated' in row:
                    row[role + '_generated'] = affected[row[role + '_id']]
        write(target / 'combinations.json', combinations)
    from .failure_report import FOCUS_FAMILIES
    g.stage_failures(staged, published, folders, target,
                     passed=sum(r['family'] in FOCUS_FAMILIES for r in data['icons']))
    return target
