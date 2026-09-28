"""Manservant: formal bust with a bow tie.

Plan: mirrored about x=24. Oval head (ellipse rx 7, ry 8) detached above the
collar. Shoulders are one arch: r8 rounded shoulders joined by a straight
collar line at y=32. A horizontal bow tie sits on the collar: two open
chevron wings meeting at the knot (24,32), which the stroke fills into solid
wings without enclosed holes. Keyshape SQUARE: shoulders x=6/42, head y=6,
base y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f673664b-85b3-410d-a058-e07884f97429"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__manservant/20260927T164623Z-thuan-mac-1/reference/manservant_f673664b-85b3-410d-a058-e07884f97429.svg"
AUTHOR = "claude-opus-5-5"


class Manservant(Solo48):
    icon_id = "manservant"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('butler', 'waiter', 'valet')
    keywords = ('butler', 'servant', 'waiter', 'bow tie', 'formal', 'person')

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

        self.path("head", (17, 14), [("A", (31, 14), 7, 8, True), ("A", (17, 14), 7, 8, True)], closed=True)
        self.path("shoulders", (6, 42), [
            ("L", (6, 40)),
            ("A", (14, 32), 8, 8, True),
            ("L", (24, 32)),
            ("L", (34, 32)),
            ("A", (42, 40), 8, 8, True),
            ("L", (42, 42)),
        ])
        self.add_polyline("bow-l", (19, 30), (24, 32), (19, 34))
        self.add_polyline("bow-r", (29, 30), (24, 32), (29, 34))
        self.relate("connect", "shoulders", "bow-l")
        self.relate("connect", "shoulders", "bow-r")
        self.relate("connect", "bow-l", "bow-r")
