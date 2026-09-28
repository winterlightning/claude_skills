from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd14f767a-d27e-45c9-837c-e0c5f4d0ad51'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-clapper-toys/20260927T055730Z-thuan-mac-1/reference/reward claps hand stick_d14f767a-d27e-45c9-837c-e0c5f4d0ad51.svg'
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
    icon_id = 'hand-clapper-toys'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # two cartoon hands mirrored about x=24: three r2 finger bumps, an r4 thumb on the outer side,
        # palm narrowing to the stick; the sticks cross below
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            cw = s < 0
            _path(self, f"hand-{side}", (x(10), 30), [
                ('c', (x(16), 28), (x(16), 24), (x(16), 20)),     # outer palm edge
                ((x(16), 12), 4, 4, cw),                          # thumb (outermost x = 4 / 44)
                (x(16), 10),
                ((x(12), 10), 2, 2, cw), ((x(8), 10), 2, 2, cw), ((x(4), 10), 2, 2, cw),   # fingers, tops at y=8
                (x(4), 20),                                        # inner palm edge
                ('c', (x(4), 24), (x(6), 28), (x(10), 30)),
            ], closed=True)
        self.add_line("stick-left", (14, 30), (32, 40))
        self.add_line("stick-right", (34, 30), (16, 40))
        for a, b in (("stick-left", "hand-left"), ("stick-right", "hand-right"), ("stick-left", "stick-right")):
            self.relate("connect", a, b)
