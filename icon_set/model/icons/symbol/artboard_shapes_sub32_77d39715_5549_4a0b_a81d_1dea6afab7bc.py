"""Independent 32px profile of artboard-shapes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '77d39715-5549-4a0b-a81d-1dea6afab7bc'
SOURCE_PATH = 'pictographic-primitives/design/artboard shapes_77d39715-5549-4a0b-a81d-1dea6afab7bc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('77d39715-5549-4a0b-a81d-1dea6afab7bc', 'pictographic-primitives/design/artboard shapes_77d39715-5549-4a0b-a81d-1dea6afab7bc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/artboard-shapes',)
SOLO_SOURCE_ICON_IDS = ('artboard-shapes',)
REFERENCE_EXPORT_SHA256 = '73ff57a59b7549ac3b61f9d8ffa0a641f7b629b7fa0ecd1f2fd9e5e97a04d198'

class Drawing(Sub32):
    icon_id = 'artboard-shapes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 10), (16, 5))
        self.add_arc('p1-r1-2', (16, 5), (13, 2), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (13, 2), (5, 2))
        self.add_arc('p1-r1-4', (5, 2), (2, 5), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (2, 5), (2, 18))
        self.add_arc('p1-r1-6', (2, 18), (5, 21), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (5, 21), (10, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (13, 10), (16, 10))
        self.add_line('p2-r1-2', (16, 10), (27, 10))
        self.add_arc('p2-r1-3', (27, 10), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (30, 13), (30, 27))
        self.add_arc('p2-r1-5', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (27, 30), (13, 30))
        self.add_arc('p2-r1-7', (13, 30), (10, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (10, 27), (10, 21))
        self.add_line('p2-r1-9', (10, 21), (10, 13))
        self.add_arc('p2-r1-10', (10, 13), (13, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-7', 'p2-r1-8')
        self.relate('connect', 'p1-r1-7', 'p2-r1-9')
