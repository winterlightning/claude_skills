"""Independent 32px profile of mailbox-arched.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fda9a667-bd1e-4cf3-8b31-404409a91c95'
SOURCE_PATH = 'pictographic-primitives/symbol/mailbox_fda9a667-bd1e-4cf3-8b31-404409a91c95.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fda9a667-bd1e-4cf3-8b31-404409a91c95', 'pictographic-primitives/symbol/mailbox_fda9a667-bd1e-4cf3-8b31-404409a91c95.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mailbox-arched',)
SOLO_SOURCE_ICON_IDS = ('mailbox-arched',)
REFERENCE_EXPORT_SHA256 = 'bffae678963f3f985dab79b005fb95c69fae657d6fc5d9a34ca86a22eceb52e5'

class DrawingVariant2(Sub32):
    icon_id = 'mailbox-arched-sub32-v2'
    related_origin_icon_id = 'mailbox-arched-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 30), (short_low, 24))
        self.add_line('p1-r1-2', (short_low, 24), (short_low, 13))
        self.add_arc('p1-r1-3', (short_low, 13), (short_high, 13), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (short_high, 13), (short_high, 24))
        self.add_line('p1-r1-5', (short_high, 24), (short_high, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (short_low, 24), (short_high, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 15), (20, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
