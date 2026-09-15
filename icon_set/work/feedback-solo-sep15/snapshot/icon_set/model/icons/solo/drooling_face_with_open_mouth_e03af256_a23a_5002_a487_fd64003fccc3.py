"""Drooling Face with Open Mouth. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e03af256-a23a-5002-a487-fd64003fccc3'
SOURCE_PATH = 'pictographic-primitives/smileys/drool_e03af256-a23a-5002-a487-fd64003fccc3.svg'
AUTHOR = 'gpt-6'


class DroolingFaceWithOpenMouth(Solo48):
    icon_id = 'drooling-face-with-open-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('drooling', 'drool', 'mouth', 'hungry', 'face', 'emoji')

    def build(self) -> None:

        # Circle envelope: center (24,24), radius 20; extremes 4 and 44.
        axis, radius = 24, 20
        self.add_arc("head-top", (axis-radius,24), (axis+radius,24), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,24), (axis-radius,24), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        for side,x in (("left",17),("right",31)):
            self.add_arc(f"eye-{side}",(x-2,17),(x+2,17),radius_x=2)
        self.add_arc("mouth-top",(18,29),(30,29),radius_x=6,radius_y=4)
        self.add_line("mouth-right",(30,29),(30,31))
        self.add_arc("mouth-corner-right",(30,31),(28,33),radius_x=2)
        self.add_line("lip-right",(28,33),(27,33))
        self.add_line("lip-left",(27,33),(20,33))
        self.add_arc("mouth-corner-left",(20,33),(18,31),radius_x=2)
        self.add_line("mouth-left",(18,31),(18,29))
        self.add_contour("mouth","mouth-top","mouth-right","mouth-corner-right","lip-right","lip-left","mouth-corner-left","mouth-left",closed=True)
        self.add_line("drool",(27,33),(27,35))
        self.relate("connect","drool","lip-right")
        self.relate("connect","drool","lip-left")
