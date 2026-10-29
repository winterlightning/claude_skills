"""The fill variant icons of the mains and subs the fill side pairs use: one SVG per variant, as the reviewed
pairs were combined from it: a main's current fill (stroke-fill/v1: regions plus the original 4px strokes) and its
flat region / group fills; a sub's fill (closed fills included). Never a rejected variant.

    python3 -m icon_set side-fill icons        # after `side-fill build`

Writes icon_set/state/side-fill/fill-icons/<main|sub>/<name>/<variant>.svg and manifest.json:
  [{key, source_key, variant, name, svg, svg_sha256, source_sha256}]
which cloud/migrate/upload_fill_parts.py stores (POST /api/icons/styled, style fill): each variant is an icon of style
fill in its solo / sub icon's own family, `key` (fill_key) beside the normal icon `source_key`.

Each SVG keeps its source drawing's canvas, 5 decimals, and what the upload route keeps (ids, not data- attributes:
portable()). The outline is the solo / sub icon itself: a pick uses its key, nothing is uploaded for it. A part whose
source was redrawn since its pairs were laid out, a text sub and an undrawn part get no icons: their variants
would belong to an old drawing, or to none.
"""
import argparse
import json
import hashlib

from .paths import DATA, WORK

OUT = WORK / 'fill-icons'


def fill_key(source, variant):
    """The fill variant's icon key, as POST /api/icons/styled stores it: <source>--fill for the fill itself (a main's
    current, a sub's fill), <source>--fill-<variant> for the others (region-3, group-wheels…)."""
    return f'{source}--fill' if variant in ('current', 'fill') else f'{source}--fill-{variant}'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def compact(svg):
    """publish.compact at 5 decimals: 2 or 4 move points enough to flip a cut's area threshold (a sliver kept or not)."""
    import re
    svg = re.sub(r'<\?xml[^>]*>\s*', '', svg)
    svg = re.sub(r'[-+]?(?:\d+\.\d+|\.\d+)(?:[eE][-+]?\d+)?', lambda m: f'{float(m.group()):.5f}'.rstrip('0').rstrip('.'), svg)
    return re.sub(r'>\s+<', '><', svg).strip()


def portable(svg, reverse=False):
    """The icon as the upload route stores it: it keeps ids and drops data- attributes, so the stroke-fill format
    is the root's id (stroke-fill-v1), each element's number its id (element-N), and a flat reverse fill's root id
    is reverse-fill (stroke_fill_format, combine_fill_side_layouts.is_reverse_fill read both forms)."""
    import xml.etree.ElementTree as ET
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    root = ET.fromstring(svg)
    if root.attrib.pop('data-format', None) == 'stroke-fill/v1':
        root.set('id', 'stroke-fill-v1')
    elif reverse:
        root.set('id', 'reverse-fill')
    for element in root.iter():
        number = element.attrib.pop('data-element', None)
        if number is not None:
            element.set('id', f'element-{int(number)}')
        for key in [k for k in element.attrib if k.startswith('data-')]:
            del element.attrib[key]
    return compact(ET.tostring(root, encoding='unicode'))


def variants_of(role, entry, part, needed=(), rejected=None):
    """[(label, svg text)] of one part, from the build's files, as the reviewed renders drew them: the fill (current
    for a main, fill for a sub), and a main's flat region / group fills (never a rejected one). `needed`: the
    variants picks use: the fill of a sub shown as its outline, and region variants the variants index hides
    (computed as the layout renderer computed them)."""
    from .adaptive_overlap import cached_region_variants, fill_path, main_variant_policy, source_path
    from .combine_fill_side import geometry_to_svg
    from .combine_fill_side_layouts import is_reverse_fill
    source, fill = source_path(part, role), fill_path(part, role)
    base = 'current' if role == 'main' else 'fill'
    out = []      # the outline is the solo / sub icon itself: not uploaded again
    if fill.is_file() and (entry['status'] == 'ready' or base in needed):
        out.append((base, portable(compact(fill.read_text()), is_reverse_fill(fill))))
    if role != 'main':
        return out
    index = json.loads((WORK / 'main-variants/index.json').read_text()).get(entry['name'], {})
    done = set()
    for variant in index.get('variants', []):
        if variant.get('status') == 'rejected' or rejected(entry['key'], variant['variant']):
            continue
        out.append((variant['variant'], portable(compact((WORK / variant['svg']).read_text()))))
        done.add(variant['variant'])
    missing = {label for label in needed if label.startswith(('region-', 'group-')) and label not in done
               and not rejected(entry['key'], label)}
    if missing:
        groups = json.dumps(main_variant_policy(entry['name']).get('groups', {}), sort_keys=True)
        for label, geometry in cached_region_variants(entry['name'], source, groups)[0]:
            if label in missing:
                out.append((label, portable(compact(geometry_to_svg(geometry, '0 0 48 48')))))
    return out


def site_fill(role, entry):
    """[('current', svg)] for a main redrawn since its pairs were laid out whose snapshot drawing the site confirmed
    is its current one (`side-fill sources`): its reworked fill of that drawing. Its pairs stay uncombined until they
    are laid out again; its fill can be reviewed and picked meanwhile."""
    from .adaptive_overlap import source_path
    from .combine_fill_side_layouts import is_reverse_fill
    from .publish_stroke_fills import ROLES, SKIP_STATUSES
    from .sources import site_drawings
    if role != 'main':
        return []
    source = source_path({'icon': entry['key']}, role)
    if not source.is_file() or site_drawings().get(entry['key']) != sha(source.read_text()):
        return []
    review = ROLES['main'][0]
    for record in json.loads((review / 'manifest.json').read_text())['records']:
        if (record['name'] == entry['name'] and record['source_sha256'] == site_drawings()[entry['key']]
                and record['kind'] != 'error' and record['review_status'] not in SKIP_STATUSES):
            path = review / record['output']
            return [('current', portable(compact(path.read_text()), is_reverse_fill(path)))] if path.is_file() else []
    return []


def view_box(svg):
    import re
    match = re.search(r'<svg\b[^>]*?\bviewBox="([^"]+)"', svg)
    return [float(n) for n in re.split(r'[\s,]+', match.group(1).strip())] if match else None


def on_canvas(svg, source):
    """The SVG with its viewBox written as its source drawing's (0.0 0.0 32.0 32.0 → 0 0 32 32), or None when the
    fill is drawn on another canvas than its source: a layout places it by the source's coordinates."""
    mine, theirs = view_box(svg), view_box(source)
    if mine is None or theirs is None or mine != theirs:
        return None
    text = ' '.join(f'{v:g}' for v in theirs)
    import re
    return re.sub(r'(<svg\b[^>]*?\bviewBox=")[^"]+(")', lambda m: m.group(1) + text + m.group(2), svg, count=1)


class Everything:
    """Every (source, label): pick_specs then names each pick's own variant, unresolved."""
    def __contains__(self, _item):
        return True


def export():
    from .parts import parts_listing
    combined = {row['id'] for row in json.loads((WORK / 'gallery-data.js').read_text().split('=', 1)[1].rstrip().rstrip(';'))['rows']}
    items = json.loads((DATA / 'data/production-layouts.json').read_text())['items']
    parts = {}
    for item in items:
        for p in item['parts']:
            if p.get('icon'):
                parts.setdefault(p['icon'], p)
    from .adaptive_overlap import source_path
    from .d1_import import pick_specs, rejected_variants
    rejected = rejected_variants()
    needed = {}
    for spec in pick_specs(available=Everything()):
        for chosen in spec['roles'].values():
            needed.setdefault(chosen['source'], set()).add(chosen['label'])
    mains, subs = parts_listing(combined)
    manifest, skipped, off_canvas = [], {}, []
    for role, listing in (('main', mains), ('sub', subs)):
        for entry, _art in listing:
            relayout = site_fill(role, entry) if entry['status'] == 'redrawn' else []
            if entry['status'] not in ('ready', 'outline') and not relayout:
                skipped[entry['status']] = skipped.get(entry['status'], 0) + 1
                continue
            part = parts[entry['key']]
            source = source_path(part, role).read_text()
            revision = sha(source) if relayout else entry['revision']
            for label, svg in relayout or variants_of(role, entry, part, needed.get(entry['key'], set()), rejected):
                svg = on_canvas(svg, source)
                if svg is None:
                    off_canvas.append(f'{entry["key"]} {label}')
                    continue
                path = OUT / role / entry['name'] / f'{label}.svg'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(svg)
                manifest.append({'key': fill_key(entry['key'], label), 'source_key': entry['key'], 'variant': label,
                                 'name': f'{entry["name"]} {label}', 'svg': str(path.relative_to(WORK)),
                                 'svg_sha256': sha(svg), 'source_sha256': revision})
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=1) + '\n')
    counts = {}
    for m in manifest:
        family = m['source_key'].split('/')[0]
        counts[family] = counts.get(family, 0) + 1
    return {'icons': len(manifest), 'by_family': counts, 'skipped_parts': skipped, 'off_canvas': off_canvas,
            'manifest': str(OUT / 'manifest.json')}


def main(argv=None):
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args(argv)
    print(json.dumps(export(), indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
