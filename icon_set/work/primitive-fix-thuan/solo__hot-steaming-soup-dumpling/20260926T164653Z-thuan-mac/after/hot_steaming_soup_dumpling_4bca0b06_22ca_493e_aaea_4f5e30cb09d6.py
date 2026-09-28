from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4bca0b06-22ca-493e-aaea-4f5e30cb09d6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hot-steaming-soup-dumpling/20260926T164653Z-thuan-mac/reference/xaio long bao soup duimpling_4bca0b06-22ca-493e-aaea-4f5e30cb09d6.svg'
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
    icon_id = 'hot-steaming-soup-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hot', 'steaming', 'soup', 'dumpling')

    def build(self) -> None:
        # Plan: steaming soup dumpling as in the reference, on SQUARE (6..42).
        # One closed pouch outline: a pleated crown of three r4 knobs - the
        # centre one raised (about (24,24), top y=20), the side ones about
        # (16,26)/(32,26) joined to it by short valley steps - whose outer sides
        # flow tangentially into a tall round belly (cubics to the widest points
        # (6,36)/(42,36) and a flat base at y=42). Three short wavy steam lines
        # (x 15/24/33, y 6..12) sit 9 or more above the knobs. Mirrored about
        # x=24. Belly pleat marks are left out: any mark under the crown reads as
        # a mouth.
        _path(self, 'dumpling', (12, 26), [
            ((16, 22), 4, 4, True), ((20, 26), 4, 4, True), (20, 24), ((24, 20), 4, 4, True), ((28, 24), 4, 4, True),
            (28, 26), ((32, 22), 4, 4, True), ((36, 26), 4, 4, True),
            ('c', (36, 30), (42, 31), (42, 36)), ('c', (42, 41), (34, 42), (24, 42)),
            ('c', (14, 42), (6, 41), (6, 36)), ('c', (6, 31), (12, 30), (12, 26)),
        ], closed=True)
        for i, x in enumerate((15, 24, 33)):
            self.add_bezier(f'steam-{i}', (x, 12), ((x + 2, 10), (x - 2, 8), (x, 6)))
