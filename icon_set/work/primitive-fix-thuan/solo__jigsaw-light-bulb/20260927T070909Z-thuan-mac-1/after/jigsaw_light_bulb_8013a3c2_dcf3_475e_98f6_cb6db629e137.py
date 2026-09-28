from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8013a3c2-dcf3-475e-98f6-cb6db629e137'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jigsaw-light-bulb/20260927T070909Z-thuan-mac-1/reference/workflow coaching puzzle lightbulb_8013a3c2-dcf3-475e-98f6-cb6db629e137.svg'
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
    icon_id = 'jigsaw-light-bulb'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('bulb', 'puzzle', 'jigsaw', 'idea', 'solution', 'creativity')

    def build(self) -> None:
        # bulb r13 about (24,17) (top y=4) cut into two puzzle pieces by a seam with a centred r3 knob;
        # tapered neck on the 5-12-13 points, base line, rounded screw cap (bottom y=44)
        _path(self, "bulb", (20, 35), [(19, 29), ((29, 29), 13, 13, True, True), (28, 35)])
        xs = (20, 24, 28)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"base-{n}", (a, 35), (b, 35))
        _path(self, "cap", (20, 35), [(20, 40), ((28, 40), 4, 4, False), (28, 35)])
        _path(self, "seam", (11, 17), [(21, 17), ((27, 17), 3, 3, True), (37, 17)])
        for a, b in (("bulb", "base-0"), ("bulb", "base-1"), ("base-0", "base-1"), ("cap", "base-0"),
                     ("cap", "base-1"), ("cap", "bulb"), ("seam", "bulb")):
            self.relate("connect", a, b)
