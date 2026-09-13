"""A friendly cat paw print reduced to four toes and one soft central pad."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class CatPawPrint(Solo48):
    icon_id = "cat-paw-print"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ("feline paw print",)
    keywords = ("cat", "paw", "pet", "kitten", "footprint", "animal")

    def build(self) -> None:
        # Square centerline extremes: (2, 2)-(46, 46), mirrored about x=24.
        # Lucide paw-print informs the spare circular toes and coherent arcs.
        for name, x, y in (
            ("toe-outer-left", 7, 21),
            ("toe-inner-left", 15, 7),
            ("toe-inner-right", 33, 7),
            ("toe-outer-right", 41, 21),
        ):
            self.add_arc(name + "-top", (x - 5, y), (x + 5, y), radius_x=5)
            self.add_arc(name + "-bottom", (x + 5, y), (x - 5, y), radius_x=5)
            self.add_contour(name, name + "-top", name + "-bottom", closed=True)

        # Two elliptical halves share vertical tangents at the widest points.
        self.add_arc("pad-crown", (14, 39), (34, 39), radius_x=10, radius_y=12)
        self.add_arc("pad-base", (34, 39), (14, 39), radius_x=10, radius_y=7)
        self.add_contour("pad", "pad-crown", "pad-base", closed=True)
