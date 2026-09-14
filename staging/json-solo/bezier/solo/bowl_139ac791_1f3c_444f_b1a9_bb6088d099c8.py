"""Bowl (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '139ac791-1f3c-444f-b1a9-bb6088d099c8'
SOURCE_PATH = 'icons-json/symbol/bowl_139ac791-1f3c-444f-b1a9-bb6088d099c8.json'
AUTHOR = 'json_to_solo'

class BowlSymbol(Solo48):
    icon_id = 'bowl-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bowl', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (33, 33), ((38.764, 29.283), (44, 18.775), (44, 10)))
        self.add_bezier('sym-e1', (44, 10), ((44, 9.606), (44, 9.394), (44, 9)))
        self.add_bezier('sym-e2', (44, 9), ((44, 8.754), (44, 8.246), (44, 8)))
        self.add_line('sym-e3', (44, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (4, 8))
        self.add_bezier('sym-e5', (4, 8), ((4, 8.246), (4, 8.754), (4, 9)))
        self.add_bezier('sym-e6', (4, 9), ((4, 9.394), (4, 9.606), (4, 10)))
        self.add_bezier('sym-e7', (4, 10), ((4, 18.775), (9.236, 29.283), (15, 33)))
        self.add_line('sym-e8', (15, 33), (15, 39))
        self.add_bezier('sym-e9', (15, 39), ((15.136, 39.32), (14.773, 39.778), (15, 40)))
        self.add_bezier('sym-e10', (15, 40), ((15.045, 40), (15.955, 40), (16, 40)))
        self.add_bezier('sym-e11', (16, 40), ((16.1, 40), (15.9, 39.951), (16, 40)))
        self.add_line('sym-e12', (16, 40), (24, 40))
        self.add_line('sym-e13', (24, 40), (32, 40))
        self.add_bezier('sym-e14', (32, 40), ((32.1, 39.951), (31.9, 40), (32, 40)))
        self.add_bezier('sym-e15', (32, 40), ((32.045, 40), (32.955, 40), (33, 40)))
        self.add_bezier('sym-e16', (33, 40), ((33.227, 39.778), (32.864, 39.32), (33, 39)))
        self.add_line('sym-e17', (33, 39), (33, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
