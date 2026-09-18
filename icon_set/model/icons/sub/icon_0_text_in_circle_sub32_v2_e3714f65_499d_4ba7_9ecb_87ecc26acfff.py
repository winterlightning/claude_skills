# Variant of icon-0-text-in-circle-sub32; parent file remains unchanged.
"""Independent 32px profile of icon-0-text-in-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3714f65-499d-4ba7-9ecb-87ecc26acfff', 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/icon-0-text-in-circle',)
SOLO_SOURCE_ICON_IDS = ('icon-0-text-in-circle',)
REFERENCE_EXPORT_SHA256 = '9a2a96442fa40bccaacddc40c716e980385c1b298dc4244b115d220e57fde623'

class DrawingVariant2(Sub32):
    icon_id = 'icon-0-text-in-circle-sub32-v2'
    variant_of = 'icon-0-text-in-circle-sub32'
    variant_label = 'Restore smooth typeface zero shoulders'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        # Preferred digit-0 from typeface/glyphs.json, scaled to 16 high and grid fitted.
        self.add_arc('zero-top', (10,13), (22,13), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_line('zero-right', (22,13), (22,19))
        self.add_arc('zero-bottom', (22,19), (10,19), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_line('zero-left', (10,19), (10,13))
        self.add_contour('path-2-1', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
