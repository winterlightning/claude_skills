"""An open laptop with a broad blank display and flared lower base.

Symbol plan: a symmetric continuous silhouette and a horizontal screen hinge.
HRECT_L centerline extremes x=4..44, y=8..40.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "c6dfac97-4fee-491d-98ff-6b8270bde0ae"
SOURCE_PATH = "pictographic-primitives/_uncategorized_24/laptop project screen_c6dfac97-4fee-491d-98ff-6b8270bde0ae.svg"
AUTHOR = "gpt-6"


class OpenLaptopComputer(Solo48):
    icon_id = "open-laptop-computer"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("laptop", "notebook computer")
    keywords = ("computer", "laptop", "screen", "keyboard", "device")

    def build(self) -> None:
        self.add_line("top", (10, 8), (38, 8))
        self.add_arc("top-right", (38, 8), (42, 12), radius_x=4)
        self.add_line("right-screen", (42, 12), (42, 32))
        self.add_line("right-base-slope", (42, 32), (44, 38))
        self.add_arc("base-right", (44, 38), (42, 40), radius_x=2)
        self.add_line("base-bottom", (42, 40), (6, 40))
        self.add_arc("base-left", (6, 40), (4, 38), radius_x=2)
        self.add_line("left-base-slope", (4, 38), (6, 32))
        self.add_line("left-screen", (6, 32), (6, 12))
        self.add_arc("top-left", (6, 12), (10, 8), radius_x=4)
        self.add_contour("laptop-outline", "top", "top-right", "right-screen", "right-base-slope", "base-right", "base-bottom", "base-left", "left-base-slope", "left-screen", "top-left", closed=True)
        self.add_line("screen-hinge", (6, 32), (42, 32))
        self.relate("connect", "screen-hinge", "laptop-outline")
