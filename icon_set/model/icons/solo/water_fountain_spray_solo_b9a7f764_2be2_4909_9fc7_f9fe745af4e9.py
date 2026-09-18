"""Water Fountain Spray. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'b9a7f764-2be2-4909-9fc7-f9fe745af4e9'
SOURCE_PATH = 'pictographic-primitives/other/fountain_b9a7f764-2be2-4909-9fc7-f9fe745af4e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'water-fountain-spray-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'water fountain spray')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('left',(4,20),((10,4),(17,4),(24,20)))
        self.add_bezier('right',(24,20),((31,4),(38,4),(44,20)))
        self.add_line('stem',(24,20),(24,40))
        self.relate('connect','left','right','stem')
