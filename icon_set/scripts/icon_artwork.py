"""Persistent artwork choices shared by the gallery and Python release builder.

Authored Python remains the baseline. Manual SVGs and accepted graph snapshots
are independent inputs; no generated source code is rewritten by an upload.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

if __package__:
    from .stroke_edits import StrokeEditStore, EditConflict, GRAPH_FIELDS, effective_validation_status
    from .edit_validation import icon_from_graph
else:
    from stroke_edits import StrokeEditStore, EditConflict, GRAPH_FIELDS, effective_validation_status
    from edit_validation import icon_from_graph

DEFAULT_ARTWORK = Path(__file__).resolve().parents[1] / 'data/icon-artwork'
MODES = ('use_org', 'use_upload', 'use_edited')
SVG_NS = 'http://www.w3.org/2000/svg'
MAX_SVG = 1024 * 1024
ET.register_namespace('', SVG_NS)


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def baseline(record):
    result = dict(record)
    result.update(record.get('generated_graph') or {})
    result['svg_sha256'] = record.get('generated_svg_sha256', record['svg_sha256'])
    return result


def safe_svg(text, canvas):
    """Accept portable vector SVGs; disallow active content and remote resources."""
    if not isinstance(text, str) or not text.strip() or len(text.encode('utf-8')) > MAX_SVG:
        raise ValueError('Choose an SVG file up to 1 MB.')
    if re.search(r'<!(DOCTYPE|ENTITY)', text, re.I):
        raise ValueError('Export SVG without a DOCTYPE or entity declarations.')
    try:
        root = ET.fromstring(text)
    except ET.ParseError as error:
        raise ValueError('This file is not valid SVG.') from error
    if root.tag not in ('svg', '{'+SVG_NS+'}svg'):
        raise ValueError('Choose an SVG file.')
    try:
        view = [float(n) for n in re.split(r'[\s,]+', root.get('viewBox', '').strip())]
    except ValueError:
        view = []
    if view != [0, 0, canvas, canvas]:
        raise ValueError(f'Export with a 0 0 {canvas} {canvas} viewBox to keep the icon on its profile canvas.')
    tags = {'svg', 'g', 'path', 'rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon',
            'defs', 'clipPath', 'mask', 'linearGradient', 'radialGradient', 'stop', 'use', 'title', 'desc', 'style'}
    paint = {'fill', 'fill-rule', 'fill-opacity', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin',
             'stroke-miterlimit', 'stroke-dasharray', 'stroke-dashoffset', 'stroke-opacity', 'opacity',
             'clip-path', 'clip-rule', 'mask', 'color', 'stop-color', 'stop-opacity', 'display', 'visibility'}
    attrs = paint | {'id', 'class', 'd', 'points', 'transform', 'viewBox', 'width', 'height', 'x', 'y',
                     'x1', 'x2', 'y1', 'y2', 'cx', 'cy', 'r', 'rx', 'ry', 'fx', 'fy', 'offset',
                     'gradientUnits', 'gradientTransform', 'spreadMethod', 'clipPathUnits', 'maskUnits',
                     'maskContentUnits', 'preserveAspectRatio', 'version', 'vector-effect'}
    def value_ok(value):
        # Backslash escapes and comments must not conceal a URL or CSS function.
        if re.search(r'[\\<>]|/\*|@', value):
            return False
        clean = re.sub(r'url\(\s*[\'\"]?#[a-zA-Z_][\w:.-]*[\'\"]?\s*\)', '', value, flags=re.I)
        return not re.search(r'url\s*\(|expression\s*\(|javascript:|data:|https?:|file:', clean, re.I)
    def declarations(css):
        pairs = []
        for declaration in css.split(';'):
            if not declaration.strip():
                continue
            if ':' not in declaration:
                raise ValueError('Unsupported SVG styling. Export with inline presentation attributes.')
            key, value = (s.strip() for s in declaration.split(':', 1))
            if key not in paint or not value_ok(value):
                raise ValueError('Unsupported SVG styling. Export vector paths with fill and stroke styles.')
            pairs.append(f'{key}:{value}')
        return ';'.join(pairs)
    count = 0
    for node in root.iter():
        count += 1
        if count > 10000:
            raise ValueError('SVG is too complex; simplify it before uploading.')
        tag = node.tag.rsplit('}', 1)[-1]
        if tag not in tags or (node.tag.startswith('{') and not node.tag.startswith('{'+SVG_NS+'}')):
            raise ValueError(f'Unsupported SVG element: {tag}. Export text as outlines and use vector shapes.')
        if tag == 'style':
            css = re.sub(r'/\*.*?\*/', '', node.text or '', flags=re.S)
            blocks = re.findall(r'([^{}]+)\{([^{}]*)\}', css)
            if re.sub(r'[^{}]+\{[^{}]*\}', '', css).strip():
                raise ValueError('Unsupported SVG stylesheet. Export with inline styles.')
            output = []
            for selector, body in blocks:
                if not re.fullmatch(r'[\w.#,\s>+-]+', selector):
                    raise ValueError('Unsupported SVG selector. Export with inline styles.')
                output.append(selector+'{'+declarations(body)+'}')
            node.text = '\n'.join(output)
        for key, value in list(node.attrib.items()):
            if key == 'style':
                node.set(key, declarations(value))
            elif key in ('href', '{http://www.w3.org/1999/xlink}href'):
                if not re.fullmatch(r'#[a-zA-Z_][\w:.-]*', value):
                    raise ValueError('SVG references must stay inside this file.')
            elif key.startswith('{') or key.startswith('data-') or key.startswith('aria-'):
                # Editor metadata does not affect rendered geometry.
                del node.attrib[key]
            elif key not in attrs or not value_ok(value):
                raise ValueError(f'Unsupported SVG attribute: {key}. Export a static vector SVG.')
    root.set('width', str(canvas)); root.set('height', str(canvas))
    # Bare SVG input still needs a namespace when downloaded or rasterized.
    if root.tag == 'svg':
        root.set('xmlns', SVG_NS)
    document = ET.tostring(root, encoding='unicode')+'\n'
    try:
        import cairosvg
        from PIL import Image
        png = cairosvg.svg2png(bytestring=document.encode(), output_width=canvas*2, output_height=canvas*2)
        with Image.open(io.BytesIO(png)) as image:
            if not image.convert('RGBA').getchannel('A').getbbox():
                raise ValueError('SVG contains no visible artwork.')
    except ImportError:
        raise
    except Exception as error:
        raise ValueError('SVG could not be rendered: '+str(error)) from error
    return document


class ArtworkStore(StrokeEditStore):
    def get(self, key):
        path = self.folder(key) / 'artwork.json'
        if not path.is_file():
            return None
        document = json.loads(path.read_text(encoding='utf-8'))
        if document.get('schema') != 'pictographic.icon-artwork.v1' or document.get('icon') != key:
            raise ValueError('Invalid saved artwork record.')
        return document

    def save(self, icon, data, user, edits):
        icon = baseline(icon)
        if data.get('svg_sha256') != icon['svg_sha256']:
            raise EditConflict('The generated icon changed. Reload before changing its artwork.')
        mode = data.get('source_mode')
        if mode not in MODES:
            raise ValueError('Choose original, uploaded, or gallery-edited artwork.')
        key = icon['key']
        with self.locked(key):
            old = self.get(key)
            if type(data.get('revision')) is not int or data['revision'] != (old or {}).get('revision', 0):
                raise EditConflict('Someone changed this artwork. Reload the source choices before saving.')
            result = deepcopy(old) if old else {'schema': 'pictographic.icon-artwork.v1', 'icon': key}
            now = datetime.now(timezone.utc).isoformat()
            if 'svg' in data:
                document = safe_svg(data['svg'], icon['canvas_size'])
                result['uploaded'] = {'svg': document, 'svg_sha256': sha(document),
                                      'name': Path(str(data.get('filename') or 'uploaded.svg')).name[:200],
                                      'uploaded_by': user, 'uploaded_at': now}
            if mode == 'use_upload' and not result.get('uploaded'):
                raise ValueError('Upload an SVG before choosing the uploaded version.')
            if mode == 'use_edited':
                # Bind selection to the revision the human actually saw.
                with edits.locked(key):
                    edit = edits.get(key, icon['svg_sha256'])
                edit = edit or result.get('edited')
                if not edit or data.get('edit_revision') != edit['revision']:
                    raise EditConflict('Save your gallery edits, then reload the source choices to use them.')
                if effective_validation_status(edit) != 'pass':
                    raise ValueError('Run validation and save the gallery edits first, or save a human force-pass reason.')
                result['edited'] = edit
            result.update(source_mode=mode, source_svg_sha256=icon['svg_sha256'],
                          revision=(old or {}).get('revision', 0)+1, updated_by=user, updated_at=now)
            if mode == 'use_upload':
                result['manual_review'] = {'reviewed_by': user, 'reviewed_at': now,
                                           'svg_sha256': result['uploaded']['svg_sha256']}
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(mode='w', dir=self.folder(key), suffix='.tmp',
                                                 encoding='utf-8', delete=False) as stream:
                    temporary = Path(stream.name)
                    json.dump(result, stream, indent=2, ensure_ascii=False, allow_nan=False)
                    stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
                os.replace(temporary, self.folder(key) / 'artwork.json')
            finally:
                if temporary and temporary.exists():
                    temporary.unlink()
        return result


def resolve_artwork(record, choice, *, variant=None):
    """Return the exact selected SVG plus its provenance; use_org returns None."""
    mode = variant or (choice or {}).get('source_mode', 'use_org')
    if mode == 'use_org':
        return None
    if not choice:
        raise ValueError('That artwork version has not been saved.')
    if mode == 'use_upload':
        uploaded = choice.get('uploaded')
        if not uploaded or sha(uploaded['svg']) != uploaded['svg_sha256']:
            raise ValueError('Uploaded SVG is missing or its content changed.')
        return {'svg': uploaded['svg'], 'svg_sha256': uploaded['svg_sha256'], 'source_mode': mode,
                'graph': None, 'validation_override': choice.get('manual_review'),
                'automatic_status': 'not-run'}
    if mode == 'use_edited':
        edit = choice.get('edited')
        if not edit or effective_validation_status(edit) != 'pass':
            raise ValueError('The saved gallery edit is not accepted for use.')
        document = icon_from_graph(edit['edited_graph']).to_svg()
        return {'svg': document, 'svg_sha256': sha(document), 'source_mode': mode,
                'graph': edit['edited_graph'], 'validation_override': edit.get('validation_override'),
                'automatic_status': edit['validation']['status'], 'edit': edit}
    raise ValueError('Unknown artwork source.')
