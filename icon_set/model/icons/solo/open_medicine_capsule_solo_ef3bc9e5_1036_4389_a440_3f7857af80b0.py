"""Open Medicine Capsule. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ef3bc9e5-1036-4389-a440-3f7857af80b0'
SOURCE_PATH = 'pictographic-primitives/other/pill open_ef3bc9e5-1036-4389-a440-3f7857af80b0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-medicine-capsule-solo'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'open medicine capsule')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('left',(15,10),(15,38),radius_x=11,radius_y=14,sweep=False)
        self.add_line('left-opening-1',(15, 38),(19, 34))
        self.add_line('left-opening-2',(19, 34),(19, 14))
        self.add_line('left-opening-3',(19, 14),(15, 10))
        self.add_contour('left-half','left','left-opening-1','left-opening-2','left-opening-3')
        self.add_arc('right',(33,38),(33,10),radius_x=11,radius_y=14,sweep=False)
        self.add_line('right-opening-1',(33, 10),(29, 14))
        self.add_line('right-opening-2',(29, 14),(29, 34))
        self.add_line('right-opening-3',(29, 34),(33, 38))
        self.add_contour('right-half','right','right-opening-1','right-opening-2','right-opening-3')
