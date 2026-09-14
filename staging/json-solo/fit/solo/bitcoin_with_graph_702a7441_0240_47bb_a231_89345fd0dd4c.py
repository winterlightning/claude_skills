"""Bitcoin with graph (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '702a7441-0240-47bb-a231-89345fd0dd4c'
SOURCE_PATH = 'icons-json/symbol/bitcoin with graph_702a7441-0240-47bb-a231-89345fd0dd4c.json'
AUTHOR = 'json_to_solo'

class BitcoinWithGraphSymbol(Solo48):
    icon_id = 'bitcoin-with-graph-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bitcoin', 'with', 'graph', 'symbol')

    def build(self):
        self.add_line('e0', (39, 8), (44, 8))
        self.add_line('e1', (44, 8), (44, 14))
        self.add_line('e2', (44, 8), (27, 40))
        self.add_line('e3', (27, 40), (16, 17))
        self.add_line('e4', (16, 17), (4, 38))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
