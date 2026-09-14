"""A cake carries a two-person topper above scalloped icing; tiny faces and limbs omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class WeddingCakeWithCoupleTopper(Solo48):
    icon_id = 'wedding-cake-with-couple-topper'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('cake', 'wedding', 'couple', 'topper', 'icing', 'celebration')

    def build(self) -> None:
        for n,x in [('groom',16),('bride',32)]:
            self.add_arc(n+'-head-r',(x,8),(x,16),radius_x=4)
            self.add_arc(n+'-head-l',(x,16),(x,8),radius_x=4)
            self.add_contour(n+'-head',n+'-head-r',n+'-head-l',closed=True)
        self.add_polyline('groom-body',(12,24),(12,16),(16,16),(20,16),(20,24))
        self.add_polyline('bride-body',(26,24),(28,16),(32,16),(36,16),(38,24))
        self.add_polyline('cake',(4,32),(4,24),(12,24),(20,24),(26,24),(38,24),(44,24),(44,32),(44,40),(4,40),closed=True)
        self.relate('connect','groom-body','cake')
        self.relate('connect','bride-body','cake')
        self.relate('connect','groom-head','groom-body')
        self.relate('connect','bride-head','bride-body')
        for i,x in enumerate((4,14,24,34)):
            self.add_arc(f'icing-{i}',(x,32),(x+10,32),radius_x=5,radius_y=3,sweep=False)
        self.add_contour('icing',*(f'icing-{i}' for i in range(4)))
        self.relate('connect','icing','cake')
