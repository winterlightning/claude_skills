"""Inventory side mains with at least two source-bound fillable regions.

The counted regions are top-level enclosed holes in a saved Normal region
recipe. Nested islands and detail cutouts are not additional fill choices.
"""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import hashlib
import html
import json
from collections import Counter, defaultdict
from pathlib import Path

from shapely import wkt

from .adaptive_overlap import (DEFAULT_LAYOUTS, ROOT, main_variant_policy, variant_rejected,
                               region_recipe, region_variants)
from .combine_fill_side import geometry_to_svg, load_fill

DEFAULT_OUT = WORK / 'multi-region-mains'


def top_level_holes(recipe):
    by_id = {region['id']: region for region in recipe['regions']}
    return [region for region in recipe['regions']
            if region['ring'] == 'hole' and region['parent'] in by_id
            and by_id[region['parent']]['ring'] == 'exterior'
            and by_id[region['parent']]['level'] == 1]


def clear_top_bottom(regions):
    if len(regions) != 2 or any(r['area'] < 50 for r in regions):
        return False
    top, bottom = sorted(regions, key=lambda r: r['center_y'])
    a, b = top['bounds'], bottom['bounds']
    horizontal_overlap = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    narrow_width = max(1, min(a[2] - a[0], b[2] - b[0]))
    return b[1] - a[3] >= -1 and horizontal_overlap / narrow_width > 0.5


def inventory(layouts, out):
    items = json.loads(layouts.read_text())['items']
    by_main = defaultdict(list)
    for item in items:
        part = next((p for p in item['parts'] if p['role'] == 'main' and p.get('icon')), None)
        if part:
            by_main[part['icon'].split('/', 1)[1]].append({'id': item['reference_id'],
                                                            'concept': item['concept']})
    (out / 'variants').mkdir(parents=True, exist_ok=True)
    for old_preview in (out / 'variants').glob('*.svg'):
        old_preview.unlink()
    rows, errors = [], []
    for name, pairs in sorted(by_main.items()):
        source = DATA / 'normal' / f'{name}.svg'
        if not source.exists():
            continue
        recipe, recipe_path = region_recipe(name, source)
        if recipe is None:
            continue
        holes = top_level_holes(recipe)
        if len(holes) < 2:
            continue
        ordered = sorted(holes, key=lambda r: wkt.loads(r['geometry_wkt']).centroid.y)
        positions = {r['id']: ('top' if n == 0 else 'bottom' if n == len(ordered) - 1 else f'middle-{n}')
                     for n, r in enumerate(ordered)}
        regions = []
        largest_source_region = max(holes, key=lambda r: wkt.loads(r['geometry_wkt']).area)
        for region in holes:
            geometry = wkt.loads(region['geometry_wkt'])
            regions.append({'id': region['id'], 'decision': region['decision'],
                            'area': round(geometry.area, 2),
                            'bounds': [round(v, 2) for v in geometry.bounds],
                            'center_y': round(geometry.centroid.y, 2),
                            'position': positions[region['id']],
                            'variant': f"region-{region['id']}"})
        regions.sort(key=lambda r: r['center_y'])
        policy = main_variant_policy(name)
        approved = set(policy.get('approved', []))
        rejected = set(policy.get('rejected', []))
        preferred = policy.get('preferred_main_variant')
        if preferred and preferred not in approved:
            errors.append({'main': f'solo/{name}', 'error': f'preferred main variant is not approved: {preferred}'})
            preferred = None
        extra_variants = []
        try:
            variants, _ = region_variants(name, source, policy.get('groups', {}))
            current_file = DATA / 'normal-fill' / f'{name}.svg'
            current_geometry = load_fill(current_file)[0] if current_file.exists() else None
            files = {}
            unique_geometries = []
            for label, geometry in variants:
                status = ('rejected' if variant_rejected(policy, label) else
                          'duplicate_current' if current_geometry is not None
                          and geometry.symmetric_difference(current_geometry).area < 0.5 else
                          'duplicate_variant' if any(geometry.symmetric_difference(previous).area < 0.5
                                                     for previous in unique_geometries) else
                          'approved' if label in approved else 'unreviewed')
                if status in ('rejected', 'duplicate_current', 'duplicate_variant'):
                    files[label] = (None, status)
                    continue
                unique_geometries.append(geometry)
                path = out / 'variants' / f'{name}--{label}.svg'
                path.write_text(geometry_to_svg(geometry, '0 0 48 48'))
                files[label] = (str(path.relative_to(out)), status)
            for region in regions:
                region['preview'], region['status'] = files.get(region['variant'], (None, 'missing'))
            group_ids = {f'group-{group_name}': spec if isinstance(spec, list) else spec.get('fill', [])
                         for group_name, spec in policy.get('groups', {}).items()}
            for label, _ in variants:
                if not label.startswith('group-'):
                    continue
                ids = group_ids.get(label, [r['id'] for r in regions if r['id'] != largest_source_region['id']])
                preview, status = files.get(label, (None, 'missing'))
                extra_variants.append({'variant': label, 'region_ids': ids,
                                       'preview': preview, 'status': status})
        except Exception as error:
            errors.append({'main': f'solo/{name}', 'error': str(error)})
        sample = pairs[0] if pairs else None
        rows.append({'main': f'solo/{name}', 'name': name, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                     'recipe': str(recipe_path), 'region_count': len(regions), 'regions': regions,
                     'largest_region': largest_source_region['id'],
                     'largest_region_filled': largest_source_region['decision'] == 'fill',
                     'clear_top_bottom': clear_top_bottom(regions),
                     'extra_variants': extra_variants, 'review_reason': policy.get('reason'),
                     'preferred_main_variant': preferred, 'side_pair_count': len(pairs),
                     'sample_pair': sample, 'side_pairs': pairs})
    rows.sort(key=lambda r: (not (r['clear_top_bottom'] and r['largest_region_filled']),
                             -r['side_pair_count'], r['name']))
    variant_statuses = Counter(variant['status'] for row in rows
                               for variant in row['regions'] + row['extra_variants'])
    result = {'schema': 'side-multi-region-mains/v1',
              'definition_sha256': hashlib.sha256(layouts.read_bytes()).hexdigest(),
              'counts': {'unique_side_mains': len(by_main), 'eligible_mains': len(rows),
                         'eligible_side_pairs': sum(r['side_pair_count'] for r in rows),
                         'largest_region_currently_filled': sum(r['largest_region_filled'] for r in rows),
                         'clear_top_bottom': sum(r['clear_top_bottom'] for r in rows),
                         'clear_top_bottom_largest_filled': sum(r['clear_top_bottom'] and r['largest_region_filled'] for r in rows),
                         'approved_variants': variant_statuses['approved'],
                         'rejected_variants': variant_statuses['rejected'],
                         'unreviewed_variants': variant_statuses['unreviewed'],
                         'preview_errors': len(errors)},
              'rows': rows, 'errors': errors}
    out.mkdir(parents=True, exist_ok=True)
    (out / 'inventory.json').write_text(json.dumps(result, indent=2) + '\n')
    (out / 'names.txt').write_text('\n'.join(sorted(r['main'] for r in rows)) + '\n')
    focused = [r for r in rows if r['clear_top_bottom'] and r['largest_region_filled']]
    lines = ['# Clear top/bottom fill alternatives', '',
             'The larger region is currently filled. These smaller-region choices are candidates for side combinations, not approved replacements.', '',
             '| Main icon | Top region | Bottom region | Side pairs | Sample pair ID |',
             '| --- | --- | --- | ---: | --- |']
    for row in focused:
        top, bottom = row['regions']
        sample_id = row['sample_pair']['id'] if row['sample_pair'] else ''
        lines.append(f"| {row['main']} | {top['id']} ({top['decision']}, {top['area']} px²) | "
                     f"{bottom['id']} ({bottom['decision']}, {bottom['area']} px²) | "
                     f"{row['side_pair_count']} | {sample_id} |")
    (out / 'top-bottom-candidates.md').write_text('\n'.join(lines) + '\n')
    (out / 'index.html').write_text(gallery(result))
    return result['counts']


def gallery(result):
    cards = []
    for row in result['rows']:
        name = html.escape(row['main'])
        category = 'top_bottom' if row['clear_top_bottom'] and row['largest_region_filled'] else 'other'
        images = [f"<figure><img loading='lazy' src='../../../normal/{html.escape(row['name'])}.svg'><figcaption>source</figcaption></figure>",
                  f"<figure><img loading='lazy' src='../../../output/normal-fill/{html.escape(row['name'])}.svg'><figcaption>current fill</figcaption></figure>"]
        for region in row['regions']:
            src = html.escape(region.get('preview') or '')
            if not src:
                continue
            preferred = row['preferred_main_variant'] == region['variant']
            remove = (f"<button type='button' class='remove' data-remove data-name='{html.escape(row['name'])}' "
                      f"data-variant='{html.escape(region['variant'])}'>Remove</button>")
            images.append(f"<figure {'class=preferred' if preferred else ''} data-status='{html.escape(region['status'])}'><img loading='lazy' src='{src}'><figcaption>{html.escape(region['position'])} · region {region['id']}<br>{region['area']} px² · {'preferred main fill' if preferred else html.escape(region['status'])}</figcaption>{remove}</figure>")
        for group in row['extra_variants']:
            src = html.escape(group.get('preview') or '')
            if src:
                preferred = row['preferred_main_variant'] == group['variant']
                remove = (f"<button type='button' class='remove' data-remove data-name='{html.escape(row['name'])}' "
                          f"data-variant='{html.escape(group['variant'])}'>Remove</button>")
                images.append(f"<figure {'class=preferred' if preferred else ''} data-status='{html.escape(group['status'])}'><img loading='lazy' src='{src}'><figcaption>{html.escape(group['variant'])}<br>regions {','.join(map(str, group['region_ids']))} · {'preferred main fill' if preferred else html.escape(group['status'])}</figcaption>{remove}</figure>")
        side = ''
        if row['sample_pair']:
            pair_id = html.escape(row['sample_pair']['id'])
            side = f"<p>Sample side pair: {html.escape(row['sample_pair']['concept'])} · {pair_id}</p>"
        cards.append(f"<section id='{html.escape(row['name'])}' data-name='{name}' data-category='{category}'><h2>{name}</h2><p>{row['region_count']} regions · {row['side_pair_count']} side pairs · largest region {row['largest_region']} {'currently filled' if row['largest_region_filled'] else 'currently kept'}</p>{side}<div class='images'>{''.join(images)}</div></section>")
    counts = result['counts']
    return ("<!doctype html><html><meta charset='utf-8'><title>Multi-region side mains</title>"
            "<style>body{font:15px system-ui;background:#f5f5f5;color:#222;max-width:1200px;margin:24px auto;padding:0 16px}section{background:white;padding:16px;margin:16px 0;border-radius:10px;scroll-margin-top:115px}h2{font-size:18px;margin:0}.images{display:flex;flex-wrap:wrap;gap:12px}figure{margin:0;text-align:center;border:1px solid #ddd;border-radius:6px;padding:8px}figure.preferred{border:2px solid #167a53;background:#effbf5}img{width:112px;height:112px}figcaption{font-size:12px}button.remove{display:block;margin:8px auto 0;padding:4px 10px;border:1px solid #a33;border-radius:5px;background:white;color:#922;cursor:pointer}button.remove:hover{background:#fff0f0}button.remove:disabled{opacity:.5;cursor:wait}input,select{font:inherit;padding:8px;margin-right:8px}#summary{position:sticky;top:0;background:#f5f5f5;padding:12px 0}#save-status{color:#167a53;margin-left:10px}body:not(.show-unreviewed) figure[data-status='unreviewed']{display:none}</style>"
            f"<div id='summary'><h1>Main icons with multiple fill regions</h1><p>{counts['eligible_mains']} mains · {counts['eligible_side_pairs']} side pairs · <span id='approved-count'>{counts['approved_variants']}</span> approved · <span id='rejected-count'>{counts['rejected_variants']}</span> rejected · {counts['unreviewed_variants']} awaiting review</p>"
            "<input id='search' placeholder='Search icon name'><select id='filter'><option value='all'>All multi-region mains</option><option value='top_bottom'>Top/bottom, largest currently filled</option></select><label><input type='checkbox' id='unreviewed'>Show unreviewed candidates</label> <span id='shown'></span><span id='save-status' role='status'></span></div>"
            + ''.join(cards)
            + "<script>const cards=[...document.querySelectorAll('section')],q=document.querySelector('#search'),f=document.querySelector('#filter'),shown=document.querySelector('#shown'),unreviewed=document.querySelector('#unreviewed'),saveStatus=document.querySelector('#save-status');function update(){let n=0;for(const c of cards){const yes=c.dataset.name.includes(q.value.trim().toLowerCase())&&(f.value==='all'||c.dataset.category===f.value);c.hidden=!yes;if(yes)n++}document.body.classList.toggle('show-unreviewed',unreviewed.checked);shown.textContent=n+' shown'}q.addEventListener('input',update);f.addEventListener('change',update);unreviewed.addEventListener('change',update);document.addEventListener('click',async event=>{const button=event.target.closest('button[data-remove]');if(!button||button.disabled)return;button.disabled=true;saveStatus.textContent='Saving rejection…';try{const response=await fetch('/side_combinations/api/reject-main-variant',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:button.dataset.name,variant:button.dataset.variant})});const result=await response.json();if(!response.ok)throw Error(result.error||'Could not save rejection');button.closest('figure').remove();document.querySelector('#approved-count').textContent=result.counts.approved_variants;document.querySelector('#rejected-count').textContent=result.counts.rejected_variants;saveStatus.textContent='Removed and saved';}catch(error){button.disabled=false;saveStatus.textContent=error.message;}});update()</script></html>")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--layouts', type=Path, default=DEFAULT_LAYOUTS)
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    print(json.dumps(inventory(args.layouts, args.out), indent=2))


if __name__ == '__main__':
    main()
