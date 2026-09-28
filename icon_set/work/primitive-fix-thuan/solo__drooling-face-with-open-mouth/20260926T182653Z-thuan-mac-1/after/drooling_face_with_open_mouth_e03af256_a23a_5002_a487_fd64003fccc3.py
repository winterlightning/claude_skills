"""Drooling face with open mouth: a round face with happy closed eyes and a wide
open mouth, a drop of drool hanging from it.

Revision (disapproved, reason not recorded): the rejected drawing had wide-open
dot eyes and a small ring mouth, so it read as a surprised "oh" face; the
original's eyes are closed happy arcs and the mouth is a wide open D with drool
hanging below. The happy closed eyes, the wide open mouth and the drool are
restored.

Symbol plan: mirror axis x=24. Face: radius-20 circle about (24,24). Eyes:
radius-2 upper arcs about (17,17)/(31,17), 8.6 inside the rim. Mouth: open D, a
straight top (17,26)-(31,26), 9 below the eyes, over a radius-7 bowl (bottom 33). Drool: a
drop from the bowl's lowest point (24,33) to (24,35), 9 inside the rim.
Omissions: the tongue outline (a closed tongue inside the mouth cannot clear the
hole minimum) and a longer drool run (it must stay 8 from the rim).
Lucide construction: 'laugh' face (arc eyes, D mouth).
Keyshape CIRCLE: rim radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e03af256-a23a-5002-a487-fd64003fccc3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__drooling-face-with-open-mouth/20260926T182653Z-thuan-mac-1/reference/drool_e03af256-a23a-5002-a487-fd64003fccc3.svg"
AUTHOR = "claude-opus-5-5"

C = 24


class DroolingFaceWithOpenMouth(Solo48):
    icon_id = "drooling-face-with-open-mouth"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emotions/faces"
    aliases = ("drool", "drooling-face")
    keywords = ("drool", "drooling", "face", "hungry", "yummy", "emoji", "mouth", "smiley")

    def build(self) -> None:
        self.add_arc("rim-top", (C - 20, C), (C + 20, C), radius_x=20)
        self.add_arc("rim-bottom", (C + 20, C), (C - 20, C), radius_x=20)
        self.add_contour("rim", "rim-top", "rim-bottom", closed=True)
        for name, x in (("eye-left", 17), ("eye-right", 31)):
            self.add_arc(name, (x - 2, 17), (x + 2, 17), radius_x=2)
        self.add_line("mouth-top", (17, 26), (31, 26))
        self.add_arc("mouth-bowl-right", (31, 26), (C, 33), radius_x=7)
        self.add_arc("mouth-bowl-left", (C, 33), (17, 26), radius_x=7)
        self.add_contour("mouth", "mouth-top", "mouth-bowl-right", "mouth-bowl-left", closed=True)
        self.add_line("drool", (C, 33), (C, 35))
        self.relate("connect", "mouth", "drool")
