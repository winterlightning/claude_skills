from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7c5fddd0-2422-4e22-b179-5596f4845f71'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gear-hierarchy-square-nodes/20260927T055612Z-thuan-mac-1/reference/obs works_7c5fddd0-2422-4e22-b179-5596f4845f71.svg'
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
    icon_id = 'gear-hierarchy-square-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: a six-lobed gear (smooth cubic lobes, tips on the (0,+-8) and
        # (+-7,+-4) lattice points about (24,16), top at y8) is the root of an
        # org chart: a stem drops from the bottom lobe (24,24) to the middle
        # box, and links leave the lower side lobes (17,20)/(31,20) for the
        # outer boxes. Boxes 8x8 at x4/20/36, y32..40, 8 apart.
        import math
        c = (24, 16)
        tips = [(24, 8), (31, 12), (31, 20), (24, 24), (17, 20), (17, 12)]
        s, p = 2.5, 4.2
        def radial(q):
            dx, dy = q[0] - c[0], q[1] - c[1]; n = math.hypot(dx, dy)
            return (dx / n, dy / n)
        def tangent(p):
            dx, dy = p[0] - c[0], p[1] - c[1]; n = math.hypot(dx, dy)
            return (-dy / n, dx / n)   # clockwise on screen
        steps = []
        for i, a in enumerate(tips):
            b = tips[(i + 1) % 6]
            ta, tb = tangent(a), tangent(b)
            ra, rb = radial(a), radial(b)
            steps.append(('c', (a[0] + s * ta[0] - p * ra[0], a[1] + s * ta[1] - p * ra[1]),
                          (b[0] - s * tb[0] - p * rb[0], b[1] - s * tb[1] - p * rb[1]), b))
        _path(self, 'gear', tips[0], steps, True)
        for name, x0 in (('left', 4), ('mid', 20), ('right', 36)):
            _path(self, f'box-{name}', (x0 + 4, 32), [(x0 + 8, 32), (x0 + 8, 40), (x0, 40), (x0, 32), (x0 + 4, 32)], True)
        self.add_line('link-mid', (24, 24), (24, 32))
        self.add_line('link-left', (17, 20), (8, 32))
        self.add_line('link-right', (31, 20), (40, 32))
        for name in ('left', 'mid', 'right'):
            self.relate('connect', f'link-{name}', 'gear')
            self.relate('connect', f'link-{name}', f'box-{name}')
