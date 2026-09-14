"""Graph (finance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5552619f-de1f-40a4-b0e9-95549bca7398'
SOURCE_PATH = 'icons-json/finance/graph_5552619f-de1f-40a4-b0e9-95549bca7398.json'
AUTHOR = 'json_to_solo'

class GraphFinance(Solo48):
    icon_id = 'graph-finance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('graph', 'finance')

    def build(self):
        self.add_line('e0', (10, 8), (10, 40))
        self.add_line('e1', (4, 40), (44, 40))
        self.add_line('e2', (38, 22), (38, 40))
        self.add_line('e3', (24, 17), (24, 40))
        self.add_line('e4', (11, 40), (9, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c1')
