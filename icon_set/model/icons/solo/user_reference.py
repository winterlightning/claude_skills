"""Reference user: circular head and open, smoothly rounded shoulders.

SOLO48 VRECT_L centerline extremes (8,4)-(40,44). Human user.svg
owns the proportions; Lucide user-round supplies only the circle/arch idiom.
Plan: one circle and one open shoulder contour, mirrored about x=24.
The head ends at y=22 and shoulders begin at y=30: 8 centerline, 4 ink.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = "icon_set/references/human_ref/user.svg"
AUTHOR = "gpt-6"


class UserReference(Solo48):
    icon_id = "user-reference"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users",)
    aliases = ()
    keywords = ("human", "user", "person", "account", "avatar")

    def build(self) -> None:
        axis, cy, radius = 24, 13, 9
        gap, stroke = 4, 4
        shoulder_y = cy + radius + stroke + gap
        self.add_arc("head-top", (axis-radius, cy), (axis+radius, cy), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius, cy), (axis-radius, cy), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        left, right, shoulder_radius, base_y = 8, 40, 12, 44
        side_y = shoulder_y + shoulder_radius
        self.add_line("left-side", (left, base_y), (left, side_y))
        self.add_arc("left-shoulder", (left, side_y), (left+shoulder_radius, shoulder_y), radius_x=shoulder_radius)
        self.add_line("shoulder-top", (left+shoulder_radius, shoulder_y), (right-shoulder_radius, shoulder_y))
        self.add_arc("right-shoulder", (right-shoulder_radius, shoulder_y), (right, side_y), radius_x=shoulder_radius)
        self.add_line("right-side", (right, side_y), (right, base_y))
        self.add_contour("body", "left-side", "left-shoulder", "shoulder-top", "right-shoulder", "right-side")
