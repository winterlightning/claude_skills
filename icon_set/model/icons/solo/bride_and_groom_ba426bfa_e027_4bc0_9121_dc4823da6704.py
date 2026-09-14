"""A groom and veiled bride stand side by side; face and finger details omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class BrideAndGroom(Solo48):
    icon_id = 'bride-and-groom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('bride', 'groom', 'couple', 'wedding', 'veil', 'marriage')

    def build(self) -> None:
        self.add_arc('groom-head-r',(12,6),(12,14),radius_x=4)
        self.add_arc('groom-head-l',(12,14),(12,6),radius_x=4)
        self.add_contour('groom-head','groom-head-r','groom-head-l',closed=True)
        self.add_polyline('shirt',(6,32),(6,25),(12,23),(18,25),(18,32),(16,32),(8,32),closed=True)
        self.add_line('leg-l',(8,32),(8,42))
        self.add_line('leg-r',(16,32),(16,42))
        self.relate('connect','shirt','leg-l')
        self.relate('connect','shirt','leg-r')
        self.add_arc('bride-hair',(26,14),(42,14),radius_x=8)
        self.add_arc('bride-face',(42,14),(26,14),radius_x=8)
        self.add_contour('bride-head','bride-hair','bride-face',closed=True)
        self.add_polyline('veil-l',(26,14),(26,26),(30,26))
        self.add_polyline('veil-r',(42,14),(42,26),(38,26))
        self.add_polyline('dress',(30,26),(34,30),(38,26),(42,42),(26,42),closed=True)
        self.relate('connect','bride-head','veil-l')
        self.relate('connect','bride-head','veil-r')
        self.relate('connect','veil-l','dress')
        self.relate('connect','veil-r','dress')
