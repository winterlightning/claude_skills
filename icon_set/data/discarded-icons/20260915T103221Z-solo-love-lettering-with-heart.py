"""LOVE occupies a two-by-two square with a heart as the O; letter strokes remain open.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '223c2cf3-707e-5588-bcee-3eb48df2972c'
SOURCE_PATH = 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg'
AUTHOR = 'gpt-6'


class LoveLetteringWithHeart(Solo48):
    icon_id = 'love-lettering-with-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('love', 'lettering', 'heart', 'word', 'romance', 'typography')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        self.add_polyline('letter-l',(6,6),(6,22),(18,22))
        heart('heart-o',34,10,4,17)
        self.add_polyline('letter-v',(6,30),(12,42),(18,30))
        self.add_polyline('letter-e',(42,26),(28,26),(28,34),(28,42),(42,42))
        self.add_line('e-middle',(28,34),(40,34))
        self.relate('connect','letter-e','e-middle')
