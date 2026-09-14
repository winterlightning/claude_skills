"""Exponential (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1195ed25-2865-5967-8377-ba7934eebadd'
SOURCE_PATH = 'icons-json/interface-essential/exponential_1195ed25-2865-5967-8377-ba7934eebadd.json'
AUTHOR = 'json_to_solo'

class Exponential1195ed25(Solo48):
    icon_id = 'exponential-1195ed25'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('exponential', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 13), (31, 21))
        self.add_line('e1', (31, 21), (42, 21))
        self.add_line('e2', (6, 21), (24, 42))
        self.add_line('e3', (6, 42), (24, 21))
        self.add_bezier('e4', (32, 9), ((32.957, 6.783), (34.44, 6.016), (36.911, 6.016)), ((37.104, 6.016), (37.298, 6), (37.491, 6)), ((37.494, 6), (37.497, 6), (37.5, 6)), ((39.75, 6), (42, 7.276), (42, 9.821)), ((42, 9.878), (41.992, 9.935), (41.992, 9.993)), ((41.992, 11.138), (40.884, 12.28), (40, 13)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
