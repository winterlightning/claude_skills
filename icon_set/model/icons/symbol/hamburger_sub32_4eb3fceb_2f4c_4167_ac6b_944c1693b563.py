"""Independent 32px profile of hamburger.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4eb3fceb-2f4c-4167-ac6b-944c1693b563'
SOURCE_PATH = 'pictographic-primitives/symbol/hamburger_4eb3fceb-2f4c-4167-ac6b-944c1693b563.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4eb3fceb-2f4c-4167-ac6b-944c1693b563', 'pictographic-primitives/symbol/hamburger_4eb3fceb-2f4c-4167-ac6b-944c1693b563.svg'), ('8dc1040e-1d03-4e50-a902-d55864c7103f', 'pictographic-primitives/symbol/hamburger_8dc1040e-1d03-4e50-a902-d55864c7103f.svg'))
PROFILE_SOURCE_KEYS = ('solo/hamburger', 'solo/hamburger-symbol')
SOLO_SOURCE_ICON_IDS = ('hamburger', 'hamburger-symbol')
REFERENCE_EXPORT_SHA256 = '0d981a03352aeaf10768305676891d49a70ea3287e10ba404086b3bac0bd9ef9'

class Drawing(Sub32):
    icon_id = 'hamburger-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 13), (13, 5), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (13, 5), (19, 5))
        self.add_arc('p1-r1-3', (19, 5), (27, 13), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-4', (27, 13), ((29, 13), (30, 15), (30, 17)))
        self.add_bezier('p1-r1-5', (30, 17), ((30, 19), (29, 20), (27, 20)))
        self.add_arc('p1-r1-6', (27, 20), (20, 27), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (20, 27), (12, 27))
        self.add_arc('p1-r1-8', (12, 27), (5, 20), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-9', (5, 20), ((3, 20), (2, 19), (2, 17)))
        self.add_bezier('p1-r1-10', (2, 17), ((2, 15), (3, 13), (5, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (5, 20), (27, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (5, 13), ((6, 14), (7, 14), (8, 14)))
        self.add_bezier('p3-r1-2', (8, 14), ((8, 14), (9, 14), (10, 13)))
        self.add_bezier('p3-r1-3', (10, 13), ((11, 13), (12, 12), (13, 12)))
        self.add_bezier('p3-r1-4', (13, 12), ((14, 12), (15, 13), (16, 13)))
        self.add_bezier('p3-r1-5', (16, 13), ((17, 14), (18, 14), (19, 14)))
        self.add_bezier('p3-r1-6', (19, 14), ((20, 14), (21, 14), (22, 13)))
        self.add_bezier('p3-r1-7', (22, 13), ((23, 13), (24, 12), (24, 12)))
        self.add_bezier('p3-r1-8', (24, 12), ((25, 12), (26, 13), (27, 13)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-8')
        self.relate('connect', 'p1-r1-4', 'p3-r1-8')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p3-r1-1')
