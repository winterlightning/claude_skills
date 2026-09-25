"""Add Location Map Pin. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '4fe0a6bc-2115-4dc8-acaf-745d96ceef9a'
SOURCE_PATH = 'pictographic-primitives/other/drop cross_4fe0a6bc-2115-4dc8-acaf-745d96ceef9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'add-location-map-pin-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'add location map pin')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('pin-top',(8,20),(40,20),radius_x=16)
        self.add_bezier('pin-bottom',(40,20),((40,29),(29,40),(24,44)),((19,40),(8,29),(8,20)))
        self.add_contour('outline','pin-top','pin-bottom',closed=True)
        self.add_polyline('h',(17,20),(24,20),(31,20))
        self.add_polyline('v',(24,13),(24,20),(24,27))
        self.relate('connect','h','v')
