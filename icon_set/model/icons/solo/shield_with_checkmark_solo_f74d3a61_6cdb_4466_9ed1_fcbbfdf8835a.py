"""Shield with Checkmark. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'f74d3a61-6cdb-4466-9ed1-fcbbfdf8835a'
SOURCE_PATH = 'pictographic-primitives/protection/protection shield_f74d3a61-6cdb-4466-9ed1-fcbbfdf8835a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shield-with-checkmark-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'state')
    tags = ('sub icon',)
    keywords = ('sub icon', 'shield with checkmark')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('shield',(24,4),((19,7),(14,9),(8,10)),((8,26),(8,35),(24,44)),((40,35),(40,26),(40,10)),((34,9),(29,7),(24,4)))
        self.add_contour('outline','shield',closed=True)
        self.add_polyline('check',(17,23),(23,29),(31,19))
