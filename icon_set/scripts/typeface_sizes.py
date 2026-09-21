"""Export every whole-unit typeface height from 12 through 32."""
import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr
from zipfile import ZipFile, ZIP_DEFLATED

from svgpathtools import Arc, Path as SVGPath, parse_path

from .workspace import DEFAULT_DIST, REPO_ROOT, output_lock

HEIGHTS = tuple(range(12, 33))


def size_record(glyph, height):
    if type(height) is not int or height not in HEIGHTS:
        raise ValueError('Typeface height must be an integer from 12 through 32')
    if glyph.get('ink_height') != 24 or glyph.get('geometry_policy') != 'grid-ink-height24':
        raise ValueError('Typeface sizes require the approved 24-unit base')
    # Round the proportional width to the nearest multiple of 2.
    # Exact odd-unit ties go upward (e.g. 9 -> 10).
    width = 2 * ((glyph['ink_width'] * height + 24) // 48)
    left, top, right, bottom = glyph['bounds']
    path_width, path_height = right-left, bottom-top
    # A point or vertical centerline is exactly one stroke wide at every size.
    width = max(4, width) if path_width > 1e-9 else 4
    ink_height = height if path_height > 1e-9 else 4
    sx = (width-4)/path_width if path_width > 1e-9 else 1
    sy = (ink_height-4)/path_height if path_height > 1e-9 else 1
    return {
        'width': width, 'height': height, 'scale_x': sx, 'scale_y': sy,
        'stroke_width': 4, 'stroke_width_x': 4, 'stroke_width_y': 4,
        'ink_width': width, 'ink_height': ink_height,
        'ink_top': (height-ink_height)/2,
        'file': f'{height}/{glyph["icon_id"]}.svg',
    }


def sized_paths(glyph, height):
    size = size_record(glyph, height)
    sx, sy = size['scale_x'], size['scale_y']
    left, top, _, _ = glyph['bounds']
    offset = complex(2-left*sx, size['ink_top']+2-top*sy)
    def point(p):
        return complex(p.real*sx, p.imag*sy)
    paths = []
    for d in glyph['paths']:
        segments = []
        for segment in parse_path(d):
            if isinstance(segment, Arc):
                if segment.rotation % 180:
                    raise ValueError('Size fitting requires an axis-aligned ellipse')
                segment = Arc(point(segment.start), point(segment.radius),
                              segment.rotation, segment.large_arc, segment.sweep,
                              point(segment.end))
            else:
                segment = segment.scaled(sx, sy)
            segments.append(segment.translated(offset))
        paths.append(SVGPath(*segments).d())
    return paths


def sized_svg(glyph, height):
    size = size_record(glyph, height)
    paths = ''.join('<path d=' + quoteattr(d) + '/>' for d in sized_paths(glyph, height))
    # Bake the transform into centerlines, so every stroke and round cap is 4
    # units wide in final coordinates, regardless of horizontal fitting.
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size["width"]}" '
        f'height="{height}" viewBox="0 0 {size["width"]} {height}" '
        f'role="img" aria-label={quoteattr(glyph["character"])}>'
        f'<title>{escape(glyph["character"])}</title>'
        f'<g fill="none" stroke="currentColor" stroke-width="4" '
        f'stroke-linecap="round" stroke-linejoin="round">{paths}</g></svg>\n'
    )


def stage_sizes(target, glyphs):
    """Stage disposable exports beneath a caller-owned, locked output folder."""
    target = Path(target)
    target.mkdir(parents=True, exist_ok=True)
    manifest = {'schema_version': 3, 'base_height': 24, 'heights': list(HEIGHTS),
                'rounding': 'nearest-multiple-of-2-half-up', 'width_grid': 2,
                'stroke_policy': 'constant-4-final-units', 'glyphs': []}
    for height in HEIGHTS:
        (target / str(height)).mkdir(exist_ok=True)
    for glyph in glyphs:
        entry = {key: glyph[key] for key in ('icon_id', 'character', 'kind', 'preferred')}
        entry.update(base_width=glyph['ink_width'], base_sha256=glyph['svg_sha256'], sizes=[])
        for height in HEIGHTS:
            record = size_record(glyph, height)
            document = sized_svg(glyph, height)
            (target / record['file']).write_text(document)
            record['svg_sha256'] = hashlib.sha256(document.encode()).hexdigest()
            entry['sizes'].append(record)
        manifest['glyphs'].append(entry)
    (target / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    template = Path(__file__).with_name('templates') / 'typeface-sizes.html'
    embedded = json.dumps(manifest, ensure_ascii=True).replace('<', '\\u003c')
    (target / 'index.html').write_text(template.read_text().replace('__SIZE_DATA__', embedded))
    # Include the manifest, offline viewer, and exactly the current exports.
    with ZipFile(target / 'typeface-12-to-32.zip', 'w', ZIP_DEFLATED) as archive:
        for name in ('manifest.json', 'index.html'):
            archive.write(target / name, name)
        for entry in manifest['glyphs']:
            for size in entry['sizes']:
                archive.write(target / size['file'], size['file'])
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    # A dedicated command publishes only these derived sizes in development.
    with output_lock(DEFAULT_DIST):
        if (DEFAULT_DIST / 'release.json').exists():
            raise ValueError('Cannot generate typeface sizes into a production release')
        data = json.loads((REPO_ROOT / 'icon_set/typeface/glyphs.json').read_text())
        target = DEFAULT_DIST / 'gallery/typeface/sizes'
        result = stage_sizes(target, data['glyphs'])
    print(f'Exported {len(result["glyphs"]) * len(HEIGHTS)} SVGs: {target}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
