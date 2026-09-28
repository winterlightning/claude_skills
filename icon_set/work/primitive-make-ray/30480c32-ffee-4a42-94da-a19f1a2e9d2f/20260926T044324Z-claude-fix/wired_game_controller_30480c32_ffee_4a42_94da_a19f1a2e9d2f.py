"""A wired game controller (joystick pad): a gamepad with two grips, a d-pad and two
buttons, its cable rising from the top.

Symbol plan: the pad is one closed outline, mirrored about x=24 in its silhouette: a flat
top (y=12) with rounded shoulders, straight sides, two rounded grips reaching the bottom
edge and an inner arch rising to y=34 between them. The cable is a straight stroke from
the top centre to the top edge. Inside, the d-pad is a plus (arms 3) over the left grip
and the two buttons are dots on a diagonal over the right grip, each 8+ from the outline
and 8.5 from each other.
Lucide construction: 'gamepad-2' - rounded pad with grips, plus-shaped d-pad and round
buttons.
Keyshape HRECT_L: centerline x 4..44 (pad sides), y 8..40 (cable top, grips).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "30480c32-ffee-4a42-94da-a19f1a2e9d2f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__wired-game-controller/20260926T044250Z-thuan-mac/reference/joystick_30480c32-ffee-4a42-94da-a19f1a2e9d2f.svg"
AUTHOR = "claude-opus-5-5"


class WiredGameController(Solo48):
    icon_id = "wired-game-controller"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/gaming"
    aliases = ("joystick", "gamepad", "game-pad")
    keywords = ("game", "controller", "gamepad", "joystick", "gaming", "play", "console", "video-game")

    def build(self) -> None:
        self.add_line("top-left", (10, 12), (24, 12))
        self.add_line("top-right", (24, 12), (38, 12))
        self.add_bezier("pad-right", (38, 12),
                        ((41.5, 12), (44, 14.5), (44, 18)),
                        ((44, 23), (44, 28), (44, 32)),
                        ((44, 37), (42.5, 40), (39, 40)),
                        ((35, 40), (33, 38), (30, 35.5)),
                        ((28, 34.5), (26, 34), (24, 34)))
        self.add_bezier("pad-left", (24, 34),
                        ((22, 34), (20, 34.5), (18, 35.5)),
                        ((15, 38), (13, 40), (9, 40)),
                        ((5.5, 40), (4, 37), (4, 32)),
                        ((4, 28), (4, 23), (4, 18)),
                        ((4, 14.5), (6.5, 12), (10, 12)))
        self.add_contour("pad", "top-right", "pad-right", "pad-left", "top-left", closed=True)
        self.add_line("cable", (24, 12), (24, 8))
        self.relate("connect", "pad", "cable")
        self.add_line("dpad-h", (13, 24), (19, 24))
        self.add_line("dpad-v", (16, 21), (16, 27))
        self.relate("connect", "dpad-h", "dpad-v")
        self.add_dot("button-a", (29, 21))
        self.add_dot("button-b", (35, 27))
