"""Independent 32px profile of pair-of-test-tubes-2869b113.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2869b113-eb2a-5dcb-a493-ca714b5657f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/test tubes_2869b113-eb2a-5dcb-a493-ca714b5657f9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2869b113-eb2a-5dcb-a493-ca714b5657f9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/test tubes_2869b113-eb2a-5dcb-a493-ca714b5657f9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pair-of-test-tubes-2869b113',)
SOLO_SOURCE_ICON_IDS = ('pair-of-test-tubes-2869b113',)
REFERENCE_EXPORT_SHA256 = '890a7a11fb3afdc4f75e9e685a8350bcb8bb14b989027f128f6fb903d14392a1'

class Drawing(Sub32):
    icon_id = 'pair-of-test-tubes-2869b113-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (4, 16))
        self.add_line('p1-r1-2', (4, 16), (4, 26))
        self.add_arc('p1-r1-3', (4, 26), (11, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (11, 26), (11, 16))
        self.add_line('p1-r1-5', (11, 16), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 2), (4, 2))
        self.add_line('p2-r1-2', (4, 2), (11, 2))
        self.add_line('p2-r1-3', (11, 2), (13, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (4, 16), (11, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 2), (21, 21))
        self.add_line('p4-r1-2', (21, 21), (21, 26))
        self.add_arc('p4-r1-3', (21, 26), (28, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p4-r1-4', (28, 26), (28, 21))
        self.add_line('p4-r1-5', (28, 21), (28, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (19, 2), (21, 2))
        self.add_line('p5-r1-2', (21, 2), (28, 2))
        self.add_line('p5-r1-3', (28, 2), (30, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (21, 21), (28, 21))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-4', 'p6-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-2')
        self.relate('connect', 'p4-r1-5', 'p5-r1-3')
        self.relate('connect', 'p4-r1-5', 'p6-r1-1')
