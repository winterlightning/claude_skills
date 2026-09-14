"""Suitcase (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '852d856f-d822-4896-b884-69ab6be018db'
SOURCE_PATH = 'icons-json/symbol/suitcase_852d856f-d822-4896-b884-69ab6be018db.json'
AUTHOR = 'json_to_solo'

class SuitcaseSymbol(Solo48):
    icon_id = 'suitcase-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('suitcase', 'symbol')

    def build(self):
        self.add_line('sym-e0', (35, 40), (35, 16))
        self.add_line('sym-e1', (35, 16), (39, 16))
        self.add_arc('sym-e2', (39, 16), (44, 20), radius_x=5)
        self.add_line('sym-e3', (44, 20), (44, 37))
        self.add_arc('sym-e4', (44, 37), (41, 40), radius_x=4)
        self.add_line('sym-e5-1', (41, 40), (40, 40))
        self.add_arc('sym-e5-2', (40, 40), (39, 40), radius_x=18, sweep=False)
        self.add_line('sym-e6', (39, 40), (37, 40))
        self.add_line('sym-e7', (37, 40), (35, 40))
        self.add_line('sym-e8', (35, 40), (24, 40))
        self.add_line('sym-e9', (24, 40), (13, 40))
        self.add_line('sym-e10', (13, 40), (13, 16))
        self.add_line('sym-e11', (13, 16), (9, 16))
        self.add_arc('sym-e12', (9, 16), (4, 20), radius_x=5, sweep=False)
        self.add_line('sym-e13', (4, 20), (4, 37))
        self.add_arc('sym-e14', (4, 37), (7, 40), radius_x=4, sweep=False)
        self.add_line('sym-e15-1', (7, 40), (8, 40))
        self.add_arc('sym-e15-2', (8, 40), (9, 40), radius_x=18)
        self.add_line('sym-e16', (9, 40), (11, 40))
        self.add_line('sym-e17', (11, 40), (13, 40))
        self.add_line('sym-e18', (24, 8), (29, 8))
        self.add_line('sym-e19', (29, 8), (30, 8))
        self.add_arc('sym-e20', (30, 8), (33, 11), radius_x=4)
        self.add_line('sym-e21', (33, 11), (33, 16))
        self.add_line('sym-e22', (33, 16), (35, 16))
        self.add_line('sym-e23', (33, 16), (24, 16))
        self.add_line('sym-e24', (24, 16), (15, 16))
        self.add_line('sym-e25', (15, 16), (15, 11))
        self.add_arc('sym-e26', (15, 11), (18, 8), radius_x=4)
        self.add_line('sym-e27', (18, 8), (19, 8))
        self.add_line('sym-e28', (19, 8), (24, 8))
        self.add_line('sym-e29', (13, 16), (15, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
        self.add_contour('sym-c3', 'sym-e29')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
