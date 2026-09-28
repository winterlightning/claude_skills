from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9639fa15-4ba6-492a-8a1f-5e66bf7fc04d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__immersion-stick-blender/20260926T164653Z-thuan-mac/reference/hand mixer_9639fa15-4ba6-492a-8a1f-5e66bf7fc04d.svg'
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
    icon_id = 'immersion-stick-blender'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('immersion', 'stick', 'blender')

    def build(self) -> None:
        # Plan: immersion (stick) blender as in the reference, on SQUARE (6..42),
        # laid on the 45-degree axis x+y=48 from the blade guard at the bottom
        # left to the handle at the top right.
        # Handle: a pill with r5 end caps about (37,11) and (29,19) whose 3-4-5
        # lattice points give straight sides on x+y=41 and x+y=55 (the top cap
        # reaches the canvas top 6 and right 42 at once).
        # Guard: a half-dome (radius 6*sqrt2 about (12,36), as two tangent
        # quarter cubics) whose flat chord (6,30)-(18,42) faces down-left, with
        # the shaft running from its apex (18,30) to the handle's bottom cap.
        _path(self, 'handle', (33, 8), [
            ((40, 15), 5, 5, True, True), (32, 23), ((26, 23), 5, 5, True), ((25, 16), 5, 5, True), (33, 8),
        ], closed=True)
        _path(self, 'guard', (6, 30), [
            ('c', (9, 27), (15, 27), (18, 30)), ('c', (21, 33), (21, 39), (18, 42)), (6, 30),
        ], closed=True)
        self.add_line('shaft', (18, 30), (26, 23))
        self.relate('connect', 'guard', 'shaft')
        self.relate('connect', 'handle', 'shaft')
