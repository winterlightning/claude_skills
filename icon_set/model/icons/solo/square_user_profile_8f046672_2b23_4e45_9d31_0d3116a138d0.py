"""A square user profile containing a detached head and shoulders."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "8f046672-2b23-4e45-9d31-0d3116a138d0"
SOURCE_PATH = "pictographic-primitives/other/square person_8f046672-2b23-4e45-9d31-0d3116a138d0.svg"
AUTHOR = "gpt-6"


class SquareUserProfile(Solo48):
    icon_id = "square-user-profile"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ("user avatar frame", "square person")
    keywords = ("profile", "account", "portrait", "user")

    def build(self) -> None:
        # Frame: paired corners and a shared central axis.
        axis_x = 24
        left, right = 6, 2 * axis_x - 6
        radius = 2
        self.add_line("frame-top", (8, 6), (40, 6))
        self.add_arc("frame-ne", (40, 6), (right, 8), radius_x=radius)
        self.add_line("frame-right", (right, 8), (right, 40))
        self.add_arc("frame-se", (right, 40), (40, 42), radius_x=radius)
        self.add_line("frame-bottom", (40, 42), (8, 42))
        self.add_arc("frame-sw", (8, 42), (left, 40), radius_x=radius)
        self.add_line("frame-left", (left, 40), (left, 8))
        self.add_arc("frame-nw", (left, 8), (8, 6), radius_x=radius)
        self.add_contour("square-frame", "frame-top", "frame-ne", "frame-right",
                         "frame-se", "frame-bottom", "frame-sw", "frame-left",
                         "frame-nw", closed=True)

        # Shared human user reference: circular head, smooth open shoulders.
        # Head bottom y=23 and shoulder crest y=31 give exactly 8 centerline
        # units, hence 4 units of visible ink clearance.
        self.add_arc("head-right", (24, 15), (24, 23), radius_x=4)
        self.add_arc("head-left", (24, 23), (24, 15), radius_x=4)
        self.add_contour("head", "head-right", "head-left", closed=True)
        self.add_arc("shoulder-left", (15, 33), (24, 31),
                     radius_x=9, radius_y=2)
        self.add_arc("shoulder-right", (24, 31), (33, 33),
                     radius_x=9, radius_y=2)
        self.add_contour("shoulders", "shoulder-left", "shoulder-right")
