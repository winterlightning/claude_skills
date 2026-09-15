"""Two mirrored cupped hands surround a heart; individual finger seams and wrist cuffs are omitted.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c'
SOURCE_PATH = 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg'
AUTHOR = 'gpt-6'


class HandsCradlingHeart(Solo48):
    icon_id = 'hands-cradling-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('hands', 'heart', 'holding', 'care', 'love', 'romance')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        heart('heart',24,10,4,22)
        for side in (-1,1):
            n='left' if side<0 else 'right'
            def p(x,y): return (24+side*x,y)
            self.add_line(n+'-wrist',p(13,42),p(13,38))
            self.add_line(n+'-heel',p(13,38),p(18,30))
            self.add_line(n+'-outer',p(18,30),p(18,26))
            self.add_arc(n+'-tip',p(18,26),p(10,26),radius_x=4,sweep=side<0)
            self.add_line(n+'-finger',p(10,26),p(10,30))
            self.add_line(n+'-palm',p(10,30),p(5,36))
            self.add_line(n+'-inner',p(5,36),p(5,42))
            self.add_contour(n,n+'-wrist',n+'-heel',n+'-outer',n+'-tip',n+'-finger',n+'-palm',n+'-inner')
