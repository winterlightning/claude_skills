"""Security Protection Shield. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '948619df-4023-4222-a169-4dace0131ae9'
SOURCE_PATH = 'pictographic-primitives/other/shield 1_948619df-4023-4222-a169-4dace0131ae9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'security-protection-shield-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'security protection shield')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('shield',(24,4),((19,7),(14,9),(8,10)),((8,26),(8,35),(24,44)),((40,35),(40,26),(40,10)),((34,9),(29,7),(24,4)))
        self.add_contour('outline','shield',closed=True)
        self.add_line('divider',(24,4),(24,44))
        self.relate('connect','outline','divider')
