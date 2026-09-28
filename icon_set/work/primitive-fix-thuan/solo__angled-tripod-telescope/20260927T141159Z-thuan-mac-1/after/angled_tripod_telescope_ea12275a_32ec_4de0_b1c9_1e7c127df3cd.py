from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ea12275a-32ec-4de0-b1c9-1e7c127df3cd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angled-tripod-telescope/20260927T141159Z-thuan-mac-1/reference/telescope_ea12275a-32ec-4de0-b1c9-1e7c127df3cd.svg'
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


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'angled-tripod-telescope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angled', 'tripod', 'telescope')

    def build(self) -> None:
        # Refracting telescope tilted up to the right on a 1:2 slope, on a tripod (reference: stepped
        # tube with a wider objective, a small eyepiece at the back, three thin legs from a mount under
        # the tube). Frame P(s,t) = O + s*(2,-1) + t*(1,2): s runs along the tube, t across it.
        O = (23, 20)
        P = lambda s, t: (O[0] + 2 * s + t, O[1] - s + 2 * t)
        # tube outline: main barrel t=+-2 from s=-4 to 4, objective t=+-3 from s=4 to 8,
        # lower side split at the mount point s=0.
        ring = [P(-4, -2), P(4, -2), P(4, -3), P(8, -3), P(8, 3), P(4, 3), P(4, 2), P(0, 2), P(-4, 2)]
        _path(self, "tube", ring[0], ring[1:] + [ring[0]], closed=True)
        # dividing wall between barrel and objective
        self.add_line("objective-wall", P(4, -2), P(4, 2))
        self.relate("connect", "objective-wall", "tube")
        # eyepiece: short stem from the back centre with a crossbar
        self.add_line("eyepiece", P(-4, 0), P(-8, 0))
        self.add_line("eyepiece-cap", P(-8, -1), P(-8, 1))
        self.relate("connect", "eyepiece", "tube"); self.relate("connect", "eyepiece", "eyepiece-cap")
        m = P(0, 2)
        for n, foot in (("leg-left", (13, 42)), ("leg-mid", (m[0], 42)), ("leg-right", (37, 42))):
            self.add_line(n, m, foot); self.relate("connect", n, "tube")
        self.relate("connect", "leg-left", "leg-mid"); self.relate("connect", "leg-mid", "leg-right")
        self.relate("connect", "leg-left", "leg-right")
