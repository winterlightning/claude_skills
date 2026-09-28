from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7de26cb7-7475-4fc2-9562-2738e9bd49cd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer-with-raised-gloves/20260927T142727Z-thuan-mac-1/reference/fighter_7de26cb7-7475-4fc2-9562-2738e9bd49cd.svg'
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
    icon_id = 'boxer-with-raised-gloves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('boxer', 'with', 'raised', 'gloves')

    def build(self) -> None:
        # Boxer with raised gloves, three-quarter view as in the reference (human ref:
        # icon_set/references/human_ref/user.svg): a round head over a rounded left shoulder, one
        # glove held low in front of the chest with its forearm dropping down, and the other glove
        # raised high on the right with the shoulder line rising to it and its forearm forming the
        # body's right edge. Gloves are r5 circles; the shoulder line ends on their lattice points.
        _circle(self, "head", 20, 10, 4)
        _path(self, "glove-front", (22, 23), [((25, 24), 5, 5, True), ((27, 28), 5, 5, True), ((22, 33), 5, 5, True),
                                              ((17, 28), 5, 5, True), ((19, 24), 5, 5, True), ((22, 23), 5, 5, True)], True)
        _path(self, "glove-raised", (37, 12), [((42, 17), 5, 5, True), ((37, 22), 5, 5, True), ((33, 20), 5, 5, True),
                                               ((32, 17), 5, 5, True), ((37, 12), 5, 5, True)], True)
        _path(self, "torso-left", (19, 24), [(14, 24), ((6, 32), 8, 8, False), (6, 42)])
        self.add_line("shoulder-right", (25, 24), (33, 20))
        self.add_line("forearm-front", (22, 33), (25, 42))
        self.add_line("forearm-raised", (37, 22), (38, 42))
        for a, b in (("torso-left", "glove-front"), ("shoulder-right", "glove-front"), ("shoulder-right", "glove-raised"),
                     ("forearm-front", "glove-front"), ("forearm-raised", "glove-raised")):
            self.relate("connect", a, b)
