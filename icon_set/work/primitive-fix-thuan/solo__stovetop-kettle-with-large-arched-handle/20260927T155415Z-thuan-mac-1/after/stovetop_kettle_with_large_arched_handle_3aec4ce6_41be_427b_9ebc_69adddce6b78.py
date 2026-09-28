"""Stovetop kettle with a large arched handle, authored on SOLO48.

Plan: SQUARE centerline box (6,6)-(42,42), kettle axis x=27 (the spout takes the
left margin). Handle = r10 semicircle about (27,16) (top on y=6) with legs dropping
to the shoulders (17,28)/(37,28). Lid = rx10/ry7 dome over the lid line y=28 with a
short knob nub on its crown (a ring knob read as an eye). Body = the right shoulder
flaring as a cubic to a vertical wall at x=42, r3 bottom corners, left wall x=12.
The spout occludes the upper left body side: its top edge leaves the left shoulder
and its bottom edge returns to the left wall, tip at (6,22), 8+ clear of the handle leg.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3aec4ce6-41be-427b-9ebc-69adddce6b78"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__stovetop-kettle-with-large-arched-handle/20260927T155415Z-thuan-mac-1/reference/tea kettle 1_3aec4ce6-41be-427b-9ebc-69adddce6b78.svg"
AUTHOR = "claude-opus-5-5"


class StovetopKettleWithLargeArchedHandle(Solo48):
    icon_id = "stovetop-kettle-with-large-arched-handle"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("food", "primitives")
    aliases = ("tea kettle",)
    keywords = ("kettle", "tea", "stovetop", "boil", "water", "kitchen", "handle")

    def build(self) -> None:
        ax, lid, bottom = 27, 28, 42
        SL, SR = (17, lid), (37, lid)
        tip, wall_top = (6, 22), (12, 38)
        # Handle
        self.add_line("handle-leg-left", SL, (17, 16))
        self.add_arc("handle-arch", (17, 16), (37, 16), radius_x=10)
        self.add_line("handle-leg-right", (37, 16), SR)
        self.add_contour("handle", "handle-leg-left", "handle-arch", "handle-leg-right")
        # Lid
        self.add_arc("lid-dome-left", SL, (ax, 21), radius_x=10, radius_y=7)
        self.add_arc("lid-dome-right", (ax, 21), SR, radius_x=10, radius_y=7)
        self.add_contour("lid-dome", "lid-dome-left", "lid-dome-right")
        self.add_line("lid-knob", (ax, 21), (ax, 17))
        self.add_line("lid-line", SL, SR)
        # Body and spout: one outline from the right shoulder round to the left shoulder
        self.add_bezier("body-side-right", SR, ((40, 29), (42, 32), (42, 38)))
        self.add_line("body-wall-right", (42, 38), (42, 39))
        self.add_arc("body-corner-right", (42, 39), (39, bottom), radius_x=3)
        self.add_line("body-bottom", (39, bottom), (15, bottom))
        self.add_arc("body-corner-left", (15, bottom), (12, 39), radius_x=3)
        self.add_line("body-wall-left", (12, 39), wall_top)
        self.add_line("spout-bottom", wall_top, tip)
        self.add_line("spout-top", tip, SL)
        self.add_contour("body", "body-side-right", "body-wall-right", "body-corner-right", "body-bottom",
                         "body-corner-left", "body-wall-left", "spout-bottom", "spout-top")
        self.relate("connect", "handle", "lid-dome", "lid-knob", "lid-line", "body")
