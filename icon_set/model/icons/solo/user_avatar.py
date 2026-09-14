"""Circular head above open, rounded shoulders, informed by human_ref/user.svg.

Fresh SOLO48 construction on VRECT_L: visible bounds (6,2)-(42,46).
Head center (24,12), radius 8; shoulder top is derived from the shared gap.
The reference's circular head, short shoulder plateau and open bottom survive.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = None
SOURCE_PATH = "icon_set/references/human_ref/user.svg"
AUTHOR = "gpt-6"


class UserAvatar(Solo48):
    icon_id = "user-avatar"
    keyshape = Keyshape.VRECT_L
    aliases = ("account-avatar",)
    keywords = ("user", "person", "avatar", "profile", "account")

    def build(self) -> None:
        cx, cy, radius = 24, 12, 8
        points = [(cx, cy-radius), (cx+radius, cy), (cx, cy+radius),
                  (cx-radius, cy), (cx, cy-radius)]
        for i, (a, b) in enumerate(zip(points, points[1:])):
            self.add_arc(f"head-{i}", a, b, radius_x=radius)
        self.add_contour("head", *(f"head-{i}" for i in range(4)), closed=True)
        top = cy + radius + HEAD_BODY_CENTERLINE_GAP
        shoulder_radius = 12
        self.add_line("left-side", (8,44), (8,top+shoulder_radius))
        self.add_arc("left-shoulder", (8,top+shoulder_radius), (20,top), radius_x=shoulder_radius)
        self.add_line("shoulder-top", (20,top), (28,top))
        self.add_arc("right-shoulder", (28,top), (40,top+shoulder_radius), radius_x=shoulder_radius)
        self.add_line("right-side", (40,top+shoulder_radius), (40,44))
        self.add_contour("body", "left-side", "left-shoulder", "shoulder-top", "right-shoulder", "right-side")
