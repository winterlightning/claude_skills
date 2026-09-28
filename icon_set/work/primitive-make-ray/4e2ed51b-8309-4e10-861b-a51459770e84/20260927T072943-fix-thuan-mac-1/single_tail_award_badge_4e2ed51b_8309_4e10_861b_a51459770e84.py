from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4e2ed51b-8309-4e10-861b-a51459770e84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__single-tail-award-badge/20260927T072849Z-thuan-mac-1/reference/badge_4e2ed51b-8309-4e10-861b-a51459770e84.svg'
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
    icon_id = 'single-tail-award-badge'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'rewards'
    categories = ('rewards', 'state')
    aliases = ()
    keywords = ('award', 'prize', 'recognition', 'single-tail-award-badge')

    def build(self) -> None:
        # Medal: a true r14 circle about (24,18) (not an ellipse); the ribbon
        # hangs from two points on its lower rim.
        _path(self, 'medal', (24, 4), [((38, 18), 14, 14, True), ((29, 31), 14, 14, True), ((19, 31), 14, 14, True),
                                       ((10, 18), 14, 14, True), ((24, 4), 14, 14, True)], True)
        # Single ribbon tail with a V notch, 8 below the medal.
        _path(self, 'ribbon', (19, 31), [(19, 44), (24, 40), (29, 44), (29, 31)])
        self.relate('connect', 'medal', 'ribbon')
