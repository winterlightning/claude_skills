from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0d236e3c-000a-4b02-9065-9a95cf6d2b26'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-blossom-vase-with-paired-leaves/20260927T080754Z-thuan-mac-1/reference/vase plant_0d236e3c-000a-4b02-9065-9a95cf6d2b26.svg'
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
    icon_id = 'three-blossom-vase-with-paired-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('vase', 'flowers', 'blossoms', 'bouquet', 'leaves', 'plant', 'decor')

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
        def lens(name, A, T, w):
            """Pointed leaf between A and T; each side bulges 0.75*w off the axis."""
            dx, dy = T[0] - A[0], T[1] - A[1]
            L = (dx * dx + dy * dy) ** 0.5
            nx, ny = -dy / L * w, dx / L * w
            p = lambda f, s: (A[0] + dx * f + nx * s, A[1] + dy * f + ny * s)
            return _path(self, name, A, [('c', p(1 / 3, 1), p(2 / 3, 1), T), ('c', p(2 / 3, -1), p(1 / 3, -1), A)], True)
        # vase; two stems from the rim to four-petal blossoms (high left, lower right) and a pair of leaves on the vase sides
        flower("bloom-l", 12, 12, 3)
        # right blossom r3 about (36,18), its left petal split at the west point (30,18) for the stem
        _path(self, "bloom-r", (33, 15), [((39, 15), 3, 3, True), ((39, 21), 3, 3, True), ((33, 21), 3, 3, True),
                                           ((30, 18), 3, 3, True), ((33, 15), 3, 3, True)], True)
        _path(self, "rim", (16, 28), [(22, 28), (28, 28)])
        _path(self, "vase", (16, 28), [(16, 34), (16, 38), ((20, 42), 4, 4, False), (24, 42), ((28, 38), 4, 4, False), (28, 36), (28, 28)])
        lens("leaf-l", (16, 34), (7, 36), 5.33)
        lens("leaf-r", (28, 36), (40, 38), 5.33)
        self.add_line("stem-l", (22, 28), (12, 18))
        self.add_line("stem-r", (22, 28), (30, 18))
        for a, b in (("stem-l", "stem-r"), ("stem-l", "rim-1"), ("stem-l", "rim-2"), ("stem-r", "rim-1"), ("stem-r", "rim-2"),
                     ("stem-l", "bloom-l-3"), ("stem-l", "bloom-l-4"), ("stem-r", "bloom-r-4"), ("stem-r", "bloom-r-5"),
                     ("vase-1", "rim-1"), ("vase-7", "rim-2"),
                     ("leaf-l-1", "vase-1"), ("leaf-l-2", "vase-1"), ("leaf-l-1", "vase-2"), ("leaf-l-2", "vase-2"),
                     ("leaf-r-1", "vase-6"), ("leaf-r-2", "vase-6"), ("leaf-r-1", "vase-7"), ("leaf-r-2", "vase-7")):
            self.relate("connect", a, b)
