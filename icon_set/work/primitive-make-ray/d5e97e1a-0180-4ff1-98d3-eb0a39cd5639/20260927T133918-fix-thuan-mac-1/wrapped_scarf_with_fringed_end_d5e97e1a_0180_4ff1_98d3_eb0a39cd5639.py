from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd5e97e1a-0180-4ff1-98d3-eb0a39cd5639'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wrapped-scarf-with-fringed-end/20260927T133651Z-thuan-mac-1/reference/sewing scarf_d5e97e1a-0180-4ff1-98d3-eb0a39cd5639.svg'
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
    icon_id = 'wrapped-scarf-with-fringed-end'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('wrapped', 'scarf', 'with', 'fringed', 'end')

    def build(self) -> None:
        # Wrapped scarf (reference: a tilted loop wound round the neck with a fold line across it, and one
        # end hanging below with a stripe band and fringe strands). The loop is five cubics whose knots on
        # the extremes carry vertical/horizontal handles, so it meets the keyshape exactly; its bottom
        # slopes down to the right like the reference's tilted wrap.
        _path(self, "loop", (8, 13), [('c', (8, 9), (9, 7), (12, 6)), ('c', (15, 5), (20, 4), (24, 4)),
                                      ('c', (32, 4), (40, 6), (40, 12)), ('c', (40, 18), (38, 23), (34, 25)),
                                      ('c', (30, 27), (22, 26), (14, 21)), ('c', (10, 18.5), (8, 17), (8, 13))], True)
        _path(self, "fold", (12, 6), [('c', (16, 10), (20, 14), (24, 14)), ('c', (29, 14), (36, 14), (40, 12))])
        self.add_line("tail-left-top", (14, 21), (14, 38))
        self.add_line("tail-left-fringe", (14, 38), (14, 44))
        self.add_line("tail-right-top", (34, 25), (34, 38))
        self.add_line("tail-right-fringe", (34, 38), (34, 44))
        self.add_line("stripe-left", (14, 38), (24, 38))
        self.add_line("stripe-right", (24, 38), (34, 38))
        self.add_line("fringe-middle", (24, 38), (24, 44))
        self.relate("connect", "loop-1", "loop-2", "fold-1")
        self.relate("connect", "loop-3", "loop-4", "fold-2")
        self.relate("connect", "loop-5", "loop-6", "tail-left-top")
        self.relate("connect", "loop-4", "loop-5", "tail-right-top")
        self.relate("connect", "tail-left-top", "tail-left-fringe", "stripe-left")
        self.relate("connect", "tail-right-top", "tail-right-fringe", "stripe-right")
        self.relate("connect", "stripe-left", "stripe-right", "fringe-middle")
