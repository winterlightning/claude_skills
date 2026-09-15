"""Three heart blooms rise from a shallow planter. Small feet and double rim are omitted.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80c91df2-deb2-4ace-944d-db4ce890e12f'
SOURCE_PATH = 'pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg'
AUTHOR = 'gpt-6'


class ThreeHeartPlantInShallowPot(Solo48):
    icon_id = 'three-heart-plant-in-shallow-pot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'plant', 'pot', 'flower', 'romance', 'growth')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        heart('centre',24,10,4,22)
        heart('left',14,24,4,32)
        heart('right',34,24,4,32)
        self.add_line('stem-c',(24,22),(24,34))
        self.add_line('stem-l',(14,32),(14,34))
        self.add_line('stem-r',(34,32),(34,34))
        for bloom,stem in [('centre','stem-c'),('left','stem-l'),('right','stem-r')]:
            self.relate('connect',bloom,stem)
        self.add_polyline('pot',(6,34),(14,34),(24,34),(34,34),(42,34),(38,42),(10,42),closed=True)
        for stem in ('stem-c','stem-l','stem-r'):
            self.relate('connect',stem,'pot')
