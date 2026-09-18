"""Circled Curved Share Arrow. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '54c4c96e-2201-4fc6-9905-c97205f79810'
SOURCE_PATH = 'pictographic-primitives/other/circle arrow next_54c4c96e-2201-4fc6-9905-c97205f79810.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circled-curved-share-arrow-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circled curved share arrow')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_bezier('turn',(16,32),((16,22),(24,20),(33,20)))
        self.add_polyline('head',(27,14),(33,20),(27,26))
        self.relate('connect','turn','head')
