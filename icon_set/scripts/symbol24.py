#!/usr/bin/env python3
"""SYMBOL24 helpers for the /symbol-24 skill: structure check, 32->24 draft, previews.

    python3 icon_set/scripts/symbol24.py check --icon plus-symbol24
    python3 icon_set/scripts/symbol24.py from32 --icon plus-sub32 --author claude-opus-5-5
    python3 icon_set/scripts/symbol24.py preview --icon plus-symbol24 --compare plus-sub32 --out /tmp/p

`check` blocks only on what defines the profile: family symbol24, an SVG root of
exactly 24x24 and every stroke 4. The library QA verdict (validate_icon, spacing,
holes, symmetry) is printed as advisory findings; the contract marks symbol24
validation advisory, so quality is judged by looking at the 24 px render.

`from32` reads a plain 32x32 sub or symbol model and writes a *draft* SYMBOL24
module: every coordinate times 3/4, rounded toward the centre (12,12) so
mirrored geometry stays mirrored and no extreme leaves the canvas. The stroke does
not scale, so every gap shrinks by a quarter; the draft is a starting point to
redraw and rebalance, never a finished icon.
"""
from __future__ import annotations

import argparse
import inspect
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model.icons.registry import create, factories  # noqa: E402
from icon_set.model.primitives import Arc, Bezier, Line  # noqa: E402
from icon_set.model.profiles import STROKE_WIDTH, Profile  # noqa: E402

PROFILE = Profile.SYMBOL24
SIZE = PROFILE.spec.canvas_size
CENTER = PROFILE.spec.center[0]
SCALE = 3 / 4
OUT_DIR = REPO_ROOT / 'icon_set' / 'model' / 'icons' / 'symbol24'


# -- check ------------------------------------------------------------------

def strict_check_icon(icon) -> dict:
    from icon_set.validation.library_qa import inspect_icon

    problems = []
    if icon.family != 'symbol24' or icon.profile is not PROFILE:
        problems.append(f'family/profile is {icon.family}/{icon.profile.name}, not symbol24/SYMBOL24')
    if getattr(icon.keyshape, 'name', '') == 'FREE':
        problems.append('keyshape: FREE; choose a real SYMBOL24 keyshape')
    root = ET.fromstring(icon.to_svg())
    if (root.get('width'), root.get('height'), root.get('viewBox')) != (str(SIZE), str(SIZE), f'0 0 {SIZE} {SIZE}'):
        problems.append(f"svg root: width={root.get('width')} height={root.get('height')} viewBox={root.get('viewBox')}")
    widths = {e.get('stroke-width') for e in root.iter() if e.get('stroke-width') is not None}
    if widths - {str(STROKE_WIDTH)}:
        problems.append(f'stroke: widths {sorted(widths)}; every stroke must be {STROKE_WIDTH}')
    try:
        row = inspect_icon(icon)
        advisory = list(row.get('errors', [])) + list(row.get('warnings', []))
        qa_status = row.get('automatic_status', row['status'])
    except Exception as error:  # advisory: a crashing check is reported, not fatal
        advisory, qa_status = [f'qa crashed: {error}'], 'error'
    return {'icon_id': icon.icon_id, 'strict_24': 'fail' if problems else 'pass',
            'problems': problems, 'qa_status': qa_status, 'advisory': advisory,
            'keyshape': getattr(icon.keyshape, 'name', str(icon.keyshape))}


def cmd_check(args) -> int:
    ok = True
    for icon_id in args.icon:
        result = strict_check_icon(create(icon_id))
        ok &= result['strict_24'] == 'pass'
        print(f"{icon_id}: strict-24 {result['strict_24']} (keyshape {result['keyshape']}, "
              f"advisory qa {result['qa_status']})")
        for message in result['problems']:
            print(f'  BLOCKING  {message}')
        for message in result['advisory']:
            print(f'  advisory  {message}')
    return 0 if ok else 1


# -- from32 -----------------------------------------------------------------

def _coord(value: float) -> int:
    """3/4 of a 32-grid coordinate, halves rounded toward the 24-grid centre."""
    offset = value * SCALE - CENTER
    return CENTER + int(math.copysign(math.ceil(abs(offset) - 0.5), offset))


def _pt(point) -> tuple[int, int]:
    return (_coord(point.x), _coord(point.y))


def _control(point) -> tuple[float, float]:
    return (round(point[0] * SCALE, 3), round(point[1] * SCALE, 3))


def _snap_knot(point) -> tuple[int, int]:
    return (_coord(point[0]), _coord(point[1]))


def default_id(icon_id: str) -> str:
    stem = re.sub(r'(-sub32)?(-symbol)?(-sub32)?(-v\d+)?$', '', icon_id)
    return f'{stem}-symbol24'


def class_name_for(icon_id: str) -> str:
    return ''.join(part.capitalize() for part in re.split(r'[^0-9a-zA-Z]+', icon_id) if part)


def convert_from32(icon, *, icon_id: str, class_name: str, author: str,
                   source_icon_id: str | None = None, source_path: str | None = None) -> str:
    from icon_set.model.icons.sub._text_base import canvas_dimensions

    if icon.profile.spec.canvas_size != 32 or canvas_dimensions(icon) != (32, 32):
        raise ValueError(f'{icon.icon_id} is not a plain 32x32 drawing; redraw it at 24 by hand')
    drawing = icon.draw()
    notes, lines = [], []
    for primitive in drawing.primitives:
        eid = primitive.element_id
        if isinstance(primitive, Line):
            start, end = _pt(primitive.start), _pt(primitive.end)
            if primitive.is_dot:
                lines.append(f'self.add_dot({eid!r}, {start})')
                continue
            if start == end:
                notes.append(f'{eid}: collapsed to a point at 24; redraw or remove it')
            lines.append(f'self.add_line({eid!r}, {start}, {end})')
        elif isinstance(primitive, Arc):
            start, end = _pt(primitive.start), _pt(primitive.end)
            rx = max(1, round(primitive.radius_x * SCALE))
            ry = max(1, round(primitive.radius_y * SCALE))
            chord = math.dist(start, end) / 2
            if rx == ry and chord > rx:
                notes.append(f'{eid}: radius {rx} was shorter than half its chord; raised to {math.ceil(chord)}')
                rx = ry = math.ceil(chord)
            radius = f'radius_x={rx}' + (f', radius_y={ry}' if ry != rx else '')
            lines.append(f'self.add_arc({eid!r}, {start}, {end}, {radius}, '
                         f'large_arc={primitive.large_arc}, sweep={primitive.sweep})')
        elif isinstance(primitive, Bezier):
            segments = list(primitive.segments)
            parts = []
            for index, (c1, c2, knot) in enumerate(segments):
                knot = _snap_knot(knot) if index == len(segments) - 1 else _control(knot)
                parts.append(f'({_control(c1)}, {_control(c2)}, {knot})')
            joined = ',\n            '.join(parts)
            lines.append(f'self.add_bezier({eid!r}, {_pt(primitive.start)},\n            {joined})')
        else:  # pragma: no cover - the primitive union is closed
            raise TypeError(f'unknown primitive {primitive!r}')
    for contour in drawing.contours:
        members = ', '.join(repr(m) for m in contour.members)
        closed = ', closed=True' if contour.closed else ''
        lines.append(f'self.add_contour({contour.contour_id!r}, {members}{closed})')
    for relation in drawing.relationships:
        members = ', '.join(repr(m) for m in relation.members)
        lines.append(f'self.relate({relation.kind!r}, {members})')
    for figure in drawing.human_figures:
        notes.append(f'human figure {figure.figure_id!r}: re-mark it with mark_human_figure and keep the 4-unit head gap')
    body = '\n'.join(f'        {line}' for line in lines) or '        pass'
    todo = ''.join(f'#   - {note}\n' for note in notes)
    return f'''"""{icon_id}: SYMBOL24 redraw of `{icon.icon_id}`.

Started from `symbol24.py from32` (every coordinate x 3/4, rounded toward the
centre). The 4-unit stroke does not scale, so gaps shrink; rebalance the drawing
at 24 and judge it visually before calling it done.
"""
from ...keyshapes import Keyshape
from ._base import Symbol24

SOURCE_ICON_ID = {source_icon_id!r}
SOURCE_PATH = {source_path!r}
AUTHOR = {author!r}
DERIVED_FROM_32 = {icon.icon_id!r}

# Draft notes from the 3/4 conversion; delete each once it is resolved.
{todo or '#   (none)\n'}

class {class_name}(Symbol24):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{icon.keyshape.name}
    semantic_role = {icon.semantic_role!r}
    semantic_kind = {type(icon).semantic_kind!r}
    category = {type(icon).category!r}
    aliases = {tuple(type(icon).aliases)!r}
    keywords = {tuple(type(icon).keywords)!r}

    def build(self) -> None:
{body}
'''


def _module_value(path: Path, name: str):
    from icon_set.scripts.fix_icon_sub import module_value
    return module_value(path, name)


def cmd_from32(args) -> int:
    factory = factories().get(args.icon)
    if factory is None:
        raise SystemExit(f'error: no registered icon {args.icon!r}')
    source = factory()
    if source.family not in ('sub', 'symbol'):
        raise SystemExit(f'error: {args.icon} is {source.family}; from32 reads sub or symbol icons')
    path = Path(inspect.getsourcefile(factory)).resolve()
    source_id = _module_value(path, 'SOURCE_ICON_ID')
    icon_id = args.id or default_id(args.icon)
    if icon_id in factories():
        raise SystemExit(f'error: {icon_id} already exists; pass --id for a new variant')
    stem = icon_id.replace('-', '_')
    if source_id:
        stem += '_' + re.sub(r'[^0-9A-Za-z]+', '_', str(source_id)).strip('_').lower()
    target = OUT_DIR / f'{stem}.py'
    if target.exists():
        raise SystemExit(f'error: {target.relative_to(REPO_ROOT)} already exists')
    try:
        text = convert_from32(source, icon_id=icon_id, class_name=class_name_for(icon_id),
                              author=args.author, source_icon_id=source_id,
                              source_path=_module_value(path, 'SOURCE_PATH'))
    except ValueError as error:
        raise SystemExit(f'error: {error}')
    target.write_text(text, encoding='utf-8')
    print(f'wrote {target.relative_to(REPO_ROOT)} ({icon_id})')
    return 0


# -- preview ----------------------------------------------------------------

THEMES = {'light': ('#ffffff', '#111111'), 'dark': ('#111111', '#f2f2f2')}


def cmd_preview(args) -> int:
    import cairosvg

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    ids = [args.icon] + ([args.compare] if args.compare else [])
    for icon_id in ids:
        document = create(icon_id).to_svg()
        (out / f'{icon_id}.svg').write_text(document, encoding='utf-8')
        native = int(ET.fromstring(document).get('width'))
        for theme, (background, ink) in THEMES.items():
            themed = document.replace('currentColor', ink)
            for label, size in (('native', native), ('x8', native * 8)):
                png = out / f'{icon_id}-{theme}-{label}.png'
                cairosvg.svg2png(bytestring=themed.encode(), write_to=str(png),
                                 output_width=size, output_height=size, background_color=background)
                print(png)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('check', help='structure gate (blocking) plus advisory QA findings')
    check.add_argument('--icon', action='append', required=True)
    check.set_defaults(run=cmd_check)
    from32 = sub.add_parser('from32', help='write a 3/4 SYMBOL24 draft from a 32x32 sub or symbol')
    from32.add_argument('--icon', required=True, help='the 32x32 sub or symbol icon id')
    from32.add_argument('--author', required=True, help='the model authoring the redraw')
    from32.add_argument('--id', help='icon id for the new symbol24 (default <stem>-symbol24)')
    from32.set_defaults(run=cmd_from32)
    preview = sub.add_parser('preview', help='native and x8 PNGs in light and dark')
    preview.add_argument('--icon', required=True)
    preview.add_argument('--compare', help='also render this icon (e.g. the 32 source)')
    preview.add_argument('--out', required=True)
    preview.set_defaults(run=cmd_preview)
    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == '__main__':
    raise SystemExit(main())
