# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of puzzle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c5ecd9ca-686b-498b-91a5-e7aeba10a365'
SOURCE_PATH = 'pictographic-primitives/state/puzzle_c5ecd9ca-686b-498b-91a5-e7aeba10a365.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c5ecd9ca-686b-498b-91a5-e7aeba10a365', 'pictographic-primitives/state/puzzle_c5ecd9ca-686b-498b-91a5-e7aeba10a365.svg'),)
PROFILE_SOURCE_KEYS = ('solo/puzzle',)
SOLO_SOURCE_ICON_IDS = ('puzzle',)
REFERENCE_EXPORT_SHA256 = '455e4ef9abe816a8178c3463c8a4f211ef7995646515631b8e59dc6da00acd80'

class DrawingVariant2(Sub32):
    icon_id = 'puzzle-sub32-v2'
    variant_of = 'puzzle-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (12, 10), (short_low, 10))
        self.add_line('p1-r1-2', (short_low, 10), (short_low, 16))
        self.add_bezier('p1-r1-3', (short_low, 16), ((8, 16), (9, 17), (9, 20)))
        self.add_bezier('p1-r1-4', (9, 20), ((9, 22), (8, 23), (short_low, 23)))
        self.add_line('p1-r1-5', (short_low, 23), (short_low, 30))
        self.add_line('p1-r1-6', (short_low, 30), (14, 30))
        self.add_bezier('p1-r1-7', (14, 30), ((14, 29), (13, 29), (13, 28)))
        self.add_bezier('p1-r1-8', (13, 28), ((13, 26), (15, 24), (17, 24)))
        self.add_bezier('p1-r1-9', (17, 24), ((20, 24), (21, 26), (21, 28)))
        self.add_bezier('p1-r1-10', (21, 28), ((21, 29), (21, 29), (21, 30)))
        self.add_line('p1-r1-11', (21, 30), (short_high, 30))
        self.add_line('p1-r1-12', (short_high, 30), (short_high, 10))
        self.add_line('p1-r1-13', (short_high, 10), (20, 10))
        self.add_bezier('p1-r1-14', (20, 10), ((21, 9), (21, 7), (21, 6)))
        self.add_bezier('p1-r1-15', (21, 6), ((21, 4), (19, 2), (16, 2)))
        self.add_bezier('p1-r1-16', (16, 2), ((13, 2), (11, 4), (11, 6)))
        self.add_bezier('p1-r1-17', (11, 6), ((11, 7), (11, 9), (12, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
