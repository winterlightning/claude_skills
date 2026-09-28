"""Woman nude: a female torso sign inside a rounded square frame - two side
contours narrowing at the waist, and the lower curves of the breasts.

Symbol plan: frame is a rounded rectangle on the SQUARE centerline box; the
torso is mirrored about x=24: each side contour is shared by the breast curve
(T-junction at the chest, declared connection); the two breast curves meet in
a centre cleavage point.
Keyshape SQUARE: frame (6,6)-(42,42).
Lucide construction: square (rounded frame, radius 6) with smooth mirrored
interior cubics.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had
heavy disconnected hooks; here the torso is a smooth mirrored line drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f11ccece-81b6-415d-a20a-a1bdd3fceb3c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__woman-nude/20260925T092544Z-thuan-mac/reference/woman nude_f11ccece-81b6-415d-a20a-a1bdd3fceb3c.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
FRAME = (6, 6, 42, 42)
CORNER = 6


def m(point):
    return (2 * AXIS - point[0], point[1])


class WomanNude(Solo48):
    icon_id = "woman-nude"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("female-torso", "nude-woman")
    keywords = ("woman", "nude", "female", "torso", "body", "breast", "naked")

    def path(self, name, start, steps, closed=False, mirror=False):
        f = m if mirror else (lambda p: p)
        members = []
        start = f(start)
        for index, (kind, *args) in enumerate(steps):
            tag = f"{name}-{index + 1}"
            if kind == "L":
                end = f(args[0])
                self.add_line(tag, start, end)
            elif kind == "C":
                c1, c2, end = (f(p) for p in args)
                self.add_bezier(tag, start, (c1, c2, end))
            else:
                end, radius = f(args[0]), args[1]
                self.add_arc(tag, start, end, radius_x=radius, sweep=not mirror)
            start = end
            members.append(tag)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        l, t, r, b = FRAME
        k = CORNER
        self.path("frame", (l + k, t), [
            ("L", (r - k, t)), ("A", (r, t + k), k),
            ("L", (r, b - k)), ("A", (r - k, b), k),
            ("L", (l + k, b)), ("A", (l, b - k), k),
            ("L", (l, t + k)), ("A", (l + k, t), k),
        ], closed=True)
        side = [
            ("C", (14, 17), (14, 19), (15, 21)),     # chest
            ("C", (16, 24), (17, 27), (17, 29)),     # into the waist
            ("C", (17, 31), (15, 31.5), (15, 33)),     # out to the hip
        ]
        breast = [
            ("C", (16, 24), (17.5, 27), (20, 27)),   # outer breast curve
            ("C", (22, 27), (23.2, 25.6), (AXIS, 24)),  # inner breast curve into the cleavage
        ]
        for name, mirror in (("left", False), ("right", True)):
            self.path(f"side-{name}", (15, 15), side, mirror=mirror)
            self.path(f"breast-{name}", (15, 21), breast, mirror=mirror)
            self.relate("connect", f"side-{name}", f"breast-{name}")
        self.relate("connect", "breast-left", "breast-right")
