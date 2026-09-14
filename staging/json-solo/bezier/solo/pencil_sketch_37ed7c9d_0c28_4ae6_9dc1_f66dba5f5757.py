"""Pencil sketch (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37ed7c9d-0c28-4ae6-9dc1-f66dba5f5757'
SOURCE_PATH = 'icons-json/design/pencil sketch_37ed7c9d-0c28-4ae6-9dc1-f66dba5f5757.json'
AUTHOR = 'json_to_solo'

class PencilSketch37ed7c9d(Solo48):
    icon_id = 'pencil-sketch-37ed7c9d'
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
        self.add_bezier('sym-e7', (41, 15), ((41.442, 14.558), (42, 13.622), (42, 13)))
        self.add_bezier('sym-e8', (42, 13), ((42, 12.951), (42, 13.049), (42, 13)))
        self.add_bezier('sym-e9', (42, 13), ((41.992, 12.943), (42, 13.057), (42, 13)))
        self.add_bezier('sym-e10', (42, 13), ((42, 12.1), (40.317, 10.317), (39, 9)))
        self.add_bezier('sym-e11', (39, 9), ((37.683, 7.683), (35.9, 6), (35, 6)))
        self.add_bezier('sym-e12', (35, 6), ((34.943, 6), (35.057, 6.008), (35, 6)))
        self.add_bezier('sym-e13', (35, 6), ((34.951, 6), (35.049, 6), (35, 6)))
        self.add_bezier('sym-e14', (35, 6), ((34.378, 6), (33.442, 6.558), (33, 7)))
        self.add_line('sym-e15', (33, 7), (27, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
