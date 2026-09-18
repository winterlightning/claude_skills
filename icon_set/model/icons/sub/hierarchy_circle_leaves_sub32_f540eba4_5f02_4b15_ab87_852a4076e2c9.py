"""Independent 32px profile of hierarchy-circle-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f540eba4-5f02-4b15-ab87-852a4076e2c9'
SOURCE_PATH = 'pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f540eba4-5f02-4b15-ab87-852a4076e2c9', 'pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hierarchy-circle-leaves',)
SOLO_SOURCE_ICON_IDS = ('hierarchy-circle-leaves',)
REFERENCE_EXPORT_SHA256 = '422d84c25ff1bd4c6142b6667dbf3634fef2ece6d3334d62e375e856b66df33a'

class Drawing(Sub32):
    icon_id = 'hierarchy-circle-leaves-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/programming'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (19, 2))
        self.add_line('p1-r1-3', (19, 2), (19, 8))
        self.add_line('p1-r1-4', (19, 8), (16, 8))
        self.add_line('p1-r1-5', (16, 8), (13, 8))
        self.add_line('p1-r1-6', (13, 8), (13, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 8), (16, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 17), (8, 17))
        self.add_line('p3-r1-2', (8, 17), (8, 23))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (8, 23), (8, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (8, 30), (8, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 17), (24, 17))
        self.add_line('p5-r1-2', (24, 17), (24, 23))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_arc('p6-r1-1', (24, 23), (24, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p6-r1-2', (24, 30), (24, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
        self.relate("connect", 'p5-r1-2', 'p6-r1-1')
        self.relate("connect", 'p5-r1-2', 'p6-r1-2')
