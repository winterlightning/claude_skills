# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of puzzle-piece.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'daa95c47-3220-4ba6-8dc5-aca5e1866078'
SOURCE_PATH = 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('daa95c47-3220-4ba6-8dc5-aca5e1866078', 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'),)
PROFILE_SOURCE_KEYS = ('solo/puzzle-piece',)
SOLO_SOURCE_ICON_IDS = ('puzzle-piece',)
REFERENCE_EXPORT_SHA256 = '69bb0742c20688dfc2cb2726d56da61a0bfb102e3c45bc787f4a18a4046c689c'

class DrawingVariant2(Sub32):
    icon_id = 'puzzle-piece-sub32-v2'
    variant_of = 'puzzle-piece-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 16), (short_low, 9))
        self.add_line('p1-r1-2', (short_low, 9), (12, 9))
        self.add_bezier('p1-r1-3', (12, 9), ((12, 8), (11, 7), (11, 6)))
        self.add_bezier('p1-r1-4', (11, 6), ((11, 5), (12, 4), (13, 3)))
        self.add_bezier('p1-r1-5', (13, 3), ((14, 2), (15, 2), (16, 2)))
        self.add_bezier('p1-r1-6', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p1-r1-7', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p1-r1-8', (16, 2), ((19, 2), (21, 4), (21, 6)))
        self.add_bezier('p1-r1-9', (21, 6), ((21, 6), (21, 7), (21, 7)))
        self.add_bezier('p1-r1-10', (21, 7), ((21, 8), (21, 8), (21, 9)))
        self.add_line('p1-r1-11', (21, 9), (short_high, 9))
        self.add_line('p1-r1-12', (short_high, 9), (short_high, 16))
        self.add_bezier('p1-r1-13', (short_high, 16), ((short_high, 16), (26, 16), (26, 16)))
        self.add_bezier('p1-r1-14', (26, 16), ((25, 16), (25, 16), (24, 16)))
        self.add_bezier('p1-r1-15', (24, 16), ((22, 16), (22, 18), (22, 20)))
        self.add_bezier('p1-r1-16', (22, 20), ((22, 22), (23, 24), (25, 24)))
        self.add_bezier('p1-r1-17', (25, 24), ((25, 24), (25, 24), (26, 24)))
        self.add_bezier('p1-r1-18', (26, 24), ((26, 24), (short_high, 24), (short_high, 24)))
        self.add_line('p1-r1-19', (short_high, 24), (short_high, 30))
        self.add_line('p1-r1-20', (short_high, 30), (short_low, 30))
        self.add_line('p1-r1-21', (short_low, 30), (short_low, 23))
        self.add_bezier('p1-r1-22', (short_low, 23), ((short_low, 23), (6, 23), (7, 23)))
        self.add_bezier('p1-r1-23', (7, 23), ((7, 23), (7, 23), (7, 23)))
        self.add_bezier('p1-r1-24', (7, 23), ((10, 23), (11, 21), (11, 19)))
        self.add_bezier('p1-r1-25', (11, 19), ((11, 17), (9, 15), (7, 15)))
        self.add_bezier('p1-r1-26', (7, 15), ((7, 15), (7, 15), (7, 15)))
        self.add_bezier('p1-r1-27', (7, 15), ((6, 15), (6, 16), (short_low, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', closed=False)
