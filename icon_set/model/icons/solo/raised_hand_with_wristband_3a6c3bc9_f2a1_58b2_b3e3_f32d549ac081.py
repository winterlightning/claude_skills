"""A raised open hand wears a rectangular wristband; thumb crease and forearm extensions omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class RaisedHandWithWristband(Solo48):
    icon_id = 'raised-hand-with-wristband'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('hand', 'wristband', 'palm', 'bracelet', 'gesture', 'raised')

    def build(self) -> None:
        self.add_line('index-side',(12,26),(12,16))
        self.add_arc('index-tip',(12,16),(20,16),radius_x=4)
        self.add_line('middle-rise',(20,16),(20,12))
        self.add_arc('middle-tip',(20,12),(28,12),radius_x=4)
        self.add_line('middle-fall',(28,12),(28,14))
        self.add_arc('ring-tip',(28,14),(36,14),radius_x=4)
        self.add_line('ring-fall',(36,14),(36,18))
        self.add_arc('little-tip',(36,18),(44,18),radius_x=4)
        self.add_line('palm-r',(44,18),(40,32))
        self.add_line('thumb-side',(16,32),(4,24))
        self.add_arc('thumb-tip',(4,24),(12,24),radius_x=4)
        self.add_line('thumb-inner',(12,24),(12,26))
        self.add_contour('hand','thumb-side','thumb-tip','thumb-inner','index-side','index-tip','middle-rise','middle-tip','middle-fall','ring-tip','ring-fall','little-tip','palm-r')
        for x,y in [(20,16),(28,14),(36,18)]:
            n=f'finger-crease-{x}'
            self.add_line(n,(x,y),(x,24))
            self.relate('connect','hand',n)
        self.add_polyline('wristband',(16,32),(40,32),(40,40),(16,40),closed=True)
        self.relate('connect','hand','wristband')
