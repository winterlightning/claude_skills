from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '772e4b1a-004f-49ee-a794-bc8ff194add3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-detected-by-motion-sensor/20260927T084830Z-thuan-mac-1/reference/school motion sensoring for learning_772e4b1a-004f-49ee-a794-bc8ff194add3.svg'
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
    icon_id = 'person-detected-by-motion-sensor'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('motion-sensor', 'person', 'running', 'detection', 'school', 'learning', 'sensor')

    def build(self) -> None:
        # person walking under a motion sensor (reference): striding stick figure at the left, a
        # ceiling sensor bar at the top right with detection waves widening below it. Before had
        # a single short arc under a boxed sensor.
        _circle(self, "head", 12, 11, 3)
        self.add_line("torso", (12, 22), (12, 24))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("torso-lean", (12, 24), (12, 30))
        self.add_line("arm-front", (12, 24), (20, 20)); self.add_line("arm-back", (12, 24), (4, 28))
        self.add_line("leg-front", (12, 30), (20, 40)); self.add_line("leg-back", (12, 30), (6, 40))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-front"), ("torso", "arm-back"), ("torso-lean", "arm-front"),
                     ("torso-lean", "arm-back"), ("arm-front", "arm-back"), ("torso-lean", "leg-front"),
                     ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
        _path(self, "sensor", (31, 8), [(41, 8), ((44, 11), 3, 3, True), (44, 13), ((41, 16), 3, 3, True), (31, 16),
                                        ((28, 13), 3, 3, True), (28, 11), ((31, 8), 3, 3, True)], True)
        self.add_arc("wave-near", (30, 25), (42, 25), radius_x=10, radius_y=10, sweep=False)
        self.add_arc("wave-far", (28, 35), (44, 35), radius_x=17, radius_y=17, sweep=False)
