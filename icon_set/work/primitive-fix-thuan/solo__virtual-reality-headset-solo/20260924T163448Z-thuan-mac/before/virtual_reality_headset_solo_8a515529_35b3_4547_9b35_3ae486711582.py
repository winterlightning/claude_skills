"""Virtual Reality Headset. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
VR visor with nose cutout and short side straps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '8a515529-35b3-4547-9b35-3ae486711582'
SOURCE_PATH = 'pictographic-primitives/other/device wearable vr goggles_8a515529-35b3-4547-9b35-3ae486711582.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'virtual-reality-headset-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'virtual reality headset')
    def build(self):
        # Plan: VR visor with nose cutout and short side straps.
        self.add_polyline('outline',(4,17),(8,17),(8,12),(14,8),(34,8),(40,12),(40,17),(44,17),(44,31),(40,31),(40,36),(34,40),(28,40),(24,35),(20,40),(14,40),(8,36),(8,31),(4,31),closed=True)
