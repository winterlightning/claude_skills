"""Three cake tiers with rounded upper corners step outward; one scalloped icing band replaces fine bands.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = ('80c91df2-deb2-4ace-944d-db4ce890e12f', '223c2cf3-707e-5588-bcee-3eb48df2972c', 'b95b4f32-ce00-535a-800c-4f12020dc625', '38fd3f15-701d-4404-8da0-af7c79ef4dd2', '32295af4-defa-5f3c-af21-d930830f3a88', 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f', '3042423e-028e-4d0e-bed7-3e328b97f33b', 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c', '045520ca-f23a-531a-b54e-ce7bc4cbf52e')
SOURCE_PATH = ('pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg', 'pictographic-primitives/romance/lgbt love_223c2cf3-707e-5588-bcee-3eb48df2972c.svg', 'pictographic-primitives/romance/love bud_b95b4f32-ce00-535a-800c-4f12020dc625.svg', 'pictographic-primitives/romance/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg', 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg', 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg', 'pictographic-primitives/romance/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg', 'pictographic-primitives/romance/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg', 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg')
AUTHOR = 'gpt-6'


class ThreeTierWeddingCake(Solo48):
    icon_id = 'three-tier-wedding-cake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('cake', 'wedding', 'tier', 'icing', 'dessert', 'celebration')

    def build(self) -> None:
        def tier(n,left,right,top,bottom):
            r=2
            self.add_line(n+'-l',(left,bottom),(left,top+r))
            self.add_arc(n+'-tl',(left,top+r),(left+r,top),radius_x=r)
            self.add_line(n+'-t',(left+r,top),(right-r,top))
            self.add_arc(n+'-tr',(right-r,top),(right,top+r),radius_x=r)
            self.add_line(n+'-r',(right,top+r),(right,bottom))
            self.add_line(n+'-b',(right,bottom),(left,bottom))
            self.add_contour(n,n+'-l',n+'-tl',n+'-t',n+'-tr',n+'-r',n+'-b',closed=True)
        tier('top-tier',16,32,6,16)
        tier('middle-tier',10,38,16,28)
        tier('bottom-tier',6,42,28,42)
        self.relate('connect','top-tier','middle-tier')
        self.relate('connect','middle-tier','bottom-tier')
        for i,x in enumerate((6,18,30)):
            self.add_arc(f'icing-{i}',(x,34),(x+12,34),radius_x=6,radius_y=3,sweep=False)
        self.add_contour('icing',*(f'icing-{i}' for i in range(3)))
        self.relate('connect','icing','bottom-tier')
