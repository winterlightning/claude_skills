"""Anxious Face with Sweat; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10d035a4-5788-550b-80e5-d9a043b07789'
SOURCE_PATH = 'pictographic-primitives/smileys/in trouble_10d035a4-5788-550b-80e5-d9a043b07789.svg'
AUTHOR = 'gpt-6'


class AnxiousFaceWithSweat(Solo48):
    icon_id = 'anxious-face-with-sweat'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('anxious', 'sweat', 'worried', 'nervous', 'face', 'emoji')

    def build(self) -> None:

        # Open upper-right outline makes room for a physical bead of sweat.
        self.add_arc("head-upper-left",(24,4),(4,24),radius_x=20,sweep=False)
        self.add_arc("head-lower",(4,24),(44,24),radius_x=20,sweep=False)
        self.add_contour("head","head-upper-left","head-lower")
        self.add_line("drop-left",(36,8),(32,15))
        self.add_arc("drop-bottom",(32,15),(40,15),radius_x=4,sweep=False)
        self.add_line("drop-right",(40,15),(36,8))
        self.add_contour("sweat","drop-left","drop-bottom","drop-right",closed=True)
        self.add_dot("eye-left",(17,21))
        self.add_dot("eye-right",(27,23))
        self.add_arc("frown",(18,34),(30,34),radius_x=9)
