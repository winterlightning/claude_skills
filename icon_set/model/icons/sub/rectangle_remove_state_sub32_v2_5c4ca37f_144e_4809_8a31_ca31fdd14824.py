# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of rectangle-remove-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5c4ca37f-144e-4809-8a31-ca31fdd14824', 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rectangle-remove-state',)
SOLO_SOURCE_ICON_IDS = ('rectangle-remove-state',)
REFERENCE_EXPORT_SHA256 = '03be80878aacbac0addaceb08ddf4b9f23023dd16de4aa2ddceb5bf462c5feb4'

class DrawingVariant2(Sub32):
    icon_id = 'rectangle-remove-state-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (5, short_low), (27, short_low))
        self.add_arc('p1-r1-2', (27, short_low), (30, 8), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 8), (30, 24))
        self.add_arc('p1-r1-4', (30, 24), (27, short_high), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, short_high), (5, short_high))
        self.add_arc('p1-r1-6', (5, short_high), (2, 24), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 24), (2, 8))
        self.add_arc('p1-r1-8', (2, 8), (5, short_low), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (10, 16), (22, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
