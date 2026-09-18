"""Discover side pairs, including reusable 32px exports of solo components."""
import hashlib
import json
import sys
import shutil
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from .category_report import REPO_ROOT, model_catalog, source_id
from .combination_experiment import DATA, ROOT

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist



def export_sub32(document):
    """Derived export: maximum visible ink dimension 32, final stroke 4."""
    from .sub_ink32 import normalize_ink32
    return normalize_ink32(document)[0]


def refresh():
    sys.path.insert(0, str(ROOT / 'vendor/combination'))
    from box_combine import bbox, parse_segments
    old = json.loads(DATA.read_text())['rows'] if DATA.exists() else []
    previous = {item.get('source_svg', item['svg']): item for row in old for role in ('mains', 'subs') for item in row[role]}
    index = defaultdict(list)
    profiles = {'solo': 'solo48', 'sub': 'sub32', 'symbol': 'symbol32', 'container': 'container64', 'combination_main':'combination_main48'}
    for model in model_catalog():
        path = development_dist(REPO_ROOT) / profiles[model['family']] / (model['icon_id'] + '.svg')
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
    from .combination_state_subs import reviewed_states
    state_subs, state_skips = reviewed_states(ROOT)
    measured = {}
    exports = ROOT / 'assets/combination-sub32'
    exports.mkdir(exist_ok=True)
    public = development_dist(ROOT.parent) / 'gallery/combination-sub32'
    public.mkdir(exist_ok=True)
    export_path = ROOT / 'data/combination-sub32.json'
    export_manifest = json.loads(export_path.read_text()) if export_path.exists() else {}
    audit_path = ROOT / 'data/combination-sub32-audit.json'
    audit = {r['icon_id']: r for r in json.loads(audit_path.read_text())['rows']} if audit_path.exists() else {}

    def measure(item, role):
        key = (item['svg'], role)
        if key not in measured:
            path = REPO_ROOT / item['svg']
            document = path.read_text()
            digest = hashlib.sha256(document.encode()).hexdigest()
            prior = previous.get(item['svg'], {})
            viewbox = list(map(float, ET.fromstring(document).attrib['viewBox'].split()))
            bounds = prior.get('source_bounds', prior['bounds']) if prior.get('source_sha256', prior.get('sha256')) == digest else bbox(parse_segments(path))
            result = dict(item, document=document, sha256=digest, bounds=bounds, canvas=viewbox[2])
            if role == 'sub':
                if not item.get('native_study'):
                    from icon_set.model.icons.registry import create
                    from icon_set.model.keyshapes import Keyshape
                    from icon_set.model.profiles import Profile
                    from icon_set.validation.envelope import centerline_radial_extent
                    model = create(item['icon'])
                    shape = model.keyshape.name
                    if item['family'] != 'sub':
                        shape = {'HRECT_XL':'HRECT_L','HRECT_S':'HRECT_L',
                                 'VRECT_XL':'VRECT_L','VRECT_S':'VRECT_L'}.get(shape,shape)
                    if shape != 'FREE':
                        result['target_keyshape'] = shape
                        result['target_keyshape_bounds'] = Keyshape[shape].bounds_for(Profile.SUB32)
                        if shape == 'CIRCLE':
                            result['source_radial_extent'] = centerline_radial_extent(model.draw().primitives,
                                ((bounds[0]+bounds[2])/2,(bounds[1]+bounds[3])/2))
                text_layout = getattr(model, 'sizing_mode', None) == 'text-height32' if not item.get('native_study') else False
                result['sizing_kind'] = 'text' if text_layout else 'symbol'
                result['sub32_status'] = 'native_sub32' if item['family'] == 'sub' else 'needs_redraw'
                result['sub32_reason'] = '' if item['family'] == 'sub' else audit.get(item['icon'], {}).get('reason', 'Requires a separate grid-aligned SUB32 version.')
                if item['family'] == 'sub':
                    result['export_url'] = item.get('export_url') or '../sub32/' + path.name
            if role == 'sub' and item['family'] != 'text':
                from .sub_ink32 import normalize_ink32
                source_bounds = bounds
                repair_path = ROOT / 'data/sub-icon-repairs.json'
                repairs = json.loads(repair_path.read_text()) if repair_path.exists() else {}
                repair = repairs.get(item['family'] + '/' + item['icon'])
                if repair:
                    document = (REPO_ROOT / repair['repair_svg']).read_text()
                    ink = repair['ink32']
                else:
                    document, ink = normalize_ink32(document, text=result.get('sizing_kind') == 'text')
                bounds = ink['bounds']
                viewbox = [0,0,32,32]
                result.update(bounds=bounds, source_bounds=source_bounds, ink32=ink, sub32_status='ink32_normalized', sub32_reason='Grid-snapped reuse export; visual and authored-profile review remain separate.')
                file = exports / (item['family'] + '--' + item['icon'] + '.svg')
                file.write_text(document)
                shutil.copyfile(file, public / file.name)
                result.update(document=document, source_svg=item['svg'], source_sha256=digest,
                              svg=file.relative_to(REPO_ROOT).as_posix(), export_size=32,
                              export_url='combination-sub32/' + file.name,
                              sha256=hashlib.sha256(document.encode()).hexdigest())
                export_manifest[item['icon']] = {k: result[k] for k in ('icon','family','source_svg','svg','export_url','source_sha256','ink32')}
            # Account for a few sources whose centerlines reach their canvas edge.
            # Uniformly fit them so the combination engine's 4px stroke stays inside.
            size = 32 if role == 'sub' else 48
            extent = max(bounds[2]-bounds[0], bounds[3]-bounds[1])
            result['canvas'] = max(viewbox[2], extent*size/(size-4))
            measured[key] = result
        return measured[key]

    remap_path = ROOT / 'data/combination-remaps.json'
    remaps = json.loads(remap_path.read_text()).get('rules', []) if remap_path.exists() else []
    rows, failures = [], []
    for original in json.loads((REPO_ROOT / 'combination_data.json').read_text()).get('side', []):
        row = dict(original)
        for rule in remaps:
            field = rule['role'] + '_id'
            fragment = row['id'][:18] if rule['role'] == 'main' else row['id'][19:34]
            if not row.get(field) and fragment == rule['fragment']:
                row[field] = rule['reference_id']
        mains = sorted(index.get((row.get('main_id') or '').lower(), []), key=lambda m: ({'solo':0,'combination_main':0,'container':1,'sub':2}[m['family']],m['icon']))
        sub_id = (row.get('sub_id') or '').lower()
        subs = sorted(state_subs.get(sub_id, index.get(sub_id, [])), key=lambda m: ({'sub':0,'solo':1,'combination_main':1,'container':2}[m['family']],m['icon']))
        if not mains or not subs:
            continue
        try:
            rows.append(dict(row, type='side', mains=[measure(m,'main') for m in mains], subs=[measure(m,'sub') for m in subs]))
        except Exception as error:
            failures.append({'id':row['id'],'concept':row['concept'],'error':str(error)})
    DATA.write_text(json.dumps({'rows': rows, 'failures': failures, 'state_skips': state_skips}))
    (ROOT / 'data/combination-sub32.json').write_text(json.dumps(export_manifest, indent=2)+'\n')
    (development_dist(ROOT.parent) / 'gallery/experiment-combination.json').write_text(DATA.read_text())
    catalog = development_dist(ROOT.parent) / 'gallery/experiments.json'
    totals = json.loads(catalog.read_text())
    totals['combination'] = len(rows)
    catalog.write_text(json.dumps(totals))
    from .deduplicate_subs import run as deduplicate_subs
    deduplicate_subs()
    print(f'Available: {len(rows)} side pairs; {len(export_manifest)} reusable 32px exports; {len(failures)} failures; grid: {len(old)} → {len(rows)}', flush=True)


if __name__ == '__main__':
    refresh()
    if '--previews' in sys.argv:
        from .build_combination_previews import build
        build()
