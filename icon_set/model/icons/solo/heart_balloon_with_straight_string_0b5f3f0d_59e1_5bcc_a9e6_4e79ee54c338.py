"""A heart balloon has a straight string and open knot; the tiny enclosed knot is simplified.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class HeartBalloonWithStraightString(Solo48):
    icon_id = 'heart-balloon-with-straight-string'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'balloon', 'string', 'party', 'romance', 'celebration')

    def build(self) -> None:
        self.add_arc('lobe-l',(24,12),(8,12),radius_x=8,sweep=False)
        self.add_arc('shoulder-l',(8,12),(12,20),radius_x=10,sweep=False)
        self.add_line('side-l',(12,20),(24,30))
        self.add_line('side-r',(24,30),(36,20))
        self.add_arc('shoulder-r',(36,20),(40,12),radius_x=10,sweep=False)
        self.add_arc('lobe-r',(40,12),(24,12),radius_x=8,sweep=False)
        self.add_contour('balloon','lobe-l','shoulder-l','side-l','side-r','shoulder-r','lobe-r',closed=True)
        self.add_polyline('knot',(20,34),(24,30),(28,34))
        self.add_line('string',(24,30),(24,44))
        self.relate('connect','balloon','knot')
        self.relate('connect','balloon','string')
        self.relate('connect','knot','string')
