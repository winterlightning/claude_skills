from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '69fd62d6-2807-4c9b-9e1a-35e009d9fd9f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-open-end-wrench/20260927T055730Z-thuan-mac-1/reference/self service wrench_69fd62d6-2807-4c9b-9e1a-35e009d9fd9f.svg'
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
    icon_id = 'hand-holding-open-end-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('hand', 'holding', 'open-end', 'wrench')

    def build(self) -> None:
        # open-end wrench: 8-thick prongs round an 8-wide jaw slot, rounded head, 8-wide shank
        _path(self, "wrench", (24, 30), [
            (24, 22),
            ('c', (20, 22), (16, 19), (16, 14)),        # head, left side
            ('c', (16, 9), (19, 6), (24, 6)),           # left prong tip (y=6)
            (24, 10), ((32, 10), 4, 4, False),          # jaw slot with rounded bottom (y=14)
            (32, 6),
            ('c', (37, 6), (40, 9), (40, 14)),          # right prong tip
            ('c', (40, 19), (36, 22), (32, 22)),        # head, right side
            (32, 30),                                   # shank down into the fist
        ])
        # fist around the shank: arm from the left, flat top, two r3 knuckles, flat base
        _path(self, "hand", (6, 32), [
            (18, 30), (24, 30), (32, 30), (39, 30),
            ((39, 36), 3, 3, True), ((39, 42), 3, 3, True),   # two knuckles (x=42)
            (6, 42),
        ])
        self.relate("connect", "hand", "wrench")
