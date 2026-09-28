"""Left-facing woman's head with long swept hair.

Plan: one open silhouette from the neck front over the face profile (chin, lips,
pointed nose, brow), across the crown and down the long hair to the bottom
edge; one swept hairline branches from the forehead top, runs back over the
head and falls behind the jaw to the bottom. Smooth cubic flow replaces the
earlier stepped, boxy profile. Keyshape VRECT_L: nose x=8, hair x=40, crown
y=4, bottom y=44.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5a0aa177-0676-4a70-8fca-aebbf095a22b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__left-facing-woman-with-swept-long-hair/20260927T164623Z-thuan-mac-1/reference/soprano_5a0aa177-0676-4a70-8fca-aebbf095a22b.svg"
AUTHOR = "claude-opus-5-5"


class LeftFacingWomanWithSweptLongHair(Solo48):
    icon_id = "left-facing-woman-with-swept-long-hair"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("soprano", "woman profile")
    keywords = ("woman", "profile", "head", "long hair", "singer", "soprano")

    def path(self, name, start, steps, closed=False):
        here, members = start, []
        for j, (kind, end, *args) in enumerate(steps):
            member = f"{name}-{j}"
            if kind == "L":
                self.add_line(member, here, end)
            elif kind == "A":
                self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
            else:
                self.add_bezier(member, here, (args[0], args[1], end))
            here = end
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        self.path("outline", (19, 44), [
            ("L", (19, 37)),
            ("C", (12, 32), (19, 34), (14, 34)),       # jaw to chin
            ("C", (11, 27), (10.5, 30.5), (11.5, 28.5)),  # chin to lips
            ("L", (8, 23)),                            # under the nose
            ("L", (12, 16)),                           # nose bridge
            ("C", (17, 8), (13.6, 13.2), (15.2, 9.2)),  # forehead, tangent to the bridge
            ("C", (26, 4), (21.5, 5), (23, 4)),        # crown
            ("C", (38, 16), (33, 4), (38, 9)),         # back of head
            ("L", (38, 30)),
            ("C", (40, 44), (38, 36), (40, 40)),       # long hair
        ])
        self.path("hairline", (17, 8), [
            ("C", (28, 20), (22, 11), (28, 14)),
            ("L", (28, 30)),
            ("C", (31, 44), (28, 37), (31, 40)),
        ])
        self.relate("connect", "outline", "hairline")
