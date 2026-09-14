"""Spinach (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee2140a-910a-408f-a46b-adcaa33ec5b6'
SOURCE_PATH = 'icons-json/symbol/spinach_4ee2140a-910a-408f-a46b-adcaa33ec5b6.json'
AUTHOR = 'json_to_solo'

class SpinachSymbol(Solo48):
    icon_id = 'spinach-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('spinach', 'symbol')

    def build(self):
        self.add_line('e0', (26, 18), (12, 44))
        self.add_line('e1', (12, 33), (15, 37))
        self.add_arc('e2-1', (15, 37), (38, 28), radius_x=23, sweep=False)
        self.add_line('e2-2', (38, 28), (40, 20))
        self.add_arc('e2-3', (40, 20), (34, 4), radius_x=26, sweep=False)
        self.add_arc('e2-4', (34, 4), (9, 20), radius_x=38, sweep=False)
        self.add_arc('e2-5', (9, 20), (8, 24), radius_x=10, sweep=False)
        self.add_arc('e2-6', (8, 24), (12, 33), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', closed=True)
        self.relate('connect', 'c1', 'c0')
