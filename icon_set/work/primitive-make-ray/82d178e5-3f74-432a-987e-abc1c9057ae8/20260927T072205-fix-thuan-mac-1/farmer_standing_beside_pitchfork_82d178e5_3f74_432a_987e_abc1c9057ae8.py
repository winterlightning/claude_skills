from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '82d178e5-3f74-432a-987e-abc1c9057ae8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__farmer-standing-beside-pitchfork/20260927T072058Z-thuan-mac-1/reference/farmer_82d178e5-3f74-432a-987e-abc1c9057ae8.svg'
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


def _smooth(knots, closed=False):
    """Catmull-Rom steps through integer knots (horizontal/vertical tangents stay exact)."""
    pts = list(knots)
    n = len(pts)
    steps = []
    for i in range(n - 1 if not closed else n):
        p0 = pts[i - 1] if (i > 0 or closed) else pts[i]
        p1, p2 = pts[i], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (i + 2 < n or closed) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        steps.append(('c', c1, c2, p2))
    return steps


class Drawing(Solo48):
    icon_id = 'farmer-standing-beside-pitchfork'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ()
    keywords = ('farmer', 'with', 'pitchfork')

    def build(self) -> None:
        # Plan: farmer on the left (axis x=12) - hat with a 12x8 crown
        # standing on the face ends, on a 16-wide brim; the face is the lower half of an r6 head hung
        # from the brim; shoulders 9 below the chin down to the ground.
        # Upright three-tine pitchfork on the right (tines 8 apart on a
        # crossbar, long handle to the ground).
        _path(self, 'hat-crown', (6, 16), [(6, 8), (18, 8), (18, 16)])
        _path(self, 'hat-brim', (4, 16), [(6, 16), (18, 16), (20, 16)])
        self.add_arc('face', (6, 16), (18, 16), radius_x=6, radius_y=6, sweep=False)
        self.relate('connect', 'hat-crown', 'hat-brim')
        self.relate('connect', 'face', 'hat-brim')
        _path(self, 'body', (4, 40), [(4, 37), ('c', (4, 33), (7, 31), (12, 31)), ('c', (17, 31), (20, 33), (20, 37)),
                                      (20, 40)])
        _path(self, 'fork-bar', (28, 18), [(36, 18), (44, 18)])
        for x in (28, 36, 44):
            self.add_line(f'tine-{x}', (x, 8), (x, 18))
            self.relate('connect', f'tine-{x}', 'fork-bar')
        self.add_line('fork-handle', (36, 18), (36, 40))
        self.relate('connect', 'fork-handle', 'fork-bar')
        self.relate('connect', 'fork-handle', 'tine-36')
