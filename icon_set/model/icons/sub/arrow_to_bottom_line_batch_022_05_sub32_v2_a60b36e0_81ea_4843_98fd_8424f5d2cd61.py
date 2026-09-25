# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of arrow-to-bottom-line-batch-022-05.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a60b36e0-81ea-4843-98fd-8424f5d2cd61'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/move bottom_a60b36e0-81ea-4843-98fd-8424f5d2cd61.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a60b36e0-81ea-4843-98fd-8424f5d2cd61', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/move bottom_a60b36e0-81ea-4843-98fd-8424f5d2cd61.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-to-bottom-line-batch-022-05',)
SOLO_SOURCE_ICON_IDS = ('arrow-to-bottom-line-batch-022-05',)
REFERENCE_EXPORT_SHA256 = 'd6ca4e102681abc06729bd82f0989c19bb9706ddc8ee56ddbf3ff9d005c23050'

class DrawingVariant2(Sub32):
    icon_id = 'arrow-to-bottom-line-batch-022-05-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (16, 24))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (8, 16), (16, 24))
        self.add_line('p2-r1-2', (16, 24), (24, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (short_low, 30), (short_high, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
