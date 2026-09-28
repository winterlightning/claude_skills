from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ddb289ec-fc69-4127-b2e2-bb63eae11231'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robot-gripper-holding-round-sample/20260927T101542Z-thuan-mac-1/reference/robot hand science experiment_ddb289ec-fc69-4127-b2e2-bb63eae11231.svg'
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
    icon_id = 'robot-gripper-holding-round-sample'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'gripper', 'holding', 'round', 'sample')

    def build(self) -> None:
        # Plan: round sample r6 about (24,15) held by two mirrored jointed claw fingers
        # (knuckle, straight upper phalanx, tip bent in over the sample) that root on
        # an r3 wrist hub; the robot arm leaves the hub down to the lower left.
        _circle(self, "sample", 24, 15, 6)
        _circle(self, "wrist", 24, 33, 3)
        _path(self, "claw-left", (21, 33), [(8, 24), (8, 12), (15, 4)], False)
        _path(self, "claw-right", (27, 33), [(40, 24), (40, 12), (33, 4)], False)
        _path(self, "arm", (24, 36), [(24, 38), (18, 44)], False)
        self.relate("connect", "claw-left", "wrist")
        self.relate("connect", "claw-right", "wrist")
        self.relate("connect", "arm", "wrist")
