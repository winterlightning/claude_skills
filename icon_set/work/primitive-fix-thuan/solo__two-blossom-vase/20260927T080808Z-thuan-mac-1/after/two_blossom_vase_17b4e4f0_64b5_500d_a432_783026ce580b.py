from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '17b4e4f0-64b5-500d-a432-783026ce580b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-blossom-vase/20260927T080808Z-thuan-mac-1/reference/decoration cherry blossom vase_17b4e4f0-64b5-500d-a432-783026ce580b.svg'
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
    icon_id = 'two-blossom-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('vase', 'blossom', 'flowers', 'stems', 'cherry', 'bouquet', 'decor')

    def build(self) -> None:
        # Two blossoms in a vase (reference) on VRECT_L, mirrored about
        # x=24: a tall vase with a straight neck (x 20..28), a belly widest
        # at y=34 and a narrower foot; two stems leave the mouth (24,20) at
        # 45 degrees (off both the mouth line and the neck walls) into the
        # lower valleys of two quatrefoil blossoms (four r3 lobes about
        # c+-(3,0), c+-(0,3), valleys c+-(3,3)) that fill the 32 width.
        _path(self, 'vase', (24, 20), [(28, 20), (28, 24),
                                       ('c', (28, 28), (33, 29), (33, 34)), ('c', (33, 39), (31, 44), (28, 44)),
                                       (20, 44), ('c', (17, 44), (15, 39), (15, 34)),
                                       ('c', (15, 29), (20, 28), (20, 24)), (20, 20), (24, 20)], True)
        for side, (cx, cy) in (('left', (14, 10)), ('right', (34, 10))):
            _path(self, f'blossom-{side}', (cx + 3, cy - 3),
                  [((cx + 3, cy + 3), 3, 3, True), ((cx - 3, cy + 3), 3, 3, True),
                   ((cx - 3, cy - 3), 3, 3, True), ((cx + 3, cy - 3), 3, 3, True)], True)
        self.add_line('stem-left', (24, 20), (17, 13))
        self.add_line('stem-right', (24, 20), (31, 13))
        self.relate('connect', 'stem-left', 'vase')
        self.relate('connect', 'stem-right', 'vase')
        self.relate('connect', 'stem-left', 'blossom-left')
        self.relate('connect', 'stem-right', 'blossom-right')
        self.relate('connect', 'stem-left', 'stem-right')
