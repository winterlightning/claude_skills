"""Geometric Shapes In Rounded Square. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '610733a3-dfd5-42df-9651-d396d039493b'
SOURCE_PATH = 'pictographic-primitives/design/shapes_610733a3-dfd5-42df-9651-d396d039493b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'geometric-shapes-in-rounded-square-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'geometric shapes in rounded square')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        circle(self,'circle',31,17,3)
        self.add_polyline('square',(15,22),(23,22),(23,30),(15,30),closed=True)
        self.add_polyline('triangle',(30,34),(34,27),(38,34),closed=True)
