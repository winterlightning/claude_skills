"""Exploding Head; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b7b83d9-cb29-47fc-bdfd-7a84082e0931'
SOURCE_PATH = 'pictographic-primitives/smileys/explosion_5b7b83d9-cb29-47fc-bdfd-7a84082e0931.svg'
AUTHOR = 'gpt-6'


class ExplodingHead(Solo48):
    icon_id = 'exploding-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('exploding', 'head', 'shocked', 'burst', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE (4,4)-(44,44): scalloped burst is continuous with the open head.
        self.add_arc("blast-left-low",(12,22),(6,16),radius_x=6)
        self.add_arc("blast-left-top",(6,16),(12,10),radius_x=6)
        self.add_arc("blast-left-inner",(12,10),(16,14),radius_x=4)
        self.add_arc("blast-top",(16,14),(32,14),radius_x=8)
        self.add_arc("blast-right-inner",(32,14),(36,10),radius_x=4)
        self.add_arc("blast-right-top",(36,10),(42,16),radius_x=6)
        self.add_arc("blast-right-low",(42,16),(36,22),radius_x=6)
        self.add_line("temple-right",(36,22),(38,25))
        self.add_arc("jaw",(38,25),(10,25),radius_x=14,radius_y=17)
        self.add_line("temple-left",(10,25),(12,22))
        self.add_contour("outline","blast-left-low","blast-left-top","blast-left-inner","blast-top","blast-right-inner","blast-right-top","blast-right-low","temple-right","jaw","temple-left",closed=True)
        self.add_dot("eye-left",(20,21))
        self.add_dot("eye-right",(28,21))
        self.add_arc("mouth-top",(22,31),(26,31),radius_x=2)
        self.add_arc("mouth-bottom",(26,31),(22,31),radius_x=2)
        self.add_contour("mouth","mouth-top","mouth-bottom",closed=True)
