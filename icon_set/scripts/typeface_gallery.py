"""Publish the independently authored natural-proportion lettering collection."""
import json
from pathlib import Path


def export_glyphs(exports: Path, payload: dict) -> None:
    """Write one stroked SVG per glyph, plus the catalog as a manifest."""
    from xml.sax.saxutils import quoteattr, escape
    exports.mkdir(exist_ok=True)
    manifest = exports/'manifest.json'
    previous = json.loads(manifest.read_text()).get('glyphs', []) if manifest.exists() else []
    current_ids = {g['icon_id'] for g in payload['glyphs']}
    for glyph in previous:
        uid = glyph['icon_id']
        if uid not in current_ids and Path(uid).name == uid:
            (exports/(uid+'.svg')).unlink(missing_ok=True)
    for glyph in payload['glyphs']:
        view_box = ' '.join(str(v) for v in glyph['preview_box'])
        paths = ''.join('<path d='+quoteattr(d)+'/>' for d in glyph['paths'])
        document = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{glyph["canvas_width"]}" height="{glyph.get("canvas_height", 24)}" '
                    'viewBox='+quoteattr(view_box)+' fill="none" stroke="currentColor" '
                    f'stroke-width="{glyph["stroke_width"]}" stroke-linecap="round" stroke-linejoin="round">'
                    '<title>'+escape(glyph['character'])+'</title>'+paths+'</svg>')
        (exports/(glyph['icon_id']+'.svg')).write_text(document+'\n')
    (exports/'manifest.json').write_text(json.dumps(payload, indent=2)+'\n')


def stage_typeface(target: Path, records: list[dict], registered: dict) -> None:
    # Lettering is now its own geometry collection, independent of SOLO48
    # validation/export and its fixed keyshapes. Keep the call signature for
    # gallery build integration; records do not override this reviewed data.
    source = Path(__file__).resolve().parents[1] / 'typeface/glyphs.json'
    payload = json.loads(source.read_text())
    glyphs = payload['glyphs']
    if payload.get('geometry_policy') != 'fixed-centerline-6x20':
        raise ValueError('Typeface requires fixed 6x20 centerline geometry')
    if len({g['icon_id'] for g in glyphs}) != len(glyphs):
        raise ValueError('Duplicate typeface glyph')
    import hashlib
    for glyph in glyphs:
        digest = hashlib.sha256(json.dumps(glyph['paths'], separators=(',', ':')).encode()).hexdigest()
        if digest != glyph['svg_sha256']:
            raise ValueError('Typeface path digest mismatch: '+glyph['icon_id'])
    payload['coordinates'] = 'centerline'
    templates = Path(__file__).with_name('templates')
    data = json.dumps(payload, ensure_ascii=True).replace('<', '\\u003c')
    (target/'typeface.json').write_text(json.dumps(payload, indent=2)+'\n')
    exports = target/'typeface'
    export_glyphs(exports, payload)
    from .typeface_sizes import stage_sizes
    stage_sizes(exports/'sizes', glyphs)

    # v2: natural-width uppercase from Letters/UPPER; the browser uppercases
    # text and falls back to v1 for characters v2 does not draw.
    v2_source = source.with_name('glyphs-v2.json')
    v2 = json.loads(v2_source.read_text())
    if v2.get('geometry_policy') != 'natural-centerline-28x32':
        raise ValueError('Typeface v2 requires the drawn 28-unit centerline on 32-unit ink')
    if len({g['icon_id'] for g in v2['glyphs']}) != len(v2['glyphs']):
        raise ValueError('Duplicate typeface v2 glyph')
    for glyph in v2['glyphs']:
        digest = hashlib.sha256(json.dumps(glyph['paths'], separators=(',', ':')).encode()).hexdigest()
        if digest != glyph['svg_sha256']:
            raise ValueError('Typeface v2 path digest mismatch: '+glyph['icon_id'])
    v2['coordinates'] = 'centerline'
    v2_data = json.dumps(v2, ensure_ascii=True).replace('<', '\\u003c')
    (target/'typeface-v2.json').write_text(json.dumps(v2, indent=2)+'\n')
    export_glyphs(target/'typeface-v2', v2)

    html = (templates/'text-combine.html').read_text()
    html = html.replace('__TYPEFACE_DATA__', data).replace('__TYPEFACE_V2_DATA__', v2_data)
    html = html.replace('__TYPEFACE_SCRIPT__', (templates/'text-combine.js').read_text())
    (target/'text-combine.html').write_text(html)

    # The text family uses these same glyphs, with a fixed-height canvas.
    (target/'text-icons.html').write_text((templates/'text-icons.html').read_text())
    spec = source.parents[1] / 'data/container-text-icons.json'
    pending = json.loads(spec.read_text()).get('unresolved', []) if spec.exists() else []
    (target/'text-unresolved.json').write_text(json.dumps(pending, indent=2)+'\n')
