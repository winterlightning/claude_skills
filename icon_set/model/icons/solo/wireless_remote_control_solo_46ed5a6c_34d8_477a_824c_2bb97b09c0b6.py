"""Wireless Remote Control. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '46ed5a6c-34d8-477a-824c-2bb97b09c0b6'
SOURCE_PATH = 'pictographic-primitives/other/remote control_46ed5a6c-34d8-477a-824c-2bb97b09c0b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wireless-remote-control-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'wireless remote control')
    def build(self):
        self.add_bezier('signal-outer',(8,12),((13,7),(18,4),(24,4)),((30,4),(35,7),(40,12)))
        self.add_bezier('signal-inner',(16,19),((20,15),(28,15),(32,19)))
        rounded_rect(self,'device',18,28,30,44,3)
