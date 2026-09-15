"""Three heart blooms on uneven branches grow from a square pot; tiny leaf twists omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e88fb37a-e605-4d7e-a557-9e046dcb12ba'
SOURCE_PATH = 'pictographic-primitives/romance/love plant_e88fb37a-e605-4d7e-a557-9e046dcb12ba.svg'
AUTHOR = 'gpt-6'


class ThreeHeartPlantInSquarePot(Solo48):
    icon_id = 'three-heart-plant-in-square-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'plant', 'pot', 'branch', 'flower', 'romance')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        heart('centre',24,8,4,20)
        heart('left',14,26,3,34)
        heart('right',34,24,3,32)
        self.add_line('stem-upper',(24,20),(24,30))
        self.add_line('stem-lower',(24,30),(24,34))
        self.add_contour('stem','stem-upper','stem-lower')
        self.add_line('branch-l',(14,34),(24,30))
        self.add_line('branch-r',(34,32),(24,30))
        self.relate('connect','centre','stem')
        self.relate('connect','left','branch-l')
        self.relate('connect','right','branch-r')
        self.relate('connect','branch-l','stem')
        self.relate('connect','branch-r','stem')
        self.relate('connect','branch-l','branch-r')
        self.add_polyline('pot',(19,34),(24,34),(29,34),(29,44),(19,44),closed=True)
        self.relate('connect','stem','pot')
