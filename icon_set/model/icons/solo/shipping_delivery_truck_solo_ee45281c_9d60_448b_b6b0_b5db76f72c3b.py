"""Shipping Delivery Truck. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

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
        # Cargo box and cab share one silhouette; small full circular wheels.
        self.add_polyline('shell',(4,26),(4,8),(27,8),(27,16),(36,16),(44,26),(4,26))
        self.add_line('cab-divider',(27,16),(27,26))
        self.relate('connect','shell','cab-divider')
        for name,x in [('rear',12),('front',36)]:
            circle(self,name+'-wheel',x,37,3)
