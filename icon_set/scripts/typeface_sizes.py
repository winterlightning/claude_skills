"""Export only the fixed 6 × 20 centerline typeface."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr
from zipfile import ZipFile, ZIP_DEFLATED


from .workspace import DEFAULT_DIST, REPO_ROOT, output_lock

HEIGHTS = (24,)


def size_record(glyph, height):
    if type(height) is not int or height != 24:
        raise ValueError('Only the fixed 6x20 centerline size (10x24 canvas) is supported')
    if glyph.get('geometry_policy') != 'fixed-centerline-6x20':
        raise ValueError('Rebuild the fixed-size base catalog first')
    return dict(width=glyph['canvas_width'], height=24, stroke_width=4,
                centerline_width=glyph['centerline_width'],
                centerline_height=glyph['centerline_height'],
                ink_width=glyph['ink_width'], ink_height=glyph['ink_height'],
                ink_left=glyph['ink_left'], ink_top=glyph['ink_top'],
                file=f"24/{glyph['icon_id']}.svg")


def sized_paths(glyph, height):
    size_record(glyph, height)
    return list(glyph['paths'])


def sized_svg(glyph, height):
    size = size_record(glyph, height)
    paths = ''.join('<path d=' + quoteattr(d) + '/>' for d in glyph['paths'])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size["width"]}" height="24" '
            f'viewBox="0 0 {size["width"]} 24" role="img" aria-label='+quoteattr(glyph['character'])+'>'
            '<title>'+escape(glyph['character'])+'</title>'
            '<g fill="none" stroke="currentColor" stroke-width="4" '
            'stroke-linecap="round" stroke-linejoin="round">'+paths+'</g></svg>\n')


def stage_sizes(target, glyphs):
    """Stage disposable exports beneath a caller-owned, locked output folder."""
    target = Path(target)
    target.mkdir(parents=True, exist_ok=True)
    previous_manifest = target/'manifest.json'
    previous = json.loads(previous_manifest.read_text()).get('glyphs', []) if previous_manifest.exists() else []
    current_ids = {g['icon_id'] for g in glyphs}
    for glyph in previous:
        uid = glyph['icon_id']
        if uid not in current_ids and Path(uid).name == uid:
            (target/'24'/(uid+'.svg')).unlink(missing_ok=True)
    manifest = {'schema_version': 4, 'base_height': 24, 'heights': [24],
                'centerline_box': [6,20], 'canvas': [10,24],
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
    with ZipFile(target / 'typeface-6x20.zip', 'w', ZIP_DEFLATED) as archive:
        for name in ('manifest.json', 'index.html'):
            archive.write(target / name, name)
        for entry in manifest['glyphs']:
            for size in entry['sizes']:
                archive.write(target / size['file'], size['file'])
    # Retire only the known derived size range after the replacement is ready.
    retired = [target/str(h) for h in range(12,33) if h != 24]
    retired.append(target/'typeface-12-to-32.zip')
    for path in retired:
        if path.is_dir():
            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()
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
