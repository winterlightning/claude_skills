from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd9212b2f-353c-4ae0-96bd-8e2bf060245f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hospital-building-batch-025-02/20260926T164653Z-thuan-mac/reference/hospital 1_d9212b2f-353c-4ae0-96bd-8e2bf060245f.svg'
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
    icon_id = 'hospital-building-batch-025-02'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('hospital', 'building')

    def build(self) -> None:
        # Plan: hospital as in the reference, on HRECT_L (x 4..44, y 8..40): a
        # tall central block (x 12..36, roof y=8) flanked by two lower wings
        # (roof y=20) whose shared walls run to the ground, a plus cross in the
        # block (arms 8, centre (24,20), 8 from roof and walls) and a door
        # (x 20..28, top y=32) cut into the ground line.
        _path(self, 'outline', (4, 40), [
            (4, 20), (12, 20), (12, 8), (36, 8), (36, 20), (44, 20), (44, 40),
            (36, 40), (28, 40), (28, 32), (20, 32), (20, 40), (12, 40), (4, 40),
        ], closed=True)
        self.add_line('left-wall', (12, 20), (12, 40))
        self.add_line('right-wall', (36, 20), (36, 40))
        self.relate('connect', 'outline', 'left-wall')
        self.relate('connect', 'outline', 'right-wall')
        _path(self, 'cross', (24, 16), [(24, 20), (24, 24)])
        self.add_line('cross-bar', (20, 20), (28, 20))
        self.relate('connect', 'cross', 'cross-bar')
