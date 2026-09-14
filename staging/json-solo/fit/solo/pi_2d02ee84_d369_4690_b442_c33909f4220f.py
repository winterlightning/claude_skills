"""Pi (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d02ee84-d369-4690-b442-c33909f4220f'
SOURCE_PATH = 'icons-json/symbol/pi_2d02ee84-d369-4690-b442-c33909f4220f.json'
AUTHOR = 'json_to_solo'

class PiSymbol(Solo48):
    icon_id = 'pi-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pi', 'symbol')

    def build(self):
        self.add_line('e0', (13, 8), (44, 8))
        self.add_line('e1', (32, 28), (34, 8))
        self.add_arc('e2', (4, 16), (13, 8), radius_x=10)
        self.add_arc('e3-1', (9, 40), (13, 31), radius_x=56, sweep=False)
        self.add_line('e3-2', (13, 31), (17, 8))
        self.add_arc('e4-1', (42, 37), (37, 40), radius_x=6)
        self.add_arc('e4-2', (37, 40), (33, 38), radius_x=5)
        self.add_arc('e4-3', (33, 38), (32, 28), radius_x=17)
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e3-1', 'e3-2')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
