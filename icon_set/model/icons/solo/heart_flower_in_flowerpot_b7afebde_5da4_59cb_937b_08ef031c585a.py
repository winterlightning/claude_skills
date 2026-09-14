"""A heart flower with one left leaf grows from a tapered flowerpot; double rim and veins omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class HeartFlowerInFlowerpot(Solo48):
    icon_id = 'heart-flower-in-flowerpot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
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
