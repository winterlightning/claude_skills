"""A gamepad with rounded grips, a D-pad and one button."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "1bb86543-aae8-452c-8b45-50bb1efcab26"
SOURCE_PATH = "pictographic-primitives/medias/gaming_1bb86543-aae8-452c-8b45-50bb1efcab26.svg"
AUTHOR = "gpt-6"

class GamepadDpadAndButton(Solo48):
    icon_id = "gamepad-dpad-and-button-1bb86543-aae8-452c-8b45-50bb1efcab26"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ("game controller",)
    keywords = ("gaming", "console", "gamepad", "d-pad")

    def build(self):
        # Plan: mirrored shell about x=24; tangent elliptical shoulders,
        # equal semicircular grips and a reverse notch. Asymmetric controls
        # are intrinsic. Lucide gamepad-2 informs the grips and simple cross.
        # HRECT_L centerline extremes: (4,8)-(44,40).
        axis, left, right, top, baseline = 24, 4, 44, 8, 32
        shoulder_x, grip_radius, notch_radius = 14, 8, 4
        mirror = lambda x: 2 * axis - x
        self.add_line("top", (shoulder_x, top), (mirror(shoulder_x), top))
        self.add_arc("right-shoulder", (mirror(shoulder_x), top), (right, baseline), radius_x=10, radius_y=24)
        self.add_arc("right-grip", (right, baseline), (axis+notch_radius, baseline), radius_x=grip_radius)
        self.add_arc("notch", (axis+notch_radius, baseline), (axis-notch_radius, baseline), radius_x=notch_radius, radius_y=1, sweep=False)
        self.add_arc("left-grip", (axis-notch_radius, baseline), (left, baseline), radius_x=grip_radius)
        self.add_arc("left-shoulder", (left, baseline), (shoulder_x, top), radius_x=10, radius_y=24)
        self.add_contour("shell", "top", "right-shoulder", "right-grip", "notch", "left-grip", "left-shoulder", closed=True)
        cx, cy, arm = 17, 21, 3
        for label, endpoint in (("left",(cx-arm,cy)),("right",(cx+arm,cy)),("top",(cx,cy-arm)),("bottom",(cx,cy+arm))):
            self.add_line("dpad-"+label, (cx,cy), endpoint)
        self.relate("connect", "dpad-left", "dpad-right", "dpad-top", "dpad-bottom")
        self.add_dot("button", (33,21))
