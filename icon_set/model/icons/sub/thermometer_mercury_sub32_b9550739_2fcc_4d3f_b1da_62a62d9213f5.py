"""Independent 32px profile of thermometer-mercury.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b9550739-2fcc-4d3f-b1da-62a62d9213f5'
SOURCE_PATH = 'pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b9550739-2fcc-4d3f-b1da-62a62d9213f5', 'pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/thermometer-mercury',)
SOLO_SOURCE_ICON_IDS = ('thermometer-mercury',)
REFERENCE_EXPORT_SHA256 = '9433a09109e9f1cdfb74828e8676ad88c428493c5035e679adb41688fd4eefa9'

class Drawing(Sub32):
    icon_id = 'thermometer-mercury-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (22, 8), (22, 15))
        self.add_arc('p1-r1-3', (22, 15), (27, 19), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (27, 19), (5, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (5, 19), (10, 15), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (10, 15), (10, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 10), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 23), (16, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
