from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a7ad061e-a477-4a15-993d-a60fd5aa42f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiker-with-headlamp/20260926T162509Z-thuan-mac/reference/climbing head light_a7ad061e-a477-4a15-993d-a60fd5aa42f9.svg'
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
    icon_id = 'hiker-with-headlamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('headlamp', 'climbing', 'hiker', 'caving', 'night', 'backpack', 'light', 'explorer', 'outdoors-batch-01')

    def build(self) -> None:
        # Plan: hiker with a backpack wearing a helmet headlamp, as in the
        # reference, in the shared stick-figure style (human_ref/full_body_ref.png)
        # on VRECT_L (x 8..40, y 4..44). Head: r6 ring about (20,10) crossed by
        # a helmet brim (13..27 at y=10), so the top half reads as the helmet and
        # the bottom half as the face. Two light beams fan out ahead of the head,
        # detached as in the reference: they start 8 apart at x=34, 8+ clear of
        # the head and brim, and spread to the right edge (40,4) / (40,16). The
        # torso stands straight below the head from the neck (20,24) to the hip
        # (20,34): the head gap is exactly 8 on centerlines (4 ink). Backpack: a
        # box x 8..20, y 25..34 whose front side is the torso. Arm reaches
        # forward from the shoulder (20,27) to (28,30); legs stride from the hip
        # to (14,44) and (26,44).
        _path(self, 'head', (20, 4), [
            ((26, 10), 6, 6, True), ((20, 16), 6, 6, True), ((14, 10), 6, 6, True), ((20, 4), 6, 6, True),
        ], closed=True)
        _path(self, 'brim', (13, 10), [(14, 10), (26, 10), (27, 10)])
        self.relate('connect', 'head', 'brim')
        self.add_line('beam-top', (34, 6), (40, 4))
        self.add_line('beam-bottom', (34, 14), (40, 16))
        _path(self, 'torso', (20, 24), [(20, 25), (20, 27), (20, 34)])
        _path(self, 'pack', (20, 25), [(8, 25), (8, 34), (20, 34)])
        self.add_line('arm', (20, 27), (28, 30))
        _path(self, 'legs', (14, 44), [(20, 34), (26, 44)])
        for a, b in (('torso', 'pack'), ('torso', 'arm'), ('torso', 'legs'), ('pack', 'legs')):
            self.relate('connect', a, b)
        self.mark_human_figure('hiker', head='head', torso='torso-1', torso_junction='start')
