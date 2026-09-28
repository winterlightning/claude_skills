from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '24c756f0-4902-4326-bb44-d7c098a9b97e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-person-with-separate-head/20260927T061820Z-thuan-mac-1/reference/donation charity care person_24c756f0-4902-4326-bb44-d7c098a9b97e.svg'
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


class Drawing(Solo48):
    icon_id = 'hands-cradling-person-with-separate-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('care', 'hands', 'person', 'support', 'protection', 'community', 'help', 'compassion')

    def build(self) -> None:
        # two upright open hands cradle a bust: each hand = outer edge, r4 fingertip, palm edge,
        # thumb slanting in and down (1:1) to the wrist. The r10 shoulder arc rests on the thumbs
        # (shared nodes); the head floats 9 above the shoulder apex.
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            _path(self, f"hand-{side}", (x(20), 40), [(x(20), 18), ((x(12), 18), 4, 4, s < 0), (x(12), 25),
                                                      (x(8), 29), (x(4), 33), (x(4), 40)])
        self.add_arc("shoulders", (16, 29), (32, 29), radius_x=10, radius_y=10, sweep=True)
        self.relate("connect", "shoulders", "hand-left"); self.relate("connect", "shoulders", "hand-right")
        _circle(self, "head", 24, 12, 4)
