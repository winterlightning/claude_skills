from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b2ae8639-be76-49c2-be2d-6826d421c781'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__audience-watching-people-on-screen-batch-018-11/20260927T150142Z-thuan-mac-1/reference/movies audience_b2ae8639-be76-49c2-be2d-6826d421c781.svg'
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
    icon_id = 'audience-watching-people-on-screen-batch-018-11'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = 'movies'
    categories = ('primitives', 'movies')
    aliases = ()
    keywords = ('audience', 'screen', 'cinema', 'viewers', 'people', 'movie', 'theater', 'group')

    def build(self) -> None:
        # a screen (standalone walls; the presenter shoulders replace the middle of its bottom edge) showing a person, watched by two audience busts in front of it.
        # Busts: r2 head resting on an elliptical shoulder arch (shared axis, jaw 4 above the arch top).
        walls = [("top", (8, 4), (40, 4)), ("right", (40, 4), (40, 24)), ("bottom-r", (40, 24), (30, 24)),
                 ("bottom-l", (18, 24), (8, 24)), ("left", (8, 24), (8, 4))]
        for n, a, b in walls:
            self.add_line(f"screen-{n}", a, b)
        names = [f"screen-{n}" for n, _, _ in walls]
        for a, b in [(names[0], names[1]), (names[1], names[2]), (names[3], names[4]), (names[4], names[0])]:
            self.relate("connect", a, b)
        _circle(self, "presenter-head", 24, 14, 2)
        self.add_arc("presenter-shoulders", (18, 24), (30, 24), radius_x=6, radius_y=4, sweep=True)
        self.relate("connect", "presenter-head", "presenter-shoulders")
        self.relate("connect", "presenter-shoulders", "screen-bottom-r")
        self.relate("connect", "presenter-shoulders", "screen-bottom-l")
        for i, cx in enumerate((16, 32)):
            _circle(self, f"viewer-head-{i}", cx, 34, 2)
            self.add_arc(f"viewer-shoulders-{i}", (cx - 8, 44), (cx + 8, 44), radius_x=8, radius_y=4, sweep=True)
            self.relate("connect", f"viewer-head-{i}", f"viewer-shoulders-{i}")
        self.relate("connect", "viewer-shoulders-0", "viewer-shoulders-1")
