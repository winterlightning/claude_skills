"""Two Falling Bombs. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'a92b9733-23c6-4903-9f3a-c893edb5e9f4'
SOURCE_PATH = 'pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-falling-bombs-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'two falling bombs')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'bomb-left',6,17,20,31,6)
        self.add_polyline('fins-left',(7,17),(7,6),(13,10),(19,6),(19,17))
        self.relate('connect','bomb-left','fins-left')
        rounded_rect(self,'bomb-right',28,28,42,42,6)
        self.add_polyline('fins-right',(29,28),(29,17),(35,21),(41,17),(41,28))
        self.relate('connect','bomb-right','fins-right')
