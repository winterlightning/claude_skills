"""Front-facing dog with two tall upright ears and a broad rounded jaw."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class DogFaceTallEars(Solo48):
    icon_id = "dog-face-tall-ears"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/mammals"
    aliases = ("dog face", "upright-ear dog")
    keywords = ("dog", "canine", "pet", "face", "tall ears", "lucide")

    def build(self) -> None:
        # VRECT_XL centerline extremes: (5, 2) through (43, 46).
        # Paired features mirror across x=24; ears are intrinsic to the head.
        self.add_line("left-ear-outer", (5, 28), (5, 2))
        self.add_line("left-ear-inner", (5, 2), (18, 17))
        self.add_line("forehead", (18, 17), (30, 17))
        self.add_line("right-ear-inner", (30, 17), (43, 2))
        self.add_line("right-ear-outer", (43, 2), (43, 28))
        self.add_arc("right-jaw", (43, 28), (25, 46), radius_x=18)
        self.add_line("chin", (25, 46), (23, 46))
        self.add_arc("left-jaw", (23, 46), (5, 28), radius_x=18)
        self.add_contour(
            "head", "left-ear-outer", "left-ear-inner", "forehead",
            "right-ear-inner", "right-ear-outer", "right-jaw", "chin",
            "left-jaw", closed=True,
        )
        self.add_dot("left-eye", (15, 26))
        self.add_dot("right-eye", (33, 26))
        self.add_polyline("nose", (21, 35), (24, 37), (27, 35))
