from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dc104ccc-60b6-4f68-9ada-273268e4595f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupping-therapy-on-patient/20260927T091424Z-thuan-mac-1/reference/vacuum cup massage back_dc104ccc-60b6-4f68-9ada-273268e4595f.svg'
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
    icon_id = 'cupping-therapy-on-patient'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('cupping', 'therapy', 'massage')

    def build(self) -> None:
        # Plan: massage table (top y=38 across the width, two short legs to y=40);
        # patient lying face down 8 above it: body pill y22..30 (caps r4) and head
        # r4 at (40,26), exactly 8 beside the shoulder cap. One cupping set on the
        # back: glass bell (walls 8 apart + r4 dome) with the r3 rubber bulb seated
        # on the dome apex, bulb top at y=8.
        self.add_line('table-1', (4, 38), (10, 38))
        self.add_line('table-2', (10, 38), (38, 38))
        self.add_line('table-3', (38, 38), (44, 38))
        self.add_line('leg-l', (10, 38), (10, 40))
        self.add_line('leg-r', (38, 38), (38, 40))
        for a, b in (('table-1', 'table-2'), ('table-2', 'table-3'), ('leg-l', 'table-1'), ('leg-l', 'table-2'),
                     ('leg-r', 'table-2'), ('leg-r', 'table-3')):
            self.relate('connect', a, b)
        _path(self, 'body', (8, 22), [
            (14, 22), (22, 22), (24, 22), ((28, 26), 4, 4, True), ((24, 30), 4, 4, True), (8, 30),
            ((4, 26), 4, 4, True), ((8, 22), 4, 4, True),
        ], True)
        _circle(self, 'head', 40, 26, 4)
        self.mark_human_figure('patient', head='head', torso='body-4', torso_junction='start')
        _path(self, 'bell', (14, 22), [(14, 18), ((18, 14), 4, 4, True), ((22, 18), 4, 4, True), (22, 22)])
        _path(self, 'bulb', (18, 14), [((15, 11), 3, 3, True), ((18, 8), 3, 3, True),
                                        ((21, 11), 3, 3, True), ((18, 14), 3, 3, True)], True)
        self.relate('connect', 'bell', 'body')
        self.relate('connect', 'bulb', 'bell')
