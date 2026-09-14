"""One chilli (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2b0b7f2-a11c-4070-ad95-4be975eeef1e'
SOURCE_PATH = 'icons-json/symbol/one chilli_d2b0b7f2-a11c-4070-ad95-4be975eeef1e.json'
AUTHOR = 'json_to_solo'

class OneChilliSymbol(Solo48):
    icon_id = 'one-chilli-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('one', 'chilli', 'symbol')

    def build(self):
        self.add_line('e0', (40, 18), (43, 14))
        self.add_arc('e1-1', (40, 18), (34, 17), radius_x=5, sweep=False)
        self.add_arc('e1-2', (34, 17), (17, 29), radius_x=31)
        self.add_arc('e1-3', (17, 29), (4, 29), radius_x=36)
        self.add_arc('e1-4', (4, 29), (19, 40), radius_x=16, sweep=False)
        self.add_arc('e1-5', (19, 40), (23, 40), radius_x=79)
        self.add_arc('e1-6', (23, 40), (30, 38), radius_x=21, sweep=False)
        self.add_arc('e1-7', (30, 38), (36, 34), radius_x=22, sweep=False)
        self.add_arc('e1-8', (36, 34), (40, 18), radius_x=12, sweep=False)
        self.add_line('e2-1', (43, 14), (44, 10))
        self.add_arc('e2-2', (44, 10), (44, 8), radius_x=22)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', closed=True)
        self.add_contour('c1', 'e0', 'e2-1', 'e2-2')
        self.relate('connect', 'c0', 'c1')
