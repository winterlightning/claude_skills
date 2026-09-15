"""Pencil sketch (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37ed7c9d-0c28-4ae6-9dc1-f66dba5f5757'
SOURCE_PATH = 'pictographic-primitives/design/pencil sketch_37ed7c9d-0c28-4ae6-9dc1-f66dba5f5757.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PencilSketch(Solo48):
    icon_id = 'pencil-sketch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pencil', 'sketch', 'design')

    def build(self):
        self.add_line('sym-e0', (31, 17), (35, 21))
        self.add_line('sym-e1', (35, 21), (17, 39))
        self.add_line('sym-e2', (17, 39), (6, 42))
        self.add_line('sym-e3', (6, 42), (9, 31))
        self.add_line('sym-e4', (9, 31), (27, 13))
        self.add_line('sym-e5', (27, 13), (31, 17))
        self.add_line('sym-e6', (35, 21), (41, 15))
        self.add_arc('sym-e7', (41, 15), (42, 13), radius_x=3, sweep=False)
        self.add_arc('sym-e10', (42, 13), (39, 9), radius_x=9, sweep=False)
        self.add_arc('sym-e11', (39, 9), (35, 6), radius_x=9, sweep=False)
        self.add_arc('sym-e14', (35, 6), (33, 7), radius_x=3, sweep=False)
        self.add_line('sym-e15', (33, 7), (27, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
