"""Search Magnifying Glass. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Circular lens with handle at a shared point; intentional diagonal handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '9f1aeae0-d56e-4c60-8db2-c377d1b6ef06'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass_9f1aeae0-d56e-4c60-8db2-c377d1b6ef06.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'search-magnifying-glass-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'search magnifying glass')
    def build(self):
        # Plan: Circular lens with handle at a shared point; intentional diagonal handle.
        self.add_arc('ring-a',(6,21),(21,6),radius_x=15)
        self.add_arc('ring-b',(21,6),(36,21),radius_x=15)
        self.add_arc('ring-c',(36,21),(30,33),radius_x=15)
        self.add_arc('ring-d',(30,33),(6,21),radius_x=15)
        self.add_contour('lens','ring-a','ring-b','ring-c','ring-d',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','lens','handle')
