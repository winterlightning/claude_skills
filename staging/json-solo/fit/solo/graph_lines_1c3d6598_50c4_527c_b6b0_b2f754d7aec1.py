"""Graph lines (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c3d6598-50c4-527c-b6b0-b2f754d7aec1'
SOURCE_PATH = 'icons-json/business/graph lines_1c3d6598-50c4-527c-b6b0-b2f754d7aec1.json'
AUTHOR = 'json_to_solo'

class GraphLinesBusiness(Solo48):
    icon_id = 'graph-lines-business'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('graph', 'lines', 'business')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (4, 40), (44, 40))
        self.add_line('e2', (4, 37), (19, 27))
        self.add_line('e3', (19, 27), (31, 32))
        self.add_line('e4', (31, 32), (44, 21))
        self.add_line('e5', (4, 27), (19, 14))
        self.add_line('e6', (19, 14), (29, 23))
        self.add_line('e7', (29, 23), (44, 10))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
