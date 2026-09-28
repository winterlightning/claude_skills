from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c6536663-b340-5128-bbbb-fbd254093c96'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__twisting-triangle-pose/20260927T080808Z-thuan-mac-1/reference/yoga twisting triangle pose_c6536663-b340-5128-bbbb-fbd254093c96.svg'
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
    icon_id = 'twisting-triangle-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('twisting', 'triangle', 'pose', 'yoga', 'exercise')

    def build(self) -> None:
        # Twisting triangle pose (reference): the head hangs forward on the
        # left, level with a short horizontal neck run (head r4 at (10,18),
        # neck (22,18): exactly 8 between centerlines); the arms form one
        # line through the shoulder (24,18), up to (34,6) and down toward
        # the floor at (15,36); the torso leans back down-right to the hips
        # (31,26), about square to the arms; legs spread wide to (21,42) and
        # (42,42). The lower arm keeps 12.5 from the head centre and 8.3
        # from the front leg.
        _circle(self, 'head', 10, 18, 4)
        self.add_line('torso', (22, 18), (24, 18))
        self.add_line('torso-lean', (24, 18), (31, 26))
        self.add_line('arm-up', (24, 18), (34, 6))
        self.add_line('arm-down', (24, 18), (15, 36))
        self.add_line('leg-front', (31, 26), (21, 42))
        self.add_line('leg-back', (31, 26), (42, 42))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        for a, b in (('torso-lean', 'torso'), ('arm-up', 'torso'), ('arm-down', 'torso'),
                     ('arm-up', 'torso-lean'), ('arm-down', 'torso-lean'), ('arm-up', 'arm-down'),
                     ('leg-front', 'torso-lean'), ('leg-back', 'torso-lean'), ('leg-front', 'leg-back')):
            self.relate('connect', a, b)
