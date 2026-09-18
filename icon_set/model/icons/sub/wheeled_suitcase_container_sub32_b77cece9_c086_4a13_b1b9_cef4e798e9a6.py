"""Independent 32px profile of wheeled-suitcase-container.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b77cece9-c086-4a13-b1b9-cef4e798e9a6'
SOURCE_PATH = 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b77cece9-c086-4a13-b1b9-cef4e798e9a6', 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'),)
PROFILE_SOURCE_KEYS = ('container/wheeled-suitcase-container',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '6e45995adf1f85635ba3fa0c3d979a7e6e8888f1b76951102cf44cf2de0f8d2b'

class Drawing(Sub32):
    icon_id = 'wheeled-suitcase-container-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'containers'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (27, 8))
        self.add_arc('p1-r1-2', (27, 8), (30, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 10), (30, 23))
        self.add_arc('p1-r1-4', (30, 23), (27, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 26), (5, 26))
        self.add_arc('p1-r1-6', (5, 26), (2, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 23), (2, 10))
        self.add_arc('p1-r1-8', (2, 10), (5, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (11, 8), (11, 4))
        self.add_arc('p2-r1-2', (11, 4), (13, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 2), (19, 2))
        self.add_arc('p2-r1-4', (19, 2), (21, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (21, 4), (21, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (9, 26), (9, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 26), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
