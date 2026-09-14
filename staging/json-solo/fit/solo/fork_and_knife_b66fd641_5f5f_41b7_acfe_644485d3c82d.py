"""Fork and knife (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'icons-json/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.json'
AUTHOR = 'json_to_solo'

class ForkAndKnifeSymbol(Solo48):
    icon_id = 'fork-and-knife-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fork', 'and', 'knife', 'symbol')

    def build(self):
        self.add_line('e0', (21, 15), (21, 5))
        self.add_line('e1', (15, 23), (15, 5))
        self.add_line('e2', (15, 23), (13, 22))
        self.add_line('e3', (8, 17), (8, 5))
        self.add_line('e4', (15, 23), (15, 44))
        self.add_line('e5', (32, 27), (40, 27))
        self.add_line('e6', (40, 27), (40, 18))
        self.add_line('e7', (35, 7), (32, 4))
        self.add_line('e8', (32, 4), (32, 44))
        self.add_arc('e9', (15, 23), (21, 15), radius_x=8, sweep=False)
        self.add_arc('e10', (13, 22), (8, 17), radius_x=7)
        self.add_arc('e11', (40, 18), (35, 7), radius_x=19, sweep=False)
        self.add_contour('c0', 'e9', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e10', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e6', 'e11', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
