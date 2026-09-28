"""A round head sits over an angular heart torso; no facial detail.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2aa1a351-da44-44d3-bef9-70273bc4350d'
SOURCE_PATH = 'pictographic-primitives/romance/phone digital well being heart 1_2aa1a351-da44-44d3-bef9-70273bc4350d.svg'
AUTHOR = 'gpt-6'


class PersonWithAngularHeartTorso(Solo48):
    icon_id = 'person-with-angular-heart-torso'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('person', 'heart', 'love', 'care', 'wellbeing', 'romance')

    def build(self) -> None:
        self.add_arc('head-r',(24,4),(24,14),radius_x=5)
        self.add_arc('head-l',(24,14),(24,4),radius_x=5)
        self.add_contour('head','head-r','head-l',closed=True)
        self.add_polyline('torso',(24,30),(18,24),(12,24),(8,28),(12,34),(24,44),(36,34),(40,28),(36,24),(30,24),closed=True)
