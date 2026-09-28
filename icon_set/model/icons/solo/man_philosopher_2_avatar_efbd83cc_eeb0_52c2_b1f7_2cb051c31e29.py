"""Bald, bearded philosopher bust based on the original portrait.

Symbol plan: circular bald cranium and jaw share an axis; the beard boundary
is a connected wave. Mirrored robe folds converge at the center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "efbd83cc-eeb0-52c2-b1f7-2cb051c31e29"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-philosopher-2-avatar/20260926T175626Z-thuan-mac-1/reference/man philosopher_efbd83cc-eeb0-52c2-b1f7-2cb051c31e29.svg"
AUTHOR = "gpt-6"


class ManPhilosopher2Avatar(Solo48):
    icon_id = "man-philosopher-2-avatar-solo"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    categories = ("primitives", "avatars")
    aliases = ()
    keywords = ("man", "philosopher", "bald", "beard", "portrait")

    def build(self):
        cx, cy, r = 24, 14, 10
        self.add_arc("bald-crown", (cx-r, cy), (cx+r, cy), radius_x=r)
        self.add_arc("jaw", (cx+r, cy), (cx-r, cy), radius_x=r)
        self.add_contour("head", "bald-crown", "jaw", closed=True)
        self.add_bezier("beard-wave", (14, 14), ((18, 18), (21, 14), (24, 14)), ((27, 14), (30, 18), (34, 14)))
        self.relate("connect", "head", "beard-wave")

        top = cy + r + HEAD_BODY_CENTERLINE_GAP
        self.add_line("left-side", (8, 44), (8, 42))
        self.add_arc("left-shoulder", (8, 42), (16, top), radius_x=8, radius_y=42-top)
        self.add_contour("body-left", "left-side", "left-shoulder")
        self.add_line("body-top", (16, top), (24, top))
        self.add_line("body-top-right", (24, top), (32, top))
        self.add_arc("right-shoulder", (32, top), (40, 42), radius_x=8, radius_y=42-top)
        self.add_line("right-side", (40, 42), (40, 44))
        self.add_contour("body-right", "right-shoulder", "right-side")
        self.relate("connect", "body-left", "body-top")
        self.relate("connect", "body-top", "body-top-right")
        self.relate("connect", "body-top-right", "body-right")
        self.relate("connect", "head", "body-top")
        self.relate("connect", "head", "body-top-right")
        self.add_polyline("robe-neck", (16, top), (24, 40), (32, top))
        self.relate("connect", "robe-neck", "body-top")
        self.relate("connect", "robe-neck", "body-top-right")
