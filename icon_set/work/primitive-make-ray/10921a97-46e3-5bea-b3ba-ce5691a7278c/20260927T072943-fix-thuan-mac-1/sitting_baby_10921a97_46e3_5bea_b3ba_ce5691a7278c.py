from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '10921a97-46e3-5bea-b3ba-ce5691a7278c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sitting-baby/20260927T072849Z-thuan-mac-1/reference/baby care body_10921a97-46e3-5bea-b3ba-ce5691a7278c.svg'
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
    icon_id = 'sitting-baby'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('sitting', 'baby', 'infant', 'nursery')

    def build(self) -> None:
        # Sitting baby (reference): big r10 head about (24,16); arms and
        # torso sides leave the head at its 6-8-10 points (16,22)/(32,22);
        # diaper line at y=34 with two r4 round feet hanging from its corners.
        _path(self, 'head', (24, 6), [((34, 16), 10, 10, True), ((32, 22), 10, 10, True), ((24, 26), 10, 10, True),
                                      ((16, 22), 10, 10, True), ((14, 16), 10, 10, True), ((24, 6), 10, 10, True)], True)
        self.add_line('arm-left', (16, 22), (6, 30))
        self.add_line('arm-right', (32, 22), (42, 30))
        _path(self, 'torso', (16, 22), [(16, 34), (32, 34), (32, 22)])
        _circle(self, 'foot-left', 16, 38, 4)
        _circle(self, 'foot-right', 32, 38, 4)
        for a, b in [('arm-left', 'head'), ('arm-right', 'head'), ('torso', 'head'), ('arm-left', 'torso'),
                     ('arm-right', 'torso'), ('foot-left', 'torso'), ('foot-right', 'torso')]:
            self.relate('connect', a, b)
