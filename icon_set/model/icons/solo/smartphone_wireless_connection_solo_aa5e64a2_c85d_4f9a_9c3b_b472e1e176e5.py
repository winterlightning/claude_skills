"""Smartphone Wireless Connection. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Two smooth concentric signal arcs above a compact device; omit nonessential indicator dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'aa5e64a2-c85d-4f9a-9c3b-b472e1e176e5'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone wifi_aa5e64a2-c85d-4f9a-9c3b-b472e1e176e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartphone-wireless-connection-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'smartphone wireless connection')
    def build(self):
        self.add_bezier('signal-outer',(8,12),((13,7),(18,4),(24,4)),((30,4),(35,7),(40,12)))
        self.add_bezier('signal-inner',(16,19),((20,15),(28,15),(32,19)))
        rounded_rect(self,'device',18,28,30,44,3)
