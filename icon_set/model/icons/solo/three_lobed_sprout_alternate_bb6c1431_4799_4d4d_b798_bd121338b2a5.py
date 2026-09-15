"""An upright pointed leaf rises between two broad side leaves above a short stem. VRECT centerline extremes (8,4)-(40,44); mirrored lobes share one central axis.
Reduction: Kept the three-lobed outline and omitted no identifying feature.
Lucide: leaf, sprout
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb6c1431-4799-4d4d-b798-bd121338b2a5'
SOURCE_PATH = 'pictographic-primitives/nature/wheat_bb6c1431-4799-4d4d-b798-bd121338b2a5.svg'
AUTHOR = 'gpt-6'

class ThreeLobedSproutAlternate(Solo48):
    icon_id = 'three-lobed-sprout-alternate'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-04"
    aliases = ()
    keywords = ('sprout', 'leaf', 'plant', 'wheat', 'growth', 'seedling', 'nature', 'agriculture')

    def build(self) -> None:
        a=24;left=a-16;right=a+16
        self.add_arc('side-left-inner',(left,18),(a-6,24),radius_x=16,radius_y=10)
        self.add_arc('center-left',(a-6,24),(a,4),radius_x=30)
        self.add_arc('center-right',(a,4),(a+6,24),radius_x=30)
        self.add_arc('side-right-inner',(a+6,24),(right,18),radius_x=16,radius_y=10)
        self.add_arc('bowl-right',(right,18),(a,36),radius_x=16,radius_y=18)
        self.add_arc('bowl-left',(a,36),(left,18),radius_x=16,radius_y=18)
        self.add_contour('sprout','side-left-inner','center-left','center-right','side-right-inner','bowl-right','bowl-left',closed=True)
        self.add_line('stem',(a,36),(a,44))
        for part in ('bowl-right','bowl-left'):self.relate('connect','stem',part)
