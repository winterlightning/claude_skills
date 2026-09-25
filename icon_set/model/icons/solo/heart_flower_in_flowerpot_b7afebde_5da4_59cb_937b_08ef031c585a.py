"""A heart flower with one left leaf grows from a tapered flowerpot; double rim and veins omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7afebde-5da4-59cb-937b-08ef031c585a'
SOURCE_PATH = 'pictographic-primitives/romance/love plant pot_b7afebde-5da4-59cb-937b-08ef031c585a.svg'
AUTHOR = 'gpt-6'


class HeartFlowerInFlowerpot(Solo48):
    icon_id = 'heart-flower-in-flowerpot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('heart', 'flower', 'pot', 'plant', 'leaf', 'romance')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        heart('bloom',28,10,6,22)
        self.add_line('stem-top',(28,22),(28,30))
        self.add_line('stem-bottom',(28,30),(28,32))
        self.add_contour('stem','stem-top','stem-bottom')
        self.relate('connect','bloom','stem')
        self.add_arc('leaf-top',(28,30),(8,20),radius_x=20,radius_y=10,sweep=True)
        self.add_arc('leaf-bottom',(8,20),(28,30),radius_x=20,radius_y=10,sweep=True)
        self.add_contour('leaf','leaf-top','leaf-bottom',closed=True)
        self.relate('connect','leaf','stem')
        self.add_polyline('pot',(14,32),(28,32),(38,32),(34,44),(18,44),closed=True)
        self.relate('connect','stem','pot')
