"""Publish the independently authored natural-proportion lettering collection."""
import json
from pathlib import Path


def stage_typeface(target: Path, records: list[dict], registered: dict) -> None:
    # Lettering is now its own geometry collection, independent of SOLO48
    # validation/export and its fixed keyshapes. Keep the call signature for
    # gallery build integration; records do not override this reviewed data.
    source = Path(__file__).resolve().parents[1] / 'typeface/glyphs.json'
    payload = json.loads(source.read_text())
    glyphs = payload['glyphs']
    if payload.get('geometry_policy') != 'natural-proportions-no-keyshape':
        raise ValueError('Typeface requires natural lettering geometry')
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
    from xml.sax.saxutils import quoteattr, escape
    exports = target/'typeface'
    exports.mkdir(exist_ok=True)
    for glyph in glyphs:
        view_box = ' '.join(str(v) for v in glyph['preview_box'])
        paths = ''.join('<path d='+quoteattr(d)+'/>' for d in glyph['paths'])
        document = ('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" '
                    'viewBox='+quoteattr(view_box)+' fill="none" stroke="currentColor" '
                    'stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
                    '<title>'+escape(glyph['character'])+'</title>'+paths+'</svg>')
        (exports/(glyph['icon_id']+'.svg')).write_text(document+'\n')
    (exports/'manifest.json').write_text(json.dumps(payload, indent=2)+'\n')

    html = (templates/'text-combine.html').read_text()
    html = html.replace('__TYPEFACE_DATA__', data)
    html = html.replace('__TYPEFACE_SCRIPT__', (templates/'text-combine.js').read_text())
    (target/'text-combine.html').write_text(html)
