"""Independent 32px profile of blank-stopwatch.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e73c1112-0549-47dc-b405-aef3c88450ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/stopwatch_e73c1112-0549-47dc-b405-aef3c88450ee.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e73c1112-0549-47dc-b405-aef3c88450ee', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/stopwatch_e73c1112-0549-47dc-b405-aef3c88450ee.svg'),)
PROFILE_SOURCE_KEYS = ('solo/blank-stopwatch',)
SOLO_SOURCE_ICON_IDS = ('blank-stopwatch',)
REFERENCE_EXPORT_SHA256 = '54ce845360a5858558570172f842c8bff86eb363c3a644ce4542b17f27a8930c'

class Drawing(Sub32):
    icon_id = 'blank-stopwatch-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Round body, crown stem and bar on top, two side buttons at 45 degrees.
        self.add_arc('p1-r1-1', (16, 10), (23, 13), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (23, 13), (16, 30), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 30), (9, 13), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (9, 13), (16, 10), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_line('p2-r1-1', (16, 2), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 2), (16, 2))
        self.add_line('p3-r1-2', (16, 2), (20, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (23, 13), (28, 8))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 13), (4, 8))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
