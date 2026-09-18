"""Shipping Delivery Truck. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shipping-delivery-truck-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'shipping delivery truck')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('body',(4,32),(4,8),(28,8),(28,32))
        self.add_polyline('cab',(28,16),(36,16),(44,25),(44,32),(42,32))
        self.add_line('axle',(14,32),(32,32))
        circle(self,'rear-wheel',10,34,6)
        circle(self,'front-wheel',38,34,6)
        self.relate('connect','body','cab','axle')
        self.relate('connect','rear-wheel','body','axle')
        self.relate('connect','front-wheel','cab','axle')
