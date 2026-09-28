"""Man with long curly hair and a full beard (bust).

Plan: mirrored about x=24. Curly hair is an open scalloped arch of r5 arc
bumps (side bumps apex x=6/42, a flatter r10 crown bump apex y=6) ending at the temples.
Inside, the face and beard are one closed contour: a brow at y=17 with r4 temples, straight
cheeks, then the beard rounding to a chin at y=38, with a moustache line across
at y=26 (face x 18-30) splitting face from beard. Short shoulder curves leave the beard sides
and fall to the bottom corners. Keyshape SQUARE.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a548408b-568e-54b3-a505-dd3fee33a1e7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-with-long-curly-hair-and-beard/20260927T164623Z-thuan-mac-1/reference/male_a548408b-568e-54b3-a505-dd3fee33a1e7.svg"
AUTHOR = "claude-opus-5-5"


class ManWithLongCurlyHairAndBeard(Solo48):
    icon_id = "man-with-long-curly-hair-and-beard"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('male', 'bearded man')
    keywords = ('man', 'beard', 'curly hair', 'long hair', 'person', 'male')

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

        self.path("hair", (8, 29), [
            ("A", (8, 21), 5, 5, True),
            ("A", (11, 13), 5, 5, True),
            ("A", (18, 8), 5, 5, True),
            ("A", (30, 8), 10, 10, True),              # crown curl
            ("A", (37, 13), 5, 5, True),
            ("A", (40, 21), 5, 5, True),
            ("A", (40, 29), 5, 5, True),
        ])
        self.path("face", (22, 17), [
            ("L", (26, 17)),
            ("A", (30, 21), 4, 4, True),
            ("L", (30, 26)),
            ("L", (30, 31)),
            ("C", (24, 38), (30, 36), (28, 38)),       # beard
            ("C", (18, 31), (20, 38), (18, 36)),
            ("L", (18, 26)),
            ("L", (18, 21)),
            ("A", (22, 17), 4, 4, True),
        ], closed=True)
        self.add_line("moustache", (18, 26), (30, 26))
        self.relate("connect", "face", "moustache")
        self.add_bezier("shoulder-l", (18, 31), ((16, 37), (9, 37), (6, 42)))
        self.add_bezier("shoulder-r", (30, 31), ((32, 37), (39, 37), (42, 42)))
        self.relate("connect", "face", "shoulder-l")
        self.relate("connect", "face", "shoulder-r")
