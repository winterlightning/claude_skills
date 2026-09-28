"""Horned Demon Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b3e332a-d46c-498c-b0ae-13caae896b54'
SOURCE_PATH = 'pictographic-primitives/smileys/smiley face horns demon_5b3e332a-d46c-498c-b0ae-13caae896b54.svg'
AUTHOR = 'gpt-6'


class HornedDemonFace(Solo48):
    icon_id = 'horned-demon-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('demon', 'horns', 'devil', 'head', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE (4,4)-(44,44): two pointed horns and a round lower head.
        self.add_arc("horn-left-inner",(6,6),(16,14),radius_x=10,radius_y=8,sweep=False)
        self.add_arc("crown",(16,14),(32,14),radius_x=16,radius_y=14)
        self.add_arc("horn-right-inner",(32,14),(42,6),radius_x=10,radius_y=8,sweep=False)
        self.add_line("horn-right-outer",(42,6),(40,26))
        self.add_arc("jaw",(40,26),(8,26),radius_x=16)
        self.add_line("horn-left-outer",(8,26),(6,6))
        self.add_contour("head","horn-left-inner","crown","horn-right-inner","horn-right-outer","jaw","horn-left-outer",closed=True)
        for side,sign in (("left",1),("right",-1)):
            self.add_arc(f"eye-{side}",(24+sign*(17-24),24),(24+sign*(19-24),26),radius_x=5,sweep=sign>0)
