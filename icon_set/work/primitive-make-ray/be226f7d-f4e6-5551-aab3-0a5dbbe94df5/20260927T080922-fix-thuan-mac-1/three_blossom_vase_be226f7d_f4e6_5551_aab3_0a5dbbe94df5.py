from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'be226f7d-f4e6-5551-aab3-0a5dbbe94df5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-blossom-vase/20260927T080754Z-thuan-mac-1/reference/decoration flower vase_be226f7d-f4e6-5551-aab3-0a5dbbe94df5.svg'
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
    icon_id = 'three-blossom-vase'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('vase', 'flowers', 'blossoms', 'bouquet', 'leaf', 'plant', 'decor')

    def build(self) -> None:
        def flower(name, cx, cy, r=3, split_bottom=True):
            """Four-petal blossom: semicircle petals r about (cx+-r, cy), (cx, cy+-r), notches at (cx+-r, cy+-r).
            With split_bottom the bottom petal is split at its lowest point (cx, cy+2r) for a stem."""
            n = r
            steps = [((cx + n, cy - n), r, r, True),                 # top petal
                     ((cx + n, cy + n), r, r, True),                 # right petal
                     ]
            if split_bottom:
                steps += [((cx, cy + 2 * r), r, r, True), ((cx - n, cy + n), r, r, True)]
            else:
                steps += [((cx - n, cy + n), r, r, True)]
            steps += [((cx - n, cy - n), r, r, True)]                # left petal
            return _path(self, name, (cx - n, cy - n), steps, True)
        # flower pot with a rim; two stems fan from the rim centre to four-petal blossoms
        flower("bloom-l", 14, 14, 4)
        # right blossom r3 about (36,18), its left petal split at the west point (30,18) for the stem
        _path(self, "bloom-r", (33, 15), [((39, 15), 3, 3, True), ((39, 21), 3, 3, True), ((33, 21), 3, 3, True),
                                           ((30, 18), 3, 3, True), ((33, 15), 3, 3, True)], True)
        _path(self, "pot", (13, 32), [(16, 32), (22, 32), (32, 32), (35, 32)])
        _path(self, "pot-body", (16, 32), [(16, 38), ((20, 42), 4, 4, False), (28, 42), ((32, 38), 4, 4, False), (32, 32)])
        self.add_line("stem-l", (22, 32), (14, 22))
        self.add_line("stem-r", (22, 32), (30, 18))
        for a, b in (("stem-l", "stem-r"), ("stem-l", "pot-2"), ("stem-l", "pot-3"), ("stem-r", "pot-2"), ("stem-r", "pot-3"),
                     ("stem-l", "bloom-l-3"), ("stem-l", "bloom-l-4"), ("stem-r", "bloom-r-4"), ("stem-r", "bloom-r-5"),
                     ("pot-body-1", "pot-1"), ("pot-body-1", "pot-2"), ("pot-body-5", "pot-3"), ("pot-body-5", "pot-4")):
            self.relate("connect", a, b)
