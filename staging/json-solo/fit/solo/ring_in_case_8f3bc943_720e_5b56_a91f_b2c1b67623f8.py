"""Batch-03/ring in case (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f3bc943-720e-5b56-a91f-b2c1b67623f8'
SOURCE_PATH = 'icons-json/accessories/batch-03/ring in case_8f3bc943-720e-5b56-a91f-b2c1b67623f8.json'
AUTHOR = 'json_to_solo'

class Batch03RingInCase(Solo48):
    icon_id = 'batch-03-ring-in-case'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'ring', 'in', 'case', 'accessories')

    def build(self):
        self.add_line('e0', (23, 24), (17, 17))
        self.add_line('e1', (17, 17), (20, 13))
        self.add_line('e2', (20, 13), (27, 13))
        self.add_line('e3', (31, 17), (25, 24))
        self.add_line('e4', (40, 33), (40, 10))
        self.add_line('e5', (36, 6), (13, 6))
        self.add_line('e6', (8, 11), (8, 33))
        self.add_line('e7', (6, 33), (42, 33))
        self.add_line('e8', (42, 33), (42, 37))
        self.add_line('e9', (36, 42), (11, 42))
        self.add_arc('e10', (31, 33), (23, 24), radius_x=7, sweep=False)
        self.add_arc('e11', (23, 24), (17, 33), radius_x=7, sweep=False)
        self.add_arc('e12', (27, 13), (31, 17), radius_x=8, sweep=False)
        self.add_arc('e13', (40, 10), (36, 6), radius_x=5, sweep=False)
        self.add_line('e14-1', (13, 6), (11, 6))
        self.add_arc('e14-2', (11, 6), (9, 8), radius_x=4, sweep=False)
        self.add_line('e14-3', (9, 8), (8, 11))
        self.add_arc('e15-1', (11, 42), (8, 41), radius_x=5)
        self.add_arc('e15-2', (8, 41), (6, 38), radius_x=4)
        self.add_line('e15-3', (6, 38), (6, 33))
        self.add_arc('e16-1', (42, 37), (37, 42), radius_x=5)
        self.add_line('e16-2', (37, 42), (36, 42))
        self.add_contour('c0', 'e10')
        self.add_contour('c1', 'e11')
        self.add_contour('c2', 'e0', 'e1', 'e2', 'e12', 'e3')
        self.add_contour('c3', 'e4', 'e13', 'e5', 'e14-1', 'e14-2', 'e14-3', 'e6')
        self.add_contour('c4', 'e15-1', 'e15-2', 'e15-3', 'e7', 'e8', 'e16-1', 'e16-2', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
