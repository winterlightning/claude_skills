"""Indian man portrait with a wrapped turban and crossing robe.

Symbol plan: the circular face carries the wrapped crown; a central node
owns the robe folds. The uneven turban fold follows the source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "ec6a97bf-8b79-5217-9903-4d323ef660ad"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-indian-avatar/20260926T175626Z-thuan-mac-1/reference/man indian_ec6a97bf-8b79-5217-9903-4d323ef660ad.svg"
AUTHOR = "gpt-6"


class ManIndianAvatar(Solo48):
    icon_id = "man-indian-avatar"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    categories = ("primitives", "avatars")
    aliases = ()
    keywords = ("man", "indian", "turban", "robe", "portrait")

    def build(self):
        cx, cy, r = 24, 14, 10
        self.add_arc("crown", (cx-r, cy), (cx+r, cy), radius_x=r)
        self.add_arc("jaw", (cx+r, cy), (cx-r, cy), radius_x=r)
        self.add_contour("head", "crown", "jaw", closed=True)
        self.add_bezier("turban-fold", (24, 4), ((34, 9), (26, 14), (14, 14)))
        self.relate("connect", "head", "turban-fold")

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
        self.add_line("robe-fold", (24, 40), (14, 44))
        self.relate("connect", "robe-neck", "body-top")
        self.relate("connect", "robe-neck", "body-top-right")
        self.relate("connect", "robe-neck", "robe-fold")
