"""A round head sits over a smoothly rounded heart torso; no facial detail.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47cc7b06-fb55-4dfc-8ad0-470fd29f4a23'
SOURCE_PATH = 'pictographic-primitives/romance/phone digital well being heart_47cc7b06-fb55-4dfc-8ad0-470fd29f4a23.svg'
AUTHOR = 'gpt-6'


class PersonWithRoundedHeartTorso(Solo48):
    icon_id = 'person-with-rounded-heart-torso'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('person', 'heart', 'love', 'care', 'wellbeing', 'romance')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        self.add_arc('head-r',(24,4),(24,14),radius_x=5)
        self.add_arc('head-l',(24,14),(24,4),radius_x=5)
        self.add_contour('head','head-r','head-l',closed=True)
        heart('torso',24,30,8,44)
