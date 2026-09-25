"""Thumbs-Up Hand; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45a32cd8-6637-575c-a11f-97d53235e4cf'
SOURCE_PATH = 'pictographic-primitives/smileys/liked_45a32cd8-6637-575c-a11f-97d53235e4cf.svg'
AUTHOR = 'gpt-6'


class ThumbsUpHand(Solo48):
    icon_id = 'thumbs-up-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('thumb', 'hand', 'approval', 'gesture', 'hand sign')

    def build(self) -> None:

        # SQUARE: ink (4,4)-(44,44). Rounded thumb and fist, with one cuff seam.
        self.add_line("cuff-top",(6,24),(14,24))
        self.add_line("thumb-rise",(14,24),(22,14))
        self.add_line("thumb-tip-left",(22,14),(22,6))
        self.add_arc("thumb-tip",(22,6),(32,16),radius_x=10)
        self.add_line("thumb-inner",(32,16),(30,24))
        self.add_line("fist-top",(30,24),(38,24))
        self.add_arc("fist-corner",(38,24),(42,28),radius_x=4)
        self.add_line("fist-edge",(42,28),(39,38))
        self.add_arc("fist-bottom",(39,38),(35,42),radius_x=4)
        self.add_line("palm-bottom",(35,42),(14,42))
        self.add_line("cuff-bottom",(14,42),(6,42))
        self.add_line("cuff-left",(6,42),(6,24))
        self.add_contour("hand","cuff-top","thumb-rise","thumb-tip-left","thumb-tip","thumb-inner","fist-top","fist-corner","fist-edge","fist-bottom","palm-bottom","cuff-bottom","cuff-left",closed=True)
        self.add_line("cuff-seam",(14,24),(14,42))
        for member in ("cuff-top","thumb-rise","palm-bottom","cuff-bottom"):
            self.relate("connect","cuff-seam",member)
