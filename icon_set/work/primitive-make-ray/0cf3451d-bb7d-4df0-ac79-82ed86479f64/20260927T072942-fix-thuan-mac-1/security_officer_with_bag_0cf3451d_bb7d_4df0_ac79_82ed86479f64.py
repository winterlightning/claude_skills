from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0cf3451d-bb7d-4df0-ac79-82ed86479f64'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__security-officer-with-bag/20260927T072849Z-thuan-mac-1/reference/security officer luggage_0cf3451d-bb7d-4df0-ac79-82ed86479f64.svg'
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
    icon_id = 'security-officer-with-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('security', 'officer', 'luggage', 'bag', 'checkpoint', 'airport', 'guard', 'inspection')

    def build(self) -> None:
        # Suitcase on the left: 12x18 body with an 8-wide r4 handle.
        _path(self, 'bag', (6, 24), [(8, 24), (16, 24), (18, 24), (18, 36), (18, 42), (6, 42), (6, 24)], True)
        _path(self, 'handle', (8, 24), [(8, 16), ((16, 16), 4, 4, True), (16, 24)])
        self.relate('connect', 'bag', 'handle')
        # Officer: peaked cap (crown flaring over the brim), face as the r6
        # half-circle under the brim, shoulders 9 below with a V collar.
        _path(self, 'cap', (28, 14), [(26, 6), (42, 6), (40, 14), (28, 14)], True)
        _path(self, 'face', (28, 14), [((34, 20), 6, 6, False), ((40, 14), 6, 6, False)])
        self.relate('connect', 'cap', 'face')
        _path(self, 'body', (26, 42), [(26, 36), (26, 32), ((29, 29), 3, 3, True), (31, 29), (34, 32), (37, 29),
                                       (39, 29), ((42, 32), 3, 3, True), (42, 42)])
        # Arm reaching from the shoulder side to the suitcase.
        self.add_line('arm', (26, 36), (18, 36))
        self.relate('connect', 'arm', 'body')
        self.relate('connect', 'arm', 'bag')
