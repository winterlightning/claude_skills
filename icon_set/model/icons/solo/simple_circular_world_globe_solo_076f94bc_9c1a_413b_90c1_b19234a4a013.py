"""Simple Circular World Globe. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.
Latitude simplified to equator to preserve clear spacing at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '076f94bc-9c1a-413b-90c1-b19234a4a013'
SOURCE_PATH = 'pictographic-primitives/other/globe_076f94bc-9c1a-413b-90c1-b19234a4a013.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-circular-world-globe-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'simple circular world globe')
    def build(self):
        # One equator replaces crowded paired latitudes; meridian preserved.
        circle(self,'outline',24,24,20)
        self.add_polyline('equator',(4,24),(24,24),(44,24))
        self.add_polyline('meridian',(24,4),(24,24),(24,44))
        self.relate('connect','outline','equator','meridian')
