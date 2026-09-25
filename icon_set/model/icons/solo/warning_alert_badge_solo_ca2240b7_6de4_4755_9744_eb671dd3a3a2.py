"""Warning Alert Badge. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ca2240b7-6de4-4755-9744-eb671dd3a3a2'
SOURCE_PATH = 'pictographic-primitives/state/badge exclamation mark_ca2240b7-6de4-4755-9744-eb671dd3a3a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'warning-alert-badge-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('sub icon', 'warning alert badge')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('outline',(24,6),(31,12),(36,12),(36,18),(42,24),(36,30),(36,36),(30,36),(24,42),(18,36),(12,36),(12,30),(6,24),(12,18),(12,12),(18,12),closed=True)
        self.add_line('stem',(24,18),(24,22))
        self.add_dot('dot',(24,30))
