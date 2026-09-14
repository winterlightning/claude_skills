"""Suitcase (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (39, 16), ((41.055, 16), (44, 18.105), (44, 20)))
        self.add_line('sym-e3', (44, 20), (44, 37))
        self.add_bezier('sym-e4', (44, 37), ((44, 38.465), (42.436, 39.629), (41, 40)))
        self.add_bezier('sym-e5', (41, 40), ((40.455, 40), (39.555, 40), (39, 40)))
        self.add_bezier('sym-e6', (39, 40), ((38.136, 40), (37.864, 40), (37, 40)))
        self.add_line('sym-e7', (37, 40), (35, 40))
        self.add_line('sym-e8', (35, 40), (24, 40))
        self.add_line('sym-e9', (24, 40), (13, 40))
        self.add_line('sym-e10', (13, 40), (13, 16))
        self.add_line('sym-e11', (13, 16), (9, 16))
        self.add_bezier('sym-e12', (9, 16), ((6.945, 16), (4, 18.105), (4, 20)))
        self.add_line('sym-e13', (4, 20), (4, 37))
        self.add_bezier('sym-e14', (4, 37), ((4, 38.465), (5.564, 39.629), (7, 40)))
        self.add_bezier('sym-e15', (7, 40), ((7.545, 40), (8.445, 40), (9, 40)))
        self.add_bezier('sym-e16', (9, 40), ((9.864, 40), (10.136, 40), (11, 40)))
        self.add_line('sym-e17', (11, 40), (13, 40))
        self.add_line('sym-e18', (24, 8), (29, 8))
        self.add_bezier('sym-e19', (29, 8), ((29.073, 8.008), (29.927, 8), (30, 8)))
        self.add_bezier('sym-e20', (30, 8), ((31.482, 8), (33, 9.678), (33, 11)))
        self.add_line('sym-e21', (33, 11), (33, 16))
        self.add_line('sym-e22', (33, 16), (35, 16))
        self.add_line('sym-e23', (33, 16), (24, 16))
        self.add_line('sym-e24', (24, 16), (15, 16))
        self.add_line('sym-e25', (15, 16), (15, 11))
        self.add_bezier('sym-e26', (15, 11), ((15, 9.678), (16.518, 8), (18, 8)))
        self.add_bezier('sym-e27', (18, 8), ((18.073, 8), (18.927, 8.008), (19, 8)))
        self.add_line('sym-e28', (19, 8), (24, 8))
        self.add_line('sym-e29', (13, 16), (15, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
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
