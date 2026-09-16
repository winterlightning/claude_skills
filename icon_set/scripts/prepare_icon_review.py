#!/usr/bin/env python3
"""Render current registered-icon evidence for an agent's visual design review.

Writes only to --out; does not edit models, builds or approval records.
--axis X1 Y1 X2 Y2 adds an arbitrary-axis mirror overlay, not a verdict.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
import inspect
import io
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def reflection_matrix(axis):
    x, y, x2, y2 = axis
    dx, dy = x2-x, y2-y
    length = math.hypot(dx, dy)
    if not all(math.isfinite(v) for v in axis) or not math.isfinite(length) or length == 0:
        raise ValueError('axis requires two distinct finite points')
    ux, uy = dx/length, dy/length
    a, b, d = 2*ux*ux-1, 2*ux*uy, 2*uy*uy-1
    return a, b, b, d, x-a*x-b*y, y-b*x-d*y


def mirror_document(document, axis):
    root = ET.fromstring(document)
    # This file is explicitly diagnostic; the original SVG stays untouched.
    originals = list(root)
    for child in originals:
        root.remove(child)
    for color, reflected in [('#2563eb', False), ('#e11d48', True)]:
        group = ET.SubElement(root, 'g', {'stroke': color, 'color': color, 'opacity': '0.7'})
        if reflected:
            group.set('transform', 'matrix(' + ' '.join(str(v) for v in reflection_matrix(axis)) + ')')
        for child in originals:
            clone = deepcopy(child)
            for element in clone.iter():
                element.attrib.pop('id', None)
                if 'stroke' in element.attrib and element.get('stroke') != 'none':
                    element.set('stroke', color)
            group.append(clone)
    # Include both whole envelopes, even when reflection leaves the canvas.
    vx, vy, vw, vh = map(float, root.get('viewBox').split())
    a, b, c, d, e, f = reflection_matrix(axis)
    corners = [(vx, vy), (vx+vw, vy), (vx, vy+vh), (vx+vw, vy+vh)]
    reflected = [(a*x+c*y+e, b*x+d*y+f) for x, y in corners]
    xs, ys = zip(*(corners+reflected))
    root.set('viewBox', f'{min(xs)-2} {min(ys)-2} {max(xs)-min(xs)+4} {max(ys)-min(ys)+4}')
    return ET.tostring(root, encoding='unicode')


def prepare(icon_id, output, axis=None):
    import cairosvg
    from PIL import Image, ImageDraw
    from icon_set.model import contracts
    from icon_set.model.icons.registry import create
    from icon_set.validation.library_qa import inspect_icon

    if axis is not None:
        reflection_matrix(axis)
    icon = create(icon_id)
    source = Path(inspect.getsourcefile(type(icon))).resolve()
    module = inspect.getmodule(type(icon))
    document = icon.to_svg()
    output.mkdir(parents=True, exist_ok=True)
    (output/'current.svg').write_text(document, encoding='utf-8')
    native = icon.profile.spec.canvas_size

    def render(svg, filename, size, background, foreground):
        root = ET.fromstring(svg)
        root.set('color', foreground)
        png = cairosvg.svg2png(bytestring=ET.tostring(root), output_width=size,
                              output_height=size, background_color=background)
        (output/filename).write_bytes(png)
        return Image.open(io.BytesIO(png)).convert('RGB')

    sheet = Image.new('RGB', (800, 510), '#edf0f4')
    pen = ImageDraw.Draw(sheet)
    pen.text((16, 10), f'{icon_id} | {icon.profile.name} | {icon.keyshape.name}', fill='black')
    for index, (theme, bg, fg) in enumerate([('light', '#ffffff', '#172033'), ('dark', '#172033', '#ffffff')]):
        x = 16+index*400
        small = render(document, f'{theme}-native.png', native, bg, fg)
        large = render(document, f'{theme}-large.png', 360, bg, fg)
        pen.text((x, 38), f'{theme}: native {native}px', fill='black')
        sheet.paste(small, (x, 58))
        pen.text((x, 130), 'Enlarged for inspection', fill='black')
        sheet.paste(large, (x, 150))
    sheet.save(output/'sheet.png')
    qa = inspect_icon(icon)
    qa = {key: value for key, value in qa.items() if not key.startswith('_')}
    reference_name = getattr(module, 'SOURCE_PATH', None)
    evidence = dict(icon_id=icon_id, source=str(source), source_icon_id=getattr(module, 'SOURCE_ICON_ID', None),
                    svg_sha256=hashlib.sha256(document.encode()).hexdigest(),
                    profile=icon.profile.name, profile_spec=asdict(icon.profile.spec),
                    style=contracts.icon_profile()['style'], keyshape=icon.keyshape.name,
                    reference=dict(path=reference_name, status='missing'),
                    axis=axis, qa=qa, visual_review='not_performed')
    if reference_name:
        reference = ROOT/reference_name
        if reference.is_file():
            try:
                if reference.suffix.lower() == '.svg':
                    render(reference.read_text(), 'reference.png', 480, '#ffffff', '#172033')
                else:
                    with Image.open(reference) as source_image:
                        source_image.convert('RGB').save(output/'reference.png')
                evidence['reference']['status'] = 'rendered'
            except Exception as error:
                evidence['reference'].update(status='error', error=f'{type(error).__name__}: {error}')
    if axis is not None:
        overlay = mirror_document(document, axis)
        (output/'mirror.svg').write_text(overlay, encoding='utf-8')
        render(overlay, 'mirror.png', 640, '#ffffff', '#172033')
    (output/'evidence.json').write_text(json.dumps(evidence, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    return evidence


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--icon', required=True)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--axis', nargs=4, type=float, metavar=('X1', 'Y1', 'X2', 'Y2'))
    args = parser.parse_args(argv)
    try:
        result = prepare(args.icon, args.out, args.axis)
    except Exception as error:
        parser.exit(2, f'error: {type(error).__name__}: {error}\n')
    print(f"Evidence: {args.out.resolve()}\nNumeric QA: {result['qa']['status']}\nVisual review: not performed")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
