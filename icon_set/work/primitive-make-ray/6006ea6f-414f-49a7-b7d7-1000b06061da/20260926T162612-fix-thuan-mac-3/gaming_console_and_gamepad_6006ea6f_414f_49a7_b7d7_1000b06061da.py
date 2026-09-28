from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6006ea6f-414f-49a7-b7d7-1000b06061da'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gaming-console-and-gamepad/20260926T162509Z-thuan-mac/reference/xbox series s joy_6006ea6f-414f-49a7-b7d7-1000b06061da.svg'
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
    icon_id = 'gaming-console-and-gamepad'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('gaming', 'console', 'and', 'gamepad')

    def build(self) -> None:
        # Plan: upright console with a gamepad in front, as in the reference, on
        # VRECT_L (x 8..40, y 4..44). The console is a tall r3-rounded box
        # (x 16..40) whose left wall stops on the controller's top edge and whose
        # base runs into the controller's right grip. Its round vent is an r3
        # ring at (28,16), 9 from both walls and the top. The controller
        # silhouette (x 8..32, y 28..44) has r4 shoulders, flared sides, a rounded
        # left grip and a raised inner arch; thumbsticks are left out because two
        # dots on this small body read as a face.
        _path(self, 'pad', (13, 28), [
            (16, 28), (27, 28), ((31, 32), 4, 4, True), (32, 44), (28, 44), (24, 40), (16, 40), (12, 44),
            ((8, 40), 4, 4, True), (9, 32), ((13, 28), 4, 4, True),
        ], closed=True)
        _path(self, 'console', (16, 28), [
            (16, 7), ((19, 4), 3, 3, True), (37, 4), ((40, 7), 3, 3, True), (40, 41), ((37, 44), 3, 3, True), (32, 44),
        ])
        self.relate('connect', 'pad', 'console')
        _circle(self, 'vent', 28, 16, 3)
