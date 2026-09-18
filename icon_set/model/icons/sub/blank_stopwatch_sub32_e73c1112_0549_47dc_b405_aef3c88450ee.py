"""Independent 32px profile of blank-stopwatch.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (15, 9), (22, 11), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 11), (26, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-3', (26, 20), ((26, 22), (25, 25), (23, 27)))
        self.add_bezier('p1-r1-4', (23, 27), ((21, 29), (18, 30), (15, 30)))
        self.add_arc('p1-r1-5', (15, 30), (5, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (5, 20), (15, 9), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (15, 2), (15, 9))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 2), (15, 2))
        self.add_line('p3-r1-2', (15, 2), (20, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (22, 11), (27, 6))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
