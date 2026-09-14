"""Graph stats descend (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a18c95dc-5f71-5078-af55-3d869e6f3b8a'
SOURCE_PATH = 'icons-json/interface-essential/graph stats descend_a18c95dc-5f71-5078-af55-3d869e6f3b8a.json'
AUTHOR = 'json_to_solo'

class GraphStatsDescend(Solo48):
    icon_id = 'graph-stats-descend'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('graph', 'stats', 'descend', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 40), (31, 19))
        self.add_line('e1', (30, 20), (22, 31))
        self.add_line('e2', (17, 28), (4, 8))
        self.add_line('e3', (44, 40), (36, 40))
        self.add_line('e4', (44, 40), (44, 29))
        self.add_arc('e5', (31, 19), (30, 20), radius_x=1)
        self.add_arc('e6-1', (22, 31), (20, 32), radius_x=2)
        self.add_line('e6-2', (20, 32), (17, 28))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-1', 'e6-2', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
