"""Independent 32px profile of car-skidding.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2'
SOURCE_PATH = 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2', 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-skidding',)
SOLO_SOURCE_ICON_IDS = ('car-skidding',)
REFERENCE_EXPORT_SHA256 = '9c7d067718aebcceaa356212e3ce9f66c57820044d15f484cfef56e28b575b4d'

class Drawing(Sub32):
    icon_id = 'car-skidding-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 9), (9, 9))
        self.add_line('p1-r1-2', (9, 9), (23, 9))
        self.add_line('p1-r1-3', (23, 9), (25, 9))
        self.add_arc('p1-r1-4', (25, 9), (27, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 11), (27, 13))
        self.add_arc('p1-r1-6', (27, 13), (25, 15), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (25, 15), (7, 15))
        self.add_arc('p1-r1-8', (7, 15), (5, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (5, 13), (5, 11))
        self.add_arc('p1-r1-10', (5, 11), (7, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (9, 9), (12, 2))
        self.add_line('p2-r1-2', (12, 2), (20, 2))
        self.add_line('p2-r1-3', (20, 2), (23, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (10, 22), (10, 26), radius_x=3, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p3-r1-2', (10, 26), (10, 30), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (22, 22), (22, 26), radius_x=3, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p4-r1-2', (22, 26), (22, 30), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
