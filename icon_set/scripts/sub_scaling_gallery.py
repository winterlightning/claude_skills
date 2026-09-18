"""Read-only solo-to-sub scaling inspection, using the combination sizing rule."""
import json
import math
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from .combination_experiment import placement

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist


ROOT = Path(__file__).resolve().parents[2]


def inspection_keyshapes():
    from icon_set.model import contracts
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.profiles import Profile
    return [dict(name=name, radial=Keyshape[name].is_radial,
                 sub_bounds=Keyshape[name].bounds_for(Profile.SUB32),
                 solo_bounds=Keyshape[name].bounds_for(Profile.SOLO48))
            for name in contracts.icon_profile()['profiles']['SOLO48']['keyshape_choices']]


def keyshape_fit(metrics, shape, radial_ink):
    left, top, right, bottom = shape['sub_bounds']
    width, height = right-left, bottom-top
    if shape['radial']:
        difference = radial_ink - width/2
        return 'matches' if abs(difference) < 1e-6 else 'inside' if difference < 0 else 'exceeds'
    dw, dh = metrics['ink_width']-width, metrics['ink_height']-height
    if abs(dw) < 1e-6 and abs(dh) < 1e-6:
        return 'matches'
    return 'inside' if dw <= 1e-6 and dh <= 1e-6 else 'exceeds'


def scaling_metrics(item):
    p = placement(item, 32, (1, 1), (0, 0), size_lock='auto')
    bounds = item['bounds']
    ink = p['painted_box']
    extent = bounds[2] - bounds[0]
    scale = (ink['w'] - 4) / extent if extent else (ink['h'] - 4) / (bounds[3] - bounds[1])
    scale_y = (ink['h']-4)/(bounds[3]-bounds[1]) if bounds[3]>bounds[1] else scale
    # Centre this inspection preview on a 32px canvas, independent of pair position.
    dx = (32 - ink['w']) / 2 + 2 - bounds[0] * scale
    dy = (32 - ink['h']) / 2 + 2 - bounds[1] * scale_y
    return {'scale': scale, 'scale_y':scale_y, 'proportion_change':abs(scale/scale_y-1)*100, 'ink_width': ink['w'], 'ink_height': ink['h'],
            'centerline_width': ink['w'] - 4, 'centerline_height': ink['h'] - 4,
            'dx': dx, 'dy': dy}


def scaled_document(document, metrics):
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    if abs(metrics['scale']-metrics.get('scale_y',metrics['scale'])) > 1e-8:
        sys.path.insert(0,str(ROOT/'icon_set/vendor/combination'))
        from box_combine import parse_segments, write_svg
        with tempfile.TemporaryDirectory() as folder:
            source=Path(folder)/'source.svg';source.write_text(document)
            segments=parse_segments(source)
            segments=[[(x*metrics['scale']+metrics['dx'],y*metrics['scale_y']+metrics['dy']) for x,y in seg] for seg in segments]
            target=Path(folder)/'scaled.svg';write_svg(segments,target,canvas=32,stroke=4,color='currentColor')
            return target.read_text()
    root = ET.fromstring(document)
    scale = metrics['scale']
    # The engine keeps a 4px final stroke, unlike a simple SVG display resize.
    root.attrib.update(width='32', height='32', viewBox='0 0 32 32')
    for element in root.iter():
        if 'stroke-width' in element.attrib:
            element.set('stroke-width', str(4 / scale))
    group = ET.Element('{http://www.w3.org/2000/svg}g', {
        'transform': f'translate({metrics["dx"]} {metrics["dy"]}) scale({scale})'})
    for child in list(root):
        root.remove(child)
        group.append(child)
    root.append(group)
    return ET.tostring(root, encoding='unicode')


def stage_sub_scaling(target):
    from icon_set.model.icons.registry import create
    from icon_set.validation.envelope import centerline_radial_extent
    shapes = inspection_keyshapes()
    source = ROOT / 'icon_set/data/combination-pairs.json'
    pairs = json.loads(source.read_text()).get('rows', []) if source.exists() else []
    audit_path = ROOT / 'icon_set/data/combination-sub32-audit.json'
    audit = {r['icon_id']: r for r in json.loads(audit_path.read_text())['rows']} if audit_path.exists() else {}
    rows = {}
    for pair in pairs:
        for item in pair['subs']:
            if item['family'] != 'solo':
                continue
            uid = item['icon']
            if uid not in rows:
                metrics = scaling_metrics(item)
                a = audit.get(uid, {})
                native_id = a.get('native_icon_id')
                native_path = development_dist(ROOT) / 'sub32' / ((native_id or '') + '.svg')
                original = create(uid)
                off_grid = []
                for primitive in original.draw().primitives:
                    for name, point in [('start', primitive.start), ('end', primitive.end)]:
                        for axis, value, offset in [('x', point.x, metrics['dx']), ('y', point.y, metrics['dy'])]:
                            value = value * (metrics['scale_y'] if axis=='y' else metrics['scale']) + offset
                            if not math.isclose(value, round(value), abs_tol=1e-6):
                                off_grid.append(f'{primitive.element_id}.{name}.{axis}: {value:.3f}')
                    for name in ('radius_x', 'radius_y'):
                        if hasattr(primitive, name):
                            value = getattr(primitive, name) * (metrics['scale_y'] if name=='radius_y' else metrics['scale'])
                            if not math.isclose(value, round(value), abs_tol=1e-6):
                                off_grid.append(f'{primitive.element_id}.{name}: {value:.3f}')
                bounds = item['bounds']
                radial_ink = centerline_radial_extent(original.draw().primitives,
                    ((bounds[0]+bounds[2])/2, (bounds[1]+bounds[3])/2)) * metrics['scale'] + 2
                target_keyshape = {'HRECT_XL':'HRECT_L', 'HRECT_S':'HRECT_L',
                                   'VRECT_XL':'VRECT_L', 'VRECT_S':'VRECT_L'}.get(original.keyshape.name, original.keyshape.name)
                rows[uid] = dict(icon_id=uid, original=item['document'],
                    scaled=scaled_document(item['document'], metrics),
                    source_ink=[bounds[2]-bounds[0]+4, bounds[3]-bounds[1]+4],
                    source_keyshape=original.keyshape.name, **metrics,
                    target_keyshape=target_keyshape,
                    keyshape_fits={s['name']:keyshape_fit(metrics,s,radial_ink) for s in shapes},
                    off_grid=off_grid, native_icon_id=native_id,
                    native=native_path.read_text() if native_id and native_path.is_file() else None,
                    audit_status=a.get('status','not_audited'), audit_reason=a.get('reason','Not audited against a SUB32 keyshape yet.'),
                    default_count=0, pairs=[])
            entry = rows[uid]
            is_default = pair['subs'][0]['icon'] == uid
            entry['default_count'] += int(is_default)
            entry['pairs'].append({'id':pair['id'], 'concept':pair['concept'], 'default':is_default,
                                   'selected_sub':pair['subs'][0]['icon']})
    result = {'keyshapes':shapes, 'rows':sorted(rows.values(), key=lambda r:(-r['default_count'],-len(r['pairs']),r['icon_id'])),
              'pair_count':len(pairs), 'solo_default_pairs':sum(p['subs'][0]['family']=='solo' for p in pairs)}
    target.mkdir(parents=True, exist_ok=True)
    (target/'sub-scaling.json').write_text(json.dumps(result))
    for name in ('sub-scaling.html','sub-scaling.js','sub-scaling.css'):
        shutil.copyfile(Path(__file__).with_name('templates')/name, target/name)
    return result


if __name__ == '__main__':
    result = stage_sub_scaling(development_dist(ROOT) / 'gallery')
    print(f'{len(result["rows"])} unique solo options; {result["solo_default_pairs"]} pairs currently use a solo sub.')
