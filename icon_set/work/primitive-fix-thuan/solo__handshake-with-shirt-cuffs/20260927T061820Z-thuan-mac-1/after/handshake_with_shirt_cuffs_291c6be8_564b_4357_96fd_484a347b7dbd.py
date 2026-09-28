from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '291c6be8-564b-4357-96fd-484a347b7dbd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handshake-with-shirt-cuffs/20260927T061820Z-thuan-mac-1/reference/deal handshake_291c6be8-564b-4357-96fd-484a347b7dbd.svg'
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
    icon_id = 'handshake-with-shirt-cuffs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('handshake', 'agreement', 'partnership', 'business', 'cooperation', 'deal', 'greeting', 'hands')

    def build(self) -> None:
        # handshake between two shirt cuffs (open sleeve ends at both edges), clasp tilted 45 degrees.
        # The right hand's back continues its cuff top into a short thumb slanting down-left with an
        # r5 tip (3-4-5 chord (7,7) about (23,14)); the left hand's back continues its cuff top to
        # the thumb's leftmost point. Below, the heel drops from the left cuff into two r5 fingertips
        # on the line x+y=56 (centres (20,35),(27,28)); the index edge climbs to the right cuff.
        _path(self, "cuff-left", (4, 14), [(10, 14), (10, 32), (4, 32)])
        _path(self, "cuff-right", (44, 8), [(38, 8), (38, 18), (38, 21), (44, 21)])
        _path(self, "right-hand", (38, 8), [(22, 8), (20, 10), ((18, 14), 5, 5, False), ((27, 17), 5, 5, False), (30, 14)])
        self.add_line("left-back", (10, 14), (18, 14))
        _path(self, "fingers", (10, 32), [(17, 39), ((24, 32), 5, 5, False), ((31, 25), 5, 5, False), (38, 18)])
        self.add_line("knuckle", (24, 32), (20, 28))
        for a, b in (("right-hand", "cuff-right"), ("left-back", "cuff-left"), ("left-back", "right-hand"),
                     ("fingers", "cuff-left"), ("fingers", "cuff-right"), ("knuckle", "fingers")):
            self.relate("connect", a, b)
