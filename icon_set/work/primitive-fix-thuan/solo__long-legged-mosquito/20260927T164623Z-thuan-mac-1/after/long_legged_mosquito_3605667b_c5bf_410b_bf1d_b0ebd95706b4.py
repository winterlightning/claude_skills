"""Long-legged mosquito seen from above.

Plan: mirrored about x=24. Proboscis on the axis into a small round head
(r4); two antennae leave the head sides at 45 degrees; wings and abdomen all
leave one shoulder node N=(24,18) (shared endpoints, no pinch slivers):
two lens narrow wings sweep out and slightly down, the lens abdomen runs down the axis, and
two long legs trail from the abdomen sides to the bottom edge. Keyshape
SQUARE: wing tips x=6/42, proboscis y=6, legs y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3605667b-c5bf-410b-bf1d-b0ebd95706b4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__long-legged-mosquito/20260927T164623Z-thuan-mac-1/reference/mosquito_3605667b-c5bf-410b-bf1d-b0ebd95706b4.svg"
AUTHOR = "claude-opus-5-5"


class LongLeggedMosquito(Solo48):
    icon_id = "long-legged-mosquito"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('mosquito', 'gnat')
    keywords = ('mosquito', 'insect', 'bug', 'bite', 'malaria', 'pest')

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

        n = (24, 18)
        self.add_line("proboscis", (24, 6), (24, 10))
        self.path("head", (24, 10), [("A", (24, 18), 4, 4, True), ("A", (24, 10), 4, 4, True)], closed=True)
        self.relate("connect", "proboscis", "head")
        for side, s in (("l", -1), ("r", 1)):
            x = lambda d: 24 + s * d
            self.add_line(f"antenna-{side}", (x(4), 14), (x(10), 8))
            self.relate("connect", "head", f"antenna-{side}")
            self.add_bezier(f"wing-{side}-a", n, ((x(10), 14), (x(18), 20), (x(18), 26)))
            self.add_bezier(f"wing-{side}-b", (x(18), 26), ((x(18), 30), (x(8), 26), n))
            self.add_contour(f"wing-{side}", f"wing-{side}-a", f"wing-{side}-b", closed=True)
            self.relate("connect", "head", f"wing-{side}")
        self.add_bezier("body-ra", n, ((28, 21), (28, 26), (28, 30)))
        self.add_bezier("body-rb", (28, 30), ((28, 35), (26, 40), (24, 42)))
        self.add_bezier("body-lb", (24, 42), ((22, 40), (20, 35), (20, 30)))
        self.add_bezier("body-la", (20, 30), ((20, 26), (20, 21), n))
        self.add_contour("body", "body-ra", "body-rb", "body-lb", "body-la", closed=True)
        self.relate("connect", "head", "body")
        self.add_line("leg-l", (20, 30), (12, 42))
        self.add_line("leg-r", (28, 30), (36, 42))
        self.relate("connect", "body", "leg-l")
        self.relate("connect", "body", "leg-r")
