"""Drug (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f8c6783-8fc1-48cd-91eb-d70ff753e4b6'
SOURCE_PATH = 'icons-json/symbol/drug_1f8c6783-8fc1-48cd-91eb-d70ff753e4b6.json'
AUTHOR = 'json_to_solo'

class DrugSymbol(Solo48):
    icon_id = 'drug-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('drug', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 24), (31, 31))
        self.add_line('sym-e1', (31, 31), (39, 23))
        self.add_bezier('sym-e2', (39, 23), ((40.767, 21.233), (42, 18.577), (42, 16)))
        self.add_bezier('sym-e3', (42, 16), ((42, 15.828), (42, 16.172), (42, 16)))
        self.add_bezier('sym-e4', (42, 16), ((42, 13.406), (40.809, 10.822), (39, 9)))
        self.add_bezier('sym-e5', (39, 9), ((37.178, 7.191), (34.594, 6), (32, 6)))
        self.add_bezier('sym-e6', (32, 6), ((31.828, 6), (32.172, 6), (32, 6)))
        self.add_bezier('sym-e7', (32, 6), ((29.423, 6), (26.767, 7.233), (25, 9)))
        self.add_line('sym-e8', (25, 9), (17, 17))
        self.add_line('sym-e9', (17, 17), (24, 24))
        self.add_bezier('sym-e10', (9, 39), ((10.822, 40.809), (13.406, 42), (16, 42)))
        self.add_bezier('sym-e11', (16, 42), ((16.172, 42), (15.828, 42), (16, 42)))
        self.add_bezier('sym-e12', (16, 42), ((18.577, 42), (21.233, 40.767), (23, 39)))
        self.add_line('sym-e13', (23, 39), (31, 31))
        self.add_bezier('sym-e14', (9, 39), ((7.191, 37.178), (6, 34.594), (6, 32)))
        self.add_bezier('sym-e15', (6, 32), ((6, 31.828), (6, 32.172), (6, 32)))
        self.add_bezier('sym-e16', (6, 32), ((6, 29.423), (7.233, 26.767), (9, 25)))
        self.add_line('sym-e17', (9, 25), (17, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
