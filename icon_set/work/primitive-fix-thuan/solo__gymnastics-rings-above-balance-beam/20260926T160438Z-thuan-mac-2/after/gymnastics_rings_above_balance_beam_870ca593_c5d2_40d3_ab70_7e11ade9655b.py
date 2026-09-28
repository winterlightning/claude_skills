from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '870ca593-c5d2-40d3-ab70-7e11ade9655b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gymnastics-rings-above-balance-beam/20260926T160438Z-thuan-mac-2/reference/gymnastics acrobatic_870ca593-c5d2-40d3-ab70-7e11ade9655b.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


class Drawing(Solo48):
    icon_id = 'gymnastics-rings-above-balance-beam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('gymnastics', 'rings', 'above', 'balance', 'beam')

    def build(self) -> None:
        # Plan: gymnastics rings above a balance beam on SQUARE, mirrored about x=24.
        # Two r4 rings hang on ropes from the top edge; the beam is an 8-tall box
        # across the full width 9 below the rings; two legs splay from the beam
        # underside to the floor, each ending on a short foot, as in the reference.
        for side, x in (('left', 14), ('right', 34)):
            self.add_line(f'rope-{side}', (x, 6), (x, 9))
            _circle(self, f'ring-{side}', x, 13, 4)
            self.relate('connect', f'rope-{side}', f'ring-{side}')
        self.add_polyline('beam', (6, 26), (42, 26), (42, 34), (34, 34), (14, 34), (6, 34), closed=True)
        self.add_line('leg-left', (14, 34), (9, 42))
        self.add_line('leg-right', (34, 34), (39, 42))
        self.add_polyline('foot-left', (6, 42), (9, 42), (12, 42))
        self.add_polyline('foot-right', (36, 42), (39, 42), (42, 42))
        for side in ('left', 'right'):
            self.relate('connect', 'beam', f'leg-{side}')
            self.relate('connect', f'leg-{side}', f'foot-{side}')
