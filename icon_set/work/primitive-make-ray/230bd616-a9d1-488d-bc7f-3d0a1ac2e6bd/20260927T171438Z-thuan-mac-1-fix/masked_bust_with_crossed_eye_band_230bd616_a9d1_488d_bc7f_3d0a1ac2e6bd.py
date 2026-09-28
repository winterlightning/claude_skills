"""Masked bust: bald head with a crossed eye band (thief).

Plan: mirrored about x=24. Oval head with a domed cap (half ellipse rx 13,
ry 11), straight temples x=11/37 (y 15-23) and a jaw curving to the chin.
The eye band is drawn as in the reference: its top edge is a shallow V and
its bottom edge a shallow Lambda, both passing through the centre node
C=(24,19) and anchored on the temple vertices, which makes two long lens
eye-holes. Shoulders are a rounded arch 9 below the chin. Frown and neck
dropped: no 8u room below the band at 48. Keyshape VRECT_L.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "230bd616-a9d1-488d-bc7f-3d0a1ac2e6bd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__masked-bust-with-crossed-eye-band/20260927T164623Z-thuan-mac-1/reference/man thief 1_230bd616-a9d1-488d-bc7f-3d0a1ac2e6bd.svg"
AUTHOR = "claude-opus-5-5"


class MaskedBustWithCrossedEyeBand(Solo48):
    icon_id = "masked-bust-with-crossed-eye-band"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('man thief', 'burglar', 'robber')
    keywords = ('thief', 'mask', 'burglar', 'robber', 'crime', 'person')

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

        self.path("head", (11, 15), [
            ("A", (37, 15), 13, 11, True),             # domed cap
            ("L", (37, 23)),
            ("C", (24, 30), (37, 27), (30, 30)),       # jaw
            ("C", (11, 23), (18, 30), (11, 27)),
            ("L", (11, 15)),
        ], closed=True)
        c = (24, 19)
        self.add_bezier("band-tl", (11, 15), ((16, 16), (20, 18), c))
        self.add_bezier("band-tr", c, ((28, 18), (32, 16), (37, 15)))
        self.add_bezier("band-bl", (11, 23), ((16, 22), (20, 20), c))
        self.add_bezier("band-br", c, ((28, 20), (32, 22), (37, 23)))
        self.add_contour("band-top", "band-tl", "band-tr")
        self.add_contour("band-bottom", "band-bl", "band-br")
        for part in ("band-top", "band-bottom"):
            self.relate("connect", "head", part)
        self.relate("connect", "band-top", "band-bottom")
        self.path("shoulders", (8, 44), [
            ("A", (13, 39), 5, 5, True),
            ("L", (35, 39)),
            ("A", (40, 44), 5, 5, True),
        ])
