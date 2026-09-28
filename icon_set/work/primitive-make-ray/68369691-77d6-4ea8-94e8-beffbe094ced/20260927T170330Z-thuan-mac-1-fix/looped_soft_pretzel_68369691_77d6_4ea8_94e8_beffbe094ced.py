"""Looped soft pretzel (figure-eight dough loop).

Plan: 180-degree balanced composition about (24,24). Figure-eight outline:
two lobes (quarter cubics through top, side and bottom extremes) meeting in
V notches at (24,11) and (24,37). A diagonal teardrop sits in the waist,
round end upper-left, point lower-right. Two leaf cut-ins, each a single
inward-bowed curve spanning a lobe's quarter (right lobe top-right, left
lobe bottom-left), as in the reference. Keyshape HRECT_L: lobes x=4/44,
y=8/40.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "68369691-77d6-4ea8-94e8-beffbe094ced"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__looped-soft-pretzel/20260927T164623Z-thuan-mac-1/reference/outdoors bird_68369691-77d6-4ea8-94e8-beffbe094ced.svg"
AUTHOR = "claude-opus-5-5"


class LoopedSoftPretzel(Solo48):
    icon_id = "looped-soft-pretzel"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('pretzel', 'outdoors bird')
    keywords = ('pretzel', 'bread', 'snack', 'bakery', 'dough', 'loop')

    def path(self, name, start, steps, closed=False):
        here, members = start, []
        for j, (kind, end, *args) in enumerate(steps):
            member = f"{name}-{j}"
            if kind == "L":
                self.add_line(member, here, end)
            elif kind == "A":
                self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                             large_arc=args[3] if len(args) > 3 else False)
            else:
                self.add_bezier(member, here, (args[0], args[1], end))
            here = end
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:

        k = 0.5523
        def quarter(name, a, b, horizontal_first):
            # quarter ellipse from a to b; tangent horizontal at a when horizontal_first
            dx, dy = b[0] - a[0], b[1] - a[1]
            if horizontal_first:
                c1, c2 = (a[0] + dx * k, a[1]), (b[0], b[1] - dy * k)
            else:
                c1, c2 = (a[0], a[1] + dy * k), (b[0] - dx * k, b[1])
            self.add_bezier(name, a, (c1, c2, b))
        top, bot = (24, 11), (24, 37)
        self.add_bezier("notch-tr", top, ((27, 9), (30, 8), (34, 8)))
        quarter("r-q1", (34, 8), (44, 24), True)
        quarter("r-q2", (44, 24), (34, 40), False)
        self.add_bezier("notch-br", (34, 40), ((30, 40), (27, 39), bot))
        self.add_bezier("notch-bl", bot, ((21, 39), (18, 40), (14, 40)))
        quarter("l-q3", (14, 40), (4, 24), True)
        quarter("l-q4", (4, 24), (14, 8), False)
        self.add_bezier("notch-tl", (14, 8), ((18, 8), (21, 9), top))
        self.add_contour("outline", "notch-tr", "r-q1", "r-q2", "notch-br", "notch-bl", "l-q3", "l-q4", "notch-tl", closed=True)
        self.add_bezier("leaf-r", (34, 8), ((34, 16), (38, 23), (44, 24)))
        self.add_bezier("leaf-l", (4, 24), ((10, 25), (14, 32), (14, 40)))
        self.relate("connect", "outline", "leaf-r")
        self.relate("connect", "outline", "leaf-l")
        self.path("drop", (32, 29), [
            ("C", (22, 19), (29, 23), (26, 19)),
            ("A", (22, 27), 4, 4, False),              # round end
            ("C", (32, 29), (26, 27), (29, 28)),       # point
        ], closed=True)
