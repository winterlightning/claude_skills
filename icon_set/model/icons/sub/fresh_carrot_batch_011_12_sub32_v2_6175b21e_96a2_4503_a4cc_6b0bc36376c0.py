"""Independent 32px profile of fresh-carrot-batch-011-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6175b21e-96a2-4503-a4cc-6b0bc36376c0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fresh-carrot-batch-011-12',)
SOLO_SOURCE_ICON_IDS = ('fresh-carrot-batch-011-12',)
REFERENCE_EXPORT_SHA256 = '2c67db710f6202338a4b821064cf730bdb737e4968f7733871534d4273898c79'

class DrawingVariant2(Sub32):
    icon_id = 'fresh-carrot-batch-011-12-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'food'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (16, 10), ((11, 10), (9, 13), (9, 16)))
        self.add_bezier('p1-r1-2', (9, 16), ((9, 20), (12, 25), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((20, 25), (23, 20), (23, 16)))
        self.add_bezier('p1-r1-6', (23, 16), ((23, 13), (21, 10), (16, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (short_low, 2), (16, 10))
        self.add_line('p2-r1-2', (16, 10), (short_high, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-2')
