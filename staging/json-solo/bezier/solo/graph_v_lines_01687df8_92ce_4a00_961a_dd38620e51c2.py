"""Graph v lines (business), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01687df8-92ce-4a00-961a-dd38620e51c2'
SOURCE_PATH = 'icons-json/business/graph v lines_01687df8-92ce-4a00-961a-dd38620e51c2.json'
AUTHOR = 'json_to_solo'

class GraphVLinesBusiness(Solo48):
    icon_id = 'graph-v-lines-business'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('graph', 'v', 'lines', 'business')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (6, 42), (26, 42))
        self.add_line('e2', (26, 42), (13, 31))
        self.add_line('e3', (13, 31), (21, 25))
        self.add_line('e4', (21, 25), (16, 18))
        self.add_line('e5', (16, 18), (22, 13))
        self.add_line('e6', (42, 42), (40, 42))
        self.add_line('e7', (15, 6), (22, 13))
        self.add_line('e8', (40, 42), (27, 26))
        self.add_line('e9', (27, 26), (37, 16))
        self.add_line('e10', (37, 16), (28, 6))
        self.add_line('e11', (28, 6), (22, 13))
        self.add_line('e12', (40, 42), (22, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8', 'e9', 'e10', 'e11')
        self.add_contour('c4', 'e12')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c4', 'c0')
