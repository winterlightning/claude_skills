"""Circular Downward Pointing Arrow. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '9703959b-8d72-4272-aa87-6963634386ca'
SOURCE_PATH = 'pictographic-primitives/other/circle arrow down_9703959b-8d72-4272-aa87-6963634386ca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-downward-pointing-arrow-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular downward pointing arrow')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('shaft',(24,14),(24,32))
        self.add_polyline('head',(17,25),(24,32),(31,25))
        self.relate('connect','shaft','head')
