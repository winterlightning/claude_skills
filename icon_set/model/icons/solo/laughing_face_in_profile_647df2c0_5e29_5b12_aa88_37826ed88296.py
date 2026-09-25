"""Laughing Face in Profile; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '647df2c0-5e29-5b12-aa88-37826ed88296'
SOURCE_PATH = 'pictographic-primitives/smileys/lol side_647df2c0-5e29-5b12-aa88-37826ed88296.svg'
AUTHOR = 'gpt-6'


class LaughingFaceInProfile(Solo48):
    icon_id = 'laughing-face-in-profile'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('laughing', 'profile', 'laugh', 'mouth', 'face', 'emoji')

    def build(self) -> None:

        # HRECT_XL: (2,6)-(46,42); rounded head and projecting left nose.
        self.add_arc("head-upper-left",(12,20),(28,8),radius_x=16,radius_y=12)
        self.add_arc("head-upper-right",(28,8),(44,24),radius_x=16)
        self.add_arc("head-lower",(44,24),(28,40),radius_x=16)
        self.add_arc("chin",(28,40),(16,36),radius_x=20)
        self.add_arc("lower-lip",(16,36),(28,26),radius_x=12,radius_y=10,sweep=False)
        self.add_line("upper-lip",(28,26),(4,26))
        self.add_line("nose",(4,26),(12,20))
        self.add_contour("head","head-upper-left","head-upper-right","head-lower","chin","lower-lip","upper-lip","nose",closed=True)
        self.add_line("eye",(24,17),(28,17))
