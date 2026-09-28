from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '12ce4cb7-a567-4bba-b7fa-b9991bdfc3b0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiker-with-walking-cane/20260926T162509Z-thuan-mac/reference/trekking stick_12ce4cb7-a567-4bba-b7fa-b9991bdfc3b0.svg'
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
    icon_id = 'hiker-with-walking-cane'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('hiker', 'with', 'walking', 'cane', 'outdoors', 'outdoors-batch-04')

    def build(self) -> None:
        # Plan: hiker walking right with a backpack and a trekking pole, as in
        # the reference, drawn in the shared stick-figure style
        # (human_ref/full_body_ref.png) on VRECT_M (x 10..38, y 4..44).
        # Head: r5 ring about (22,9); the torso stands straight below it from
        # the neck (22,22) to the hip (22,32), so the head gap is exactly 8 on
        # centerlines (4 ink). Backpack: a box x 10..22, y 23..32 whose front
        # side is the torso. Arm: from the shoulder (22,25) to the elbow (30,30)
        # and forward to the hand on the pole (38,28). Pole: vertical x=38 from
        # just above the hand down to the ground. Legs stride from the hip to
        # (16,44) and (28,44).
        _circle(self, 'head', 22, 9, 5)
        _path(self, 'torso', (22, 22), [(22, 23), (22, 25), (22, 32)])
        _path(self, 'pack', (22, 23), [(10, 23), (10, 32), (22, 32)])
        _path(self, 'arm', (22, 25), [(30, 30), (38, 28)])
        _path(self, 'pole', (38, 23), [(38, 28), (38, 44)])
        _path(self, 'legs', (16, 44), [(22, 32), (28, 44)])
        for a, b in (('torso', 'pack'), ('torso', 'arm'), ('arm', 'pole'), ('torso', 'legs'), ('pack', 'legs')):
            self.relate('connect', a, b)
        self.mark_human_figure('hiker', head='head', torso='torso-1', torso_junction='start')
