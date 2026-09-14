"""A right-facing wedding car tows a heart balloon; side decal, cans and ribbon details omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class WeddingCarWithHeartBalloon(Solo48):
    icon_id = 'wedding-car-with-heart-balloon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('car', 'wedding', 'balloon', 'heart', 'vehicle', 'celebration')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        heart('balloon',14,10,4,20)
        self.add_arc('tether',(14,20),(10,28),radius_x=10,sweep=False)
        self.relate('connect','balloon','tether')
        self.add_polyline('body',(10,28),(16,28),(20,22),(30,22),(34,28),(38,28),(42,32),(42,38),(40,38))
        self.relate('connect','body','tether')
        self.add_line('bumper-left',(8,38),(6,38))
        self.add_line('rear',(6,38),(6,32))
        self.add_arc('rear-corner',(6,32),(10,28),radius_x=4)
        self.add_contour('rear-body','bumper-left','rear','rear-corner')
        self.relate('connect','rear-body','body')
        for n,x in [('rear-wheel',12),('front-wheel',36)]:
            self.add_arc(n+'-a',(x-4,38),(x+4,38),radius_x=4)
            self.add_arc(n+'-b',(x+4,38),(x-4,38),radius_x=4)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.add_line('sill',(16,38),(32,38))
        self.relate('connect','rear-wheel','rear-body')
        self.relate('connect','rear-wheel','sill')
        self.relate('connect','front-wheel','sill')
        self.relate('connect','front-wheel','body')
