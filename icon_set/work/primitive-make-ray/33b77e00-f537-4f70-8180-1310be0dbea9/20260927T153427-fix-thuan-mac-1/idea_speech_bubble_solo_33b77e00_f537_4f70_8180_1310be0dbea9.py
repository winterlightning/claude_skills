from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '33b77e00-f537-4f70-8180-1310be0dbea9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__idea-speech-bubble-solo/20260927T153247Z-thuan-mac-1/reference/messages bubble with idea_33b77e00-f537-4f70-8180-1310be0dbea9.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'idea-speech-bubble-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('sub icon', 'idea speech bubble')

    def build(self) -> None:
        # Idea speech bubble, as in the reference: a tall rounded-square speech bubble with a
        # pointed tail leaving its bottom edge toward the lower left, holding a light bulb: a round
        # glass dome narrowing into an 8-wide neck with a flat base.
        _path(self, "bubble", (14, 4), [(34, 4), ((40, 10), 6, 6, True), (40, 32), ((34, 38), 6, 6, True), (22, 38),
                                        (12, 44), (14, 38), ((8, 32), 6, 6, True), (8, 10), ((14, 4), 6, 6, True)], True)
        _path(self, "bulb", (20, 29), [(28, 29), (28, 27), ('c', (28, 24), (31, 22.5), (31, 19)),
                                       ((17, 19), 7, 6, False), ('c', (17, 22.5), (20, 24), (20, 27)), (20, 29)], True)
