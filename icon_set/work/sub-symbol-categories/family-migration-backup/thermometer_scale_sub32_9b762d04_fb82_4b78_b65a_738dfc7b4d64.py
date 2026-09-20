"""Independent 32px profile of thermometer-scale.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9b762d04-fb82-4b78-b65a-738dfc7b4d64'
SOURCE_PATH = 'pictographic-primitives/symbol/thermometer_9b762d04-fb82-4b78-b65a-738dfc7b4d64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9b762d04-fb82-4b78-b65a-738dfc7b4d64', 'pictographic-primitives/symbol/thermometer_9b762d04-fb82-4b78-b65a-738dfc7b4d64.svg'),)
PROFILE_SOURCE_KEYS = ('solo/thermometer-scale',)
SOLO_SOURCE_ICON_IDS = ('thermometer-scale',)
REFERENCE_EXPORT_SHA256 = 'e0270d75f72e447b53e1e6d8f6a7d2ff928cc80edf0a81fa056ca97cd866c6ce'

class Drawing(Sub32):
    icon_id = 'thermometer-scale-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (4, 9), (18, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (18, 9), (18, 16))
        self.add_arc('p1-r1-3', (18, 16), (21, 21), radius_x=2, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-4', (21, 21), ((21, 26), (16, 30), (11, 30)))
        self.add_bezier('p1-r1-5', (11, 30), ((6, 30), (2, 26), (2, 21)))
        self.add_arc('p1-r1-6', (2, 21), (4, 16), radius_x=2, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (4, 16), (4, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (11, 11), (11, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 23), (11, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (28, 5), (30, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (28, 13), (30, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
