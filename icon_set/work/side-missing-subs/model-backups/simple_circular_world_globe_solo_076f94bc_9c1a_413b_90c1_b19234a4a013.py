"""Simple Circular World Globe. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
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
        circle(self,'outline',24,24,20)
        self.add_line('latitude-top',(8,12),(40,12))
        self.add_line('latitude-bottom',(8,36),(40,36))
        self.add_line('meridian',(24,4),(24,44))
        self.relate('connect','outline','latitude-top','latitude-bottom','meridian')
