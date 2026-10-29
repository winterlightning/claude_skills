"""Rework a flat Normal fill into a stroke-keeping SVG: black fill regions plus the original strokes.

Each original stroke element is copied unchanged (path data, caps, joins, width) and painted black where
the existing fill inks it, or white where the fill cuts it out. The black regions are the existing fill's
paint between strokes. Nothing is redrawn: the regions come from the existing fill, the strokes from the
source. Painting order is regions, black strokes, white strokes, so the file renders like the old fill and
can be resized by moving the centerlines and keeping every stroke 4px.
"""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import copy
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from shapely.geometry import LineString, Point, Polygon
from shapely.ops import substring, unary_union
from shapely.prepared import prep
from shapely.validation import make_valid

from .adaptive_overlap import ROOT, fill_path, source_path
from .combine_fill_side import HALF_STROKE, load_fill
from .combine_fill_side_layouts import DEFAULT_LAYOUTS, element_segments, polygons, repo_layout_svg

SVG = 'http://www.w3.org/2000/svg'
OUT = WORK / 'stroke-fill-rework'
STEP = 0.5          # px of centerline per black/white sample
SLIVER = 0.4        # px: paint thinner than twice this between strokes is not a region
MIXED_LENGTH = 1.0  # px of centerline in its minority colour that makes an element mixed (dashed)
ET.register_namespace('', SVG)


class Shape:
    """One drawn source element: its centerline, its filled area, and which of the two it paints."""

    def __init__(self, segments, own, root, element):
        self.segments = segments
        self.element = element
        self.stroked = own.get('stroke', root.get('stroke', 'none')).lower() not in ('none', 'transparent')
        self.filled = own.get('fill', root.get('fill', 'black')).lower() not in ('none', 'transparent')
        self.area = filled_area(element, root) if self.filled else Polygon()
        parts = [LineString(seg) if len(seg) > 1 and LineString(seg).length > 1e-6 else Point(seg[0])
                 for seg in segments if seg]
        self.centerline = unary_union(parts) if parts else Polygon()

    def ink(self, width=2 * HALF_STROKE):
        """What it paints: its round stroke (4px, or its own detail width) and its filled area."""
        stroke = self.centerline.buffer(width / 2) if self.stroked and not self.centerline.is_empty else Polygon()
        return unary_union([stroke, self.area])


def filled_area(element, root):
    """The area one element fills, read with the fill parser (the engine segments only strokes)."""
    import tempfile
    from ...vendor.fill_processing.vendor.fill_utils import parse_all_shapes
    alone = ET.Element(f'{{{SVG}}}svg', {k: v for k, v in root.attrib.items() if k in ('viewBox', 'width', 'height')})
    copied = copy.deepcopy(element)
    copied.set('fill', '#000')
    copied.set('stroke', 'none')
    alone.append(copied)
    with tempfile.NamedTemporaryFile('w', suffix='.svg') as handle:
        handle.write(ET.tostring(alone, encoding='unicode'))
        handle.flush()
        _r, _v, shapes = parse_all_shapes(handle.name, include_fills=True)
    areas = [s['geometry'] for s in shapes if s.get('kind') == 'fill']
    return make_valid(unary_union(areas)) if areas else Polygon()


def shapes_of(cls, root, document):
    return [Shape(segments, own, root, element)
            for segments, (element, own) in zip(element_segments(cls, document), cls.elements(root))]


def subpaths(shape):
    """The element's centerline as continuous runs (an SVG dash pattern restarts on each subpath)."""
    runs, current, seen = [], [], set()
    for seg in shape.segments:
        if len(seg) < 2:
            continue
        key = tuple((round(x, 6), round(y, 6)) for x, y in seg)
        if key in seen:   # the engine repeats an element's segments; one copy is its path
            continue
        seen.add(key)
        if current and (abs(current[-1][0] - seg[0][0]) > 1e-6 or abs(current[-1][1] - seg[0][1]) > 1e-6):
            runs.append(current)
            current = []
        current = current + list(seg[1:] if current else seg)
    if current:
        runs.append(current)
    return [LineString(run) for run in runs if LineString(run).length > 1e-6]


def white_dashes(shape, fill, width):
    """(stroke-dasharray, stroke-dashoffset) painting only the element's white parts, or None.

    Lengths are along the element's own path, so the dash pattern belongs to the unchanged path data.
    A dash that ends where the fill turns black stops a cap radius short, so its round cap ends there.
    Only single-subpath elements can carry one pattern; others return None.
    """
    runs = subpaths(shape)
    if len(runs) != 1:
        return None
    line = runs[0]
    true_length = svg_length(shape.element) or line.length
    covered = prep(fill)
    n = max(1, int(line.length / (STEP / 2)))
    white, start = [], None
    for k in range(n + 1):
        t = k / n
        inked = covered.contains(line.interpolate(t, normalized=True))
        if not inked and start is None:
            start = t
        if (inked or k == n) and start is not None:
            white.append((start, t))
            start = None
    cap = width / 2
    dashes = []
    for a, b in white:
        a, b = a * true_length, b * true_length
        a = a + cap if a > 1e-6 else a
        b = b - cap if b < true_length - 1e-6 else b
        if b - a > .05:
            dashes.append((a, b))
    if not dashes:
        return None
    pattern = []
    for (a, b), following in zip(dashes, dashes[1:] + [None]):
        pattern.append(b - a)
        pattern.append((following[0] - b) if following else (true_length - b) + dashes[0][0] + true_length)
    painted = unary_union([substring(line, a / true_length, b / true_length, normalized=True).buffer(cap)
                           for a, b in dashes])
    return ' '.join(f'{v:.3f}' for v in pattern), f'{-dashes[0][0]:.3f}', painted


def svg_length(element):
    """Rendered length of a <path> (what SVG dashes measure), or None for other elements."""
    if element.tag.split('}')[-1] != 'path' or not element.get('d'):
        return None
    try:
        from svgpathtools import parse_path
        return parse_path(element.get('d')).length()
    except Exception:
        return None


def classify(shapes, fill):
    """[(element index, 'black' | 'white', minority share, minority length)] for each drawn element."""
    covered = prep(fill)
    result = []
    for index, shape in enumerate(shapes):
        black = white = 0.0
        if shape.filled and not shape.stroked:
            # A filled shape (a key, a socket slot) is black or white by its inside.
            if not shape.area.is_empty:
                inked = covered.contains(shape.area.representative_point())
                result.append((index, 'black' if inked else 'white', 0.0, 0.0))
            continue
        for seg in shape.segments:
            if not seg:
                continue
            line = LineString(seg) if len(seg) > 1 else None
            if line is None or line.length < 1e-6:
                # A dot (zero-length path with a round cap) counts once, by its centre.
                if covered.contains(Point(seg[0])):
                    black += STEP
                else:
                    white += STEP
                continue
            n = max(1, int(line.length / STEP))
            for k in range(n):
                part = substring(line, k / n, (k + 1) / n, normalized=True)
                if covered.contains(line.interpolate((k + .5) / n, normalized=True)):
                    black += part.length
                else:
                    white += part.length
        if black + white == 0:
            continue
        colour = 'black' if black >= white else 'white'
        result.append((index, colour, min(black, white) / (black + white), min(black, white)))
    return result


def colours_of(colours):
    return {i: colour for i, colour, *_rest in colours}


def ink(shapes, indices, widths=None):
    """What the chosen elements paint (strokes 4px, or each one's own detail width)."""
    widths = widths or {}
    parts = [shapes[i].ink(widths.get(i, 2 * HALF_STROKE)) for i in indices]
    return unary_union(parts) if parts else Polygon()


DETAIL_LIMIT = 3.6  # px: a white cut narrower than this in the fill keeps its own (detail) width


def cut_width(line, fill):
    """Width of the white cut the fill paints around one white element's centerline.

    The fill may shrink small details (dots, short dashes) below 4px; the width whose round stroke
    matches the white area around the centerline is kept, so the detail scales like the fill drew it.
    """
    white = line.buffer(HALF_STROKE + .2).difference(fill).area
    low, high = .5, 2 * HALF_STROKE
    for _ in range(20):
        mid = (low + high) / 2
        if line.buffer(mid / 2).area < white:
            low = mid
        else:
            high = mid
    return round((low + high) / 2, 1)


TUCK = 1.0         # px from a centerline: regions end this far under each bordering stroke


def regions_of(fill, black_ink, white_ink):
    """The fill's paint between strokes, each edge tucked under its bordering stroke.

    White cut-outs fill back so white strokes paint over them. Every region edge ends TUCK from the
    stroke centerline it meets (under the 4px stroke), so the file renders without seams and a resize
    up to 2x scales the regions as they are: an edge s*TUCK from its moved centerline stays under it.
    """
    # Closing wide enough for junctions where white strokes meet (a $ splitting its box in two); it
    # only ever adds the white stroke band, so empty canvas around the drawing stays empty.
    reach = 2 * HALF_STROKE
    closed = fill.buffer(reach, join_style='round').buffer(-reach, join_style='round')
    inside = closed.union(unary_union([Polygon(p.exterior) for p in polygons(fill)]))
    whole = make_valid(fill.union(white_ink.buffer(.05).intersection(inside)))
    core = whole.difference(black_ink)
    core = core.buffer(-SLIVER, join_style='round').buffer(SLIVER, join_style='round')
    if core.is_empty:
        return core
    reach_under = HALF_STROKE - TUCK
    # White counters (a dot inside a white ring) stay clear by the same margin as black strokes. A
    # counter is only the white inside a hole, not paint nested within it (a socket's inner disc).
    counters = unary_union([Polygon(r) for p in polygons(whole) for r in p.interiors]).difference(whole)
    # Hairline gaps between the fill's outline and a stroke's exact outline are not counters.
    counters = counters.buffer(-SLIVER, join_style='round').buffer(SLIVER, join_style='round')
    region = core.buffer(reach_under, join_style='round').intersection(whole)
    if not counters.is_empty:
        region = region.difference(counters.buffer(reach_under, join_style='round'))
    return make_valid(region)


def path_data(geometry):
    out = []
    for poly in polygons(geometry):
        for ring in [poly.exterior, *poly.interiors]:
            out.append('M' + 'L'.join(f'{x:.4f},{y:.4f}' for x, y in ring.coords[:-1]) + 'Z')
    return ''.join(out)


def drawn_elements(cls, root):
    """The source's drawable elements in the engine's element order (the numbers layouts use), each
    carrying the stroke attributes it inherited from its groups."""
    found = []
    for element, own in cls.elements(root):
        element = copy.deepcopy(element)
        for key, value in own.items():
            if key.startswith('stroke') and key != 'stroke' and key not in element.attrib:
                element.set(key, value)
        found.append(element)
    return found


def inline_styles(document):
    """The source with its stylesheet and style="" declarations written out as plain attributes.

    Elements styled by class (`.st0 {stroke:#000; stroke-width:4px}`) carry their paint as attributes,
    so each copied element paints the same without the <style> block. Path data is unchanged.
    """
    from ...vendor.fill_processing.vendor.fill_utils import _inline_svg_styles
    root = ET.fromstring(document)
    if not list(root.iter(f'{{{SVG}}}style')) and not any('style' in e.attrib for e in root.iter()):
        return document
    _inline_svg_styles(root)
    for parent in root.iter():
        for child in list(parent):
            if child.tag == f'{{{SVG}}}style':
                parent.remove(child)
    for element in root.iter():
        element.attrib.pop('style', None)
        element.attrib.pop('class', None)
        for key in ('stroke-width',):
            if element.get(key, '').endswith('px'):
                element.set(key, element.get(key)[:-2])
    return ET.tostring(root, encoding='unicode')


def rework(source, fill_file):
    """(SVG text, report) for one source drawing and its existing flat fill."""
    cls = repo_layout_svg()
    document = inline_styles(source.read_text())
    fill = load_fill(fill_file)[0]
    root = ET.fromstring(document)
    shapes = shapes_of(cls, root, document)
    colours = classify(shapes, fill)
    black = [i for i, c, *_ in colours if c == 'black']
    white = [i for i, c, *_ in colours if c == 'white']
    widths = {}
    for i in white:
        if not shapes[i].stroked or shapes[i].filled:
            continue
        width = cut_width(shapes[i].centerline, fill)
        if width < DETAIL_LIMIT:
            widths[i] = width
    # An element the fill paints partly white (a globe's centre line drawn with its rim, a line that
    # ends in a filled area) also gets a white copy of itself, dashed to its white parts only.
    dashed, under = {}, []
    for i, colour, share, minority in colours:
        if minority < MIXED_LENGTH or not shapes[i].stroked:
            continue
        found = white_dashes(shapes[i], fill, widths.get(i, 2 * HALF_STROKE))
        if found:
            dashed[i] = found
        elif colour == 'white':
            under.append(i)   # several subpaths: black strokes cover its black part where they can
    over = [i for i in white if i not in dashed and i not in under]
    black_ink = ink(shapes, black)
    dashed_ink = unary_union([painted for _p, _o, painted in dashed.values()]) if dashed else Polygon()
    white_ink = unary_union([ink(shapes, over + under, widths), dashed_ink])
    regions = regions_of(fill, black_ink, white_ink)

    out = ET.Element(f'{{{SVG}}}svg', {k: v for k, v in root.attrib.items()
                                        if k in ('width', 'height', 'viewBox')})
    out.set('data-format', 'stroke-fill/v1')
    for title in root.findall(f'{{{SVG}}}title'):
        out.append(copy.deepcopy(title))
    if not regions.is_empty:
        ET.SubElement(out, f'{{{SVG}}}path', {'id': 'fill-regions', 'd': path_data(regions),
                                             'fill': '#000', 'fill-rule': 'evenodd', 'stroke': 'none'})
    stroke_attrs = {k: v for k, v in root.attrib.items()
                    if k.startswith('stroke') and k != 'stroke'}
    elements = drawn_elements(cls, root)
    dashed_white = [i for i in dashed if colours_of(colours)[i] == 'white']
    for name, indices, paint in (('white-strokes-under', under, '#fff'), ('black-strokes', black, '#000'),
                                 ('white-strokes', over + list(dashed), '#fff')):
        if not indices:
            continue
        group = ET.SubElement(out, f'{{{SVG}}}g', {'id': name, 'fill': 'none', 'stroke': paint, **stroke_attrs})
        for i in indices:
            element = copy.deepcopy(elements[i])
            # Paint as the source did: a stroke takes the group colour, a filled shape is filled with it.
            if shapes[i].stroked:
                element.attrib.pop('stroke', None)
            else:
                element.set('stroke', 'none')
            element.set('fill', paint if shapes[i].filled and i not in dashed else 'none')
            element.set('data-element', str(i))
            if i in widths:
                element.set('stroke-width', f'{widths[i]:g}')
                element.set('data-detail-width', 'true')
            if paint == '#fff' and i in dashed:
                element.set('stroke-dasharray', dashed[i][0])
                element.set('stroke-dashoffset', dashed[i][1])
                element.set('data-white-parts', 'true')
            group.append(element)
    text = ET.tostring(out, encoding='unicode')

    rendered = make_valid(regions.difference(ink(shapes, under, widths)).union(black_ink)
                          .difference(unary_union([ink(shapes, over, widths), dashed_ink])))
    report = {'black_elements': black, 'white_elements': white, 'white_under_black': under,
              'white_dashed': list(dashed), 'white_dashed_only': dashed_white,
              'detail_widths': {str(i): w for i, w in widths.items()},
              'mixed_elements': [{'element': i, 'minority_share': round(share, 3)}
                                 for i, _c, share, minority in colours if minority >= MIXED_LENGTH],
              'difference_from_fill_px2': round(rendered.symmetric_difference(fill).area, 2),
              'fill_area_px2': round(fill.area, 2)}
    return text, report


def targets(names=None):
    """{(role, icon key): part} for every main and sub the production layouts use."""
    found = {}
    for item in json.loads(DEFAULT_LAYOUTS.read_text())['items']:
        for part in item['parts']:
            if part.get('icon'):
                key = (part['role'], part['icon'])
                if (names is None or part['icon'].split('/', 1)[1] in names) and key not in found:
                    found[key] = part
    return found


def output_path(part, role):
    name = part['icon'].split('/', 1)[1]
    if role == 'main':
        return OUT / 'main' / f'{name}.svg'
    return OUT / 'sub' / name / f"{part.get('current_sha') or part['built_sha']}.svg"


def rework_review(review):
    """Rework every fill-only output of a region-fill review folder into <review>-stroke-fill/svg.

    Outputs that already keep their strokes (unchanged, retained originals) are copied as they are.
    The review folder itself is not changed.
    """
    import hashlib
    import shutil
    manifest = json.loads((review / 'manifest.json').read_text())
    out = review.parent / f'{review.name}-stroke-fill'
    (out / 'svg').mkdir(parents=True, exist_ok=True)
    records = []
    for record in manifest['records']:
        name, draft = record['name'], review / record['output']
        source = Path(record['source'])
        target = out / 'svg' / f'{name}.svg'
        row = {'name': name, 'review_status': record.get('status'), 'source': str(source),
               'source_sha256': record.get('source_sha256_at_run'), 'output': f'svg/{name}.svg'}
        try:
            if not draft.is_file() or not source.is_file():
                raise ValueError('missing source or review output')
            if hashlib.sha256(source.read_bytes()).hexdigest() != record.get('source_sha256_at_run'):
                raise ValueError('source changed since the review ran')
            kept = reverse_fill(record, manifest, draft)
            loaded = parse_kinds(draft)
            if kept is not None:
                # Reverse fills (solid material with source lines cut through it) are not 4px strokes
                # over regions; they stay exactly as they are.
                shutil.copy2(kept, target)
                row.update(kind='kept (reverse fill)', kept_from=str(kept))
            elif loaded == 'fill only':
                text, info = rework(source, draft)
                target.write_text(text)
                row.update(info, kind='reworked')
            else:
                shutil.copy2(draft, target)
                row['kind'] = f'copied ({loaded})'
        except Exception as error:  # one bad drawing must not stop the batch
            row.update(kind='error', error=repr(error)[:300])
            target.unlink(missing_ok=True)
        if row['kind'] != 'error' and 'proposal_output' in record:
            row['variants'] = rework_variants(record, review, out, source)
        records.append(row)
        print(f"{name:60} {row['kind']:24} {row.get('difference_from_fill_px2', '')}")
    summary = {
        'schema': 'stroke-fill-rework/v1', 'review': str(review), 'method': __doc__.strip().splitlines()[0],
        'counts': {kind: sum(r['kind'] == kind for r in records) for kind in sorted({r['kind'] for r in records})},
        'records': records}
    (out / 'manifest.json').write_text(json.dumps(summary, indent=2) + '\n')
    write_index(out, review, records)
    print(json.dumps(summary['counts'], indent=2), f'\nmanifest {out / "manifest.json"}')


def write_index(out, review, records):
    """A static side-by-side page: source, old flat fill, reworked stroke-fill (largest change first)."""
    from html import escape
    order = sorted(records, key=lambda r: (r['kind'] != 'error', -(r.get('difference_from_fill_px2') or 0)))
    cards = []
    for r in order:
        name = escape(r['name'])
        diff = r.get('difference_from_fill_px2')
        flags = []
        if r.get('white_dashed'):
            flags.append('white parts dashed')
        if r.get('detail_widths'):
            flags.append('detail widths ' + ', '.join(f'{w}px' for w in r['detail_widths'].values()))
        if r.get('white_under_black'):
            flags.append('white under black')
        note = escape(r.get('error', '')) if r['kind'] == 'error' else escape(' · '.join(flags))
        cls = 'bad' if r['kind'] == 'error' or (diff or 0) >= 10 else 'warn' if (diff or 0) >= 3 else ''
        old = f'../{review.name}/{r["output"]}'
        new = '' if r['kind'] == 'error' else f'<img src="{escape(r["output"])}" alt="">'
        cards.append(
            f'<article class="{cls}" data-diff="{diff or 0}"><h2>{name}</h2>'
            f'<div class="row"><img src="{escape(old)}" alt="">{new}</div>'
            f'<p>{escape(r["kind"])}{f" · {diff} px²" if diff is not None else ""}</p><p>{note}</p></article>')
    counts = ' · '.join(f'{escape(k)} {sum(r["kind"] == k for r in records)}' for k in sorted({r['kind'] for r in records}))
    (out / 'index.html').write_text(f'''<!doctype html><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Stroke-fill rework</title>
<style>
body{{margin:0;padding:16px;font:13px system-ui;background:#f4f5f7;color:#1b2430}}
header{{position:sticky;top:0;background:#f4f5f7;padding:6px 0 10px}} h1{{font-size:18px;margin:0 0 4px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}}
article{{background:#fff;border:1px solid #d8dde4;border-radius:10px;padding:8px}}
article.warn{{border-color:#d8a23a}} article.bad{{border:2px solid #c2412d}}
h2{{font-size:12px;margin:0 0 6px;word-break:break-all}} p{{margin:4px 0 0;color:#5a6575}}
.row{{display:grid;grid-template-columns:repeat(2,1fr);gap:4px}} .row img{{width:100%;aspect-ratio:1;background:#fff;border:1px solid #eef0f3}}
label{{margin-left:12px}}
</style>
<header><h1>Stroke-fill rework · {escape(review.name)}</h1>
<div>Each card: old flat fill · reworked file (original strokes painted black/white over black fill regions).
Largest change first. {counts}<label><input type="checkbox" id="only"> only changes ≥ 3 px²</label></div></header>
<div class="grid" id="grid">{"".join(cards)}</div>
<script>document.getElementById('only').addEventListener('change',e=>{{for(const a of document.querySelectorAll('article'))
a.hidden=e.target.checked&&Number(a.dataset.diff)<3&&!a.classList.contains('bad');}});</script>
''')


REVERSE_DIFF = 10.0   # px²: a fill this far from any 4px-stroke rendering is a reverse fill


def offered_variants(record, review):
    """(identifier, file) for every variant the main review still offers (not removed by the user)."""
    removed = set(record.get('removed_variants', []))
    preserved = Path(json.loads((review / 'manifest.json').read_text()).get('preserved_fill_folder', ''))
    found = [('script', review / record['proposal_output'])]
    found += [(f'script:{item["variant"]}', review / item['path']) for item in record.get('script_variants', [])]
    current = record.get('current_fill')
    if current and not current.get('duplicate_of'):
        found.append(('current', preserved / current['path']))
    found += [(f'approved:{item["variant"]}', preserved / item['path'])
              for item in record.get('approved_alternates', [])
              if not item.get('duplicate_of') and item.get('inventory_source_sha256') == record['source_sha256_at_run']]
    return [(identifier, path) for identifier, path in found if identifier not in removed]


def rework_variants(record, review, out, source):
    """Stroke versions of every offered main variant, in <out>/variants/<name>/<identifier>.svg.

    Retained icons offer only their original. A variant whose decision cuts source strokes, or that no
    4px-stroke rendering matches (white parts dashed, or REVERSE_DIFF away), is a reverse fill: kept as is.
    """
    import shutil
    if retained_by_user(record):
        return []
    decisions = DATA / 'data/main48-region-fill-review-decisions.json'
    decided = json.loads(decisions.read_text())['decisions'].get(record['name'], {}) if decisions.exists() else {}
    rows = []
    for identifier, path in offered_variants(record, review):
        target = out / 'variants' / record['name'] / (identifier.replace(':', '--') + '.svg')
        target.parent.mkdir(parents=True, exist_ok=True)
        row = {'variant': identifier, 'output': str(target.relative_to(out)), 'from': str(path)}
        try:
            decision = (decided if identifier == 'script' else
                        decided.get('variants', {}).get(identifier.split(':', 1)[1], {}) if identifier.startswith('script:') else {})
            kind = parse_kinds(path)
            if decision.get('cut_source_strokes') or decision.get('extend_source_stroke_cuts'):
                shutil.copy2(path, target)
                row['kind'] = 'kept (reverse fill)'
            elif kind != 'fill only':
                shutil.copy2(path, target)
                row['kind'] = f'copied ({kind})'
            else:
                text, info = rework(source, path)
                if info['white_dashed'] or info['difference_from_fill_px2'] >= REVERSE_DIFF:
                    shutil.copy2(path, target)
                    row.update(kind='kept (reverse fill)', difference_from_fill_px2=info['difference_from_fill_px2'])
                else:
                    target.write_text(text)
                    row.update(info, kind='reworked')
        except Exception as error:  # one bad variant must not stop the batch
            target.unlink(missing_ok=True)
            row.update(kind='error', error=repr(error)[:300])
        rows.append(row)
    return rows


def reverse_fill(record, manifest, draft):
    """The fill file to keep as it is when the review used a reverse fill, else None.

    Sub reviews mark reverse fills by cutting source strokes through the filled material
    (cut_source_strokes / extend_source_stroke_cuts). Main reviews mark them by keeping the existing fill
    (selected_kind "original"), which lives in the preserved fill folder.
    """
    if record.get('cut_source_strokes') or record.get('extend_source_stroke_cuts'):
        return draft
    current = record.get('current_fill') or {}
    if retained_by_user(record):
        return None   # "Retain original": the plain source drawing, not a fill
    if record.get('selected_kind') == 'original' and current.get('path') and manifest.get('preserved_fill_folder'):
        path = Path(manifest['preserved_fill_folder']) / current['path']
        return path if path.is_file() else None
    return None


def retained_by_user(record):
    """Whether the main review user marked this icon "Retain original" (its source, unfilled)."""
    marks = DATA / 'data/main48-user-review-marks.json'
    if not marks.exists():
        return False
    mark = json.loads(marks.read_text()).get('marks', {}).get(record['name'], {})
    return mark.get('action') == 'retain' and mark.get('source_sha256') == record.get('source_sha256_at_run')


def parse_kinds(path):
    """'fill only' | 'strokes only' | 'strokes + fill' for an SVG's painted elements."""
    from ...vendor.fill_processing.vendor.fill_utils import parse_all_shapes
    _root, _viewbox, shapes = parse_all_shapes(str(path), include_fills=True)
    fills = any(s.get('kind') == 'fill' for s in shapes)
    strokes = any(s.get('kind') != 'fill' for s in shapes)
    return 'strokes + fill' if fills and strokes else 'fill only' if fills else 'strokes only'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('names', nargs='*', help='icon names (default: every main and sub in the layouts)')
    parser.add_argument('--review', type=Path, help='a region-fill review folder to rework as a whole')
    args = parser.parse_args()
    if args.review:
        rework_review(args.review.resolve())
        return
    report = {}
    for (role, key), part in sorted(targets(set(args.names) or None).items()):
        source, fill_file = source_path(part, role), fill_path(part, role)
        if not source.is_file() or not fill_file.is_file():
            report[key] = {'error': 'missing source or fill'}
            continue
        try:
            text, info = rework(source, fill_file)
        except Exception as error:  # one bad drawing must not stop the batch
            report[key] = {'error': repr(error)[:300]}
            continue
        out = output_path(part, role)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        report[key] = {**info, 'role': role, 'source': str(source.relative_to(DATA)),
                       'fill': str(fill_file.relative_to(DATA)), 'output': str(out.relative_to(WORK))}
        print(f"{key:60} diff {info['difference_from_fill_px2']:7.2f}px²  black {len(info['black_elements'])}"
              f"  white {len(info['white_elements'])}  mixed {len(info['mixed_elements'])}")
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / ('report.json' if not args.names else 'pilot-report.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(f'report {path}')


if __name__ == '__main__':
    main()
