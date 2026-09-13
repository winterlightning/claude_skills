"""A front-facing cobra head with a broad rounded hood and dot eyes."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class CobraHeadFriendly(Solo48):
    icon_id = "cobra-head-friendly"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("cobra-head",)
    keywords = ("cobra", "snake", "reptile", "hood", "head", "friendly")

    def build(self) -> None:
        # VRECT_XL centerline extremes: (5, 2)–(43, 46).
        # Mirrored elliptical quadrants share horizontal/vertical tangents.
        self.add_arc("hood-upper-right", (24, 2), (43, 19),
                     radius_x=19, radius_y=17)
        self.add_arc("hood-lower-right", (43, 19), (33, 37),
                     radius_x=10, radius_y=18)
        self.add_arc("neck-turn-right", (33, 37), (30, 43),
                     radius_x=3, radius_y=6, sweep=False)
        self.add_line("neck-right", (30, 43), (30, 46))
        self.add_line("neck-base", (30, 46), (18, 46))
        self.add_line("neck-left", (18, 46), (18, 43))
        self.add_arc("neck-turn-left", (18, 43), (15, 37),
                     radius_x=3, radius_y=6, sweep=False)
        self.add_arc("hood-lower-left", (15, 37), (5, 19),
                     radius_x=10, radius_y=18)
        self.add_arc("hood-upper-left", (5, 19), (24, 2),
                     radius_x=19, radius_y=17)
        self.add_contour("hood", "hood-upper-right", "hood-lower-right",
                         "neck-turn-right", "neck-right", "neck-base", "neck-left",
                         "neck-turn-left", "hood-lower-left", "hood-upper-left", closed=True)
        self.add_line("face-left", (14, 13), (14, 23))
        self.add_arc("chin", (14, 23), (34, 23), radius_x=10, sweep=False)
        self.add_line("face-right", (34, 23), (34, 13))
        self.add_contour("face", "face-left", "chin", "face-right")
        self.add_dot("eye-left", (21, 20))
        self.add_dot("eye-right", (27, 20))
