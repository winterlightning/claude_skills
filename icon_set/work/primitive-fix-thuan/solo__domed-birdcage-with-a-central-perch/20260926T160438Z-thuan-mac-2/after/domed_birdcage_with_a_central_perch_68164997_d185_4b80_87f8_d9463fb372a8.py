from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '68164997-d185-4b80-87f8-d9463fb372a8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__domed-birdcage-with-a-central-perch/20260926T160438Z-thuan-mac-2/reference/bird cage empty_68164997-d185-4b80-87f8-d9463fb372a8.svg'
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
    icon_id = 'domed-birdcage-with-a-central-perch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: empty domed birdcage on VRECT_L (8..40 x 4..44), mirrored about x=24.
        # Ring knob (r3) sits on the dome top, joined at its bottom cardinal point.
        # Dome: r14 semicircle (top y=10) on straight sides x=10/38 standing on the
        # base, one stroke (8..40, y=44) that overhangs the sides like the
        # reference's plate. The central pole runs from the dome top to the base;
        # the perch crosses it at y=30, 8 clear of the side walls.
        _circle(self, 'knob', 24, 7, 3)
        _path(self, 'cage', (10, 44), [
            (10, 24), ((24, 10), 14, 14, True), ((38, 24), 14, 14, True), (38, 44),
        ])
        self.add_polyline('base', (8, 44), (10, 44), (24, 44), (38, 44), (40, 44))
        _path(self, 'pole', (24, 10), [(24, 30), (24, 44)])
        _path(self, 'perch', (18, 30), [(24, 30), (30, 30)])
        self.relate('connect', 'knob', 'cage')
        self.relate('connect', 'cage', 'base')
        self.relate('connect', 'cage', 'pole')
        self.relate('connect', 'pole', 'base')
        self.relate('connect', 'pole', 'perch')
        self.relate('connect', 'knob', 'pole')
