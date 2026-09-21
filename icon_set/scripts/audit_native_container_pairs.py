"""Compose defined container pairs at native size and measure ink-edge padding."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from shapely.affinity import translate
from .container_placement import Artwork, render
from .container_vector_geometry import VectorInk, reject_effects, vector_zone, check_pair
from .workspace import build_dist

ROOT = Path(__file__).resolve().parents[2]


class NativeSub:
    def __init__(self, art):
        self.ink = VectorInk.from_art(art)
        self.envelopes = {outer: self.ink.envelope(2, outer) for outer in (True, False)}

    def at(self, dx, dy):
        source = self
        class Placed:
            lines = translate(source.ink.lines, dx, dy)
            error = source.ink.error
            def envelope(self, radius, outer):
                assert radius == 2
                return translate(source.envelopes[outer], dx, dy)
        return Placed()


def load_art(path):
    doc = path.read_text()
    root = reject_effects(doc)
    vb = [float(v) for v in root.get('viewBox', '').replace(',', ' ').split()]
    if len(vb) != 4 or vb[:2] != [0, 0] or any(v != int(v) for v in vb):
        raise ValueError('Unsupported native canvas')
    return Artwork.read(doc, (int(vb[2]), int(vb[3])))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--padding', type=float, default=6)
    parser.add_argument('--out', type=Path, default=ROOT/'published/reports/container-pairs-padding-6')
    args = parser.parse_args()
    if not 0 <= args.padding < 64:
        parser.error('Padding must be between 0 and 64.')
    out = args.out
    (out/'svg').mkdir(parents=True, exist_ok=True)
    gallery = build_dist(ROOT)/'gallery'
    catalog = json.loads((gallery/'combinations.json').read_text())
    pairs = [r for r in catalog['rows'] if r['kind'] == 'container']
    library = json.loads((gallery/'icons.json').read_text())
    records = {r['key']: r for r in library['icons'] + library.get('failed_icons', [])}
    areas = json.loads((ROOT/'icon_set/data/container-content-areas.json').read_text())['areas']
    prefs = json.loads((ROOT/'icon_set/data/container-placement-preferences.json').read_text())
    hosts, subs, rows = {}, {}, []

    def host(g):
        key = g['key']
        if key not in hosts:
            art = load_art((gallery/g['preview_url']).resolve())
            ink = VectorInk.from_art(art)
            area = areas.get(g['icon_id'], {})
            info, inner, outer = vector_zone(ink, area)
            center = prefs.get('container_centers', {}).get(g['icon_id']) or area.get('center') or info.get('center_units') or [32, 32]
            hosts[key] = art, ink, inner, outer, center, info
        return hosts[key]

    def sub(g):
        key = (g['key'], g['preview_url'])
        if key not in subs:
            art = load_art((gallery/g['preview_url']).resolve())
            subs[key] = art, NativeSub(art)
        return subs[key]

    for index, pair in enumerate(pairs):
        mains, children = pair.get('main_generated', []), pair.get('sub_generated', [])
        if not mains or not children:
            rows.append(dict(pair_id=pair['id'], concept=pair['concept'], status='missing', reason='Missing linked main or sub artwork'))
            continue
        seen = set()
        for hg in mains:
            for sg in children:
                identity = (hg['key'], sg['key'], sg['preview_url'])
                if identity in seen:
                    continue
                seen.add(identity)
                row = dict(pair_id=pair['id'], concept=pair['concept'], main=hg['key'], sub=sg['key'])
                try:
                    ha, hi, inner, outer, center, info = host(hg)
                    sa, si = sub(sg)
                    center = prefs.get('optical_overrides', {}).get(hg['icon_id'], {}).get(sg['icon_id'], center)
                    width, height = sa.canvas
                    dx, dy = center[0]-width/2, center[1]-height/2
                    # No scaling or fit optimization: evaluate the current native artwork.
                    metrics = check_pair(hi, si.at(dx, dy), inner, outer, padding=args.padding)
                    digest = hashlib.sha256('|'.join((pair['id'], *identity)).encode()).hexdigest()[:20]
                    filename = f'svg/{digest}.svg'
                    (out/filename).write_text(render(ha, sa, (1, dx, dy)))
                    (out/f'svg/{digest}-padding.svg').write_text(render(ha, sa, (1, dx, dy), padding=args.padding))
                    record = records.get(sg['key'], {})
                    validation = sg.get('model_validation') or ('fail' if record.get('build_failed') else record.get('validation', 'unknown'))
                    if isinstance(validation, dict):
                        validation = validation.get('automatic_status', validation.get('status', 'unknown'))
                    row.update(status=metrics['status'], metrics=metrics, source_validation=validation,
                               fully_validated=metrics['status']=='pass' and validation=='pass',
                               preview=filename, padding_preview=f'svg/{digest}-padding.svg',
                               native_size=[width,height], center=center, transform=[1,dx,dy],
                               host_sha256=ha.sha256, sub_sha256=sa.sha256, interior=info)
                except (ValueError, OSError, KeyError) as exc:
                    row.update(status='blocked', reason=str(exc))
                    # Unsupported measurement does not prevent a faithful preview.
                    try:
                        hdoc = ET.fromstring((gallery/hg['preview_url']).resolve().read_text())
                        sdoc = ET.fromstring((gallery/sg['preview_url']).resolve().read_text())
                        vb = [float(v) for v in sdoc.get('viewBox', '').split()]
                        if len(vb) != 4 or vb[:2] != [0, 0]:
                            raise ValueError('Unsupported preview canvas')
                        center = prefs.get('container_centers', {}).get(hg['icon_id']) or areas.get(hg['icon_id'], {}).get('center') or [32, 32]
                        center = prefs.get('optical_overrides', {}).get(hg['icon_id'], {}).get(sg['icon_id'], center)
                        for node, x, y, w, h in ((hdoc,0,0,64,64),(sdoc,center[0]-vb[2]/2,center[1]-vb[3]/2,vb[2],vb[3])):
                            node.attrib.update(x=str(x),y=str(y),width=str(w),height=str(h),overflow='visible')
                        root = ET.Element('{http://www.w3.org/2000/svg}svg', {'viewBox':'0 0 64 64','width':'64','height':'64'})
                        root.extend([hdoc,sdoc])
                        digest = hashlib.sha256('|'.join((pair['id'], *identity)).encode()).hexdigest()[:20]
                        filename = f'svg/{digest}.svg'
                        (out/filename).write_text(ET.tostring(root,encoding='unicode'))
                        row.update(preview=filename,padding_preview=filename,native_size=vb[2:],center=center)
                    except (ValueError, OSError, ET.ParseError):
                        pass
                rows.append(row)
        if (index+1) % 200 == 0:
            print(f'{index+1}/{len(pairs)} pairs processed', flush=True)
    counts = dict(Counter(r['status'] for r in rows))
    by_pair = defaultdict(list)
    for row in rows:
        by_pair[row['pair_id']].append(row)
    summary = dict(defined_pairs=len(pairs), composition_results=sum('main' in r for r in rows),
                   counts=counts, pairs_with_passing_fit=sum(any(r['status']=='pass' for r in group) for group in by_pair.values()),
                   fully_validated_compositions=sum(r.get('fully_validated', False) for r in rows),
                   fully_validated_pairs=sum(any(r.get('fully_validated') for r in group) for group in by_pair.values()))
    data = dict(padding=args.padding, summary=summary, rows=rows,
                policy='Defined pairs only; current native dimensions, scale=1, 4-unit strokes, saved content/optical centers. Pass requires gap, containment and canvas checks. Uncertain boundaries stay review. No artwork or sizing suggestions modified.')
    (out/'results.json').write_text(json.dumps(data, separators=(',', ':'))+'\n')
    template = (ROOT/'icon_set/scripts/templates/native-container-audit.html').read_text()
    (out/'index.html').write_text(template.replace('__DATA__', json.dumps(data).replace('<', '\\u003c')))
    print(json.dumps(summary, indent=2), flush=True)
    print(out/'index.html', flush=True)


if __name__ == '__main__':
    main()
