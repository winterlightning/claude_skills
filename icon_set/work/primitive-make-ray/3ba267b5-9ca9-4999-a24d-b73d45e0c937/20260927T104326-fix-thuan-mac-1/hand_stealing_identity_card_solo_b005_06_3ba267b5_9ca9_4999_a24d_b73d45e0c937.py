from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3ba267b5-9ca9-4999-a24d-b73d45e0c937'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260927T104205Z-thuan-mac-1/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg'
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
    icon_id = 'hand-stealing-identity-card-solo-b005-06'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('hand', 'stealing', 'identity', 'card')

    def build(self) -> None:
        # Plan (reference): an ID card with a portrait, grabbed at its top edge
        # by a hand reaching down from above. Card = rounded rectangle
        # (6,11)-(38,42); its top edge and right wall stop under the fingers.
        # Portrait = Lucide square-user bust: r4 head about (20,28) resting on an
        # r6 shoulder arch rising from the card's bottom edge (bust contact: same
        # centre x, head bottom 4 above the arch top). Hand = two outlined
        # fingers (walls x=26/34/42, 8 wide) hanging from the top edge, their r4
        # tips about (30,15)/(38,15) hooked over the card's top-right corner.
        human_construction = "bust"
        _path(self, "card", (26, 11), [(9, 11), ((6, 14), 3, 3, False), (6, 39), ((9, 42), 3, 3, False),
                                       (14, 42), (26, 42), (35, 42), ((38, 39), 3, 3, False), (38, 19)])
        _circle(self, "head", 20, 28, 4)
        self.add_arc("shoulders", (14, 42), (26, 42), radius_x=6, radius_y=6, sweep=True)
        _path(self, "fingers", (26, 6), [(26, 11), (26, 15), ((30, 19), 4, 4, False), ((34, 15), 4, 4, False),
                                         ((38, 19), 4, 4, False), ((42, 15), 4, 4, False), (42, 6)])
        self.add_line("finger-split", (34, 15), (34, 6))
        self.relate("connect", "shoulders", "card")
        self.relate("connect", "head", "shoulders")
        self.relate("connect", "fingers", "card")
        self.relate("connect", "finger-split", "fingers")
