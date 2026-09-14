"""Virtual coin cyrpto currency (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '573e6276-1546-4e04-a069-78d9e36ee390'
SOURCE_PATH = 'icons-json/design/virtual coin cyrpto currency_573e6276-1546-4e04-a069-78d9e36ee390.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCyrptoCurrencyDesign(Solo48):
    icon_id = 'virtual-coin-cyrpto-currency-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('virtual', 'coin', 'cyrpto', 'currency', 'design')

    def build(self):
        self.add_line('e0', (41, 25), (25, 34))
        self.add_line('e1', (23, 34), (7, 25))
        self.add_line('e2', (7, 33), (23, 42))
        self.add_line('e3', (25, 42), (41, 33))
        self.add_line('e4', (7, 17), (23, 25))
        self.add_line('e5', (25, 25), (41, 17))
        self.add_line('e6', (41, 15), (25, 6))
        self.add_line('e7', (23, 6), (7, 15))
        self.add_line('e8-1', (40, 22), (42, 24))
        self.add_line('e8-2', (42, 24), (41, 25))
        self.add_line('e9', (25, 34), (23, 34))
        self.add_line('e10-1', (7, 25), (6, 24))
        self.add_line('e10-2', (6, 24), (8, 22))
        self.add_arc('e11-1', (8, 31), (6, 32), radius_x=3, sweep=False)
        self.add_arc('e11-2', (6, 32), (7, 33), radius_x=3, sweep=False)
        self.add_line('e12', (23, 42), (25, 42))
        self.add_arc('e13-1', (41, 33), (42, 32), radius_x=1, sweep=False)
        self.add_arc('e13-2', (42, 32), (40, 31), radius_x=2, sweep=False)
        self.add_line('e14', (23, 25), (25, 25))
        self.add_line('e15-1', (41, 17), (42, 16))
        self.add_arc('e15-2', (42, 16), (41, 15), radius_x=3, sweep=False)
        self.add_line('e16', (25, 6), (23, 6))
        self.add_line('e17-1', (7, 15), (6, 16))
        self.add_line('e17-2', (6, 16), (7, 17))
        self.add_contour('c0', 'e8-1', 'e8-2', 'e0', 'e9', 'e1', 'e10-1', 'e10-2')
        self.add_contour('c1', 'e11-1', 'e11-2', 'e2', 'e12', 'e3', 'e13-1', 'e13-2')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15-1', 'e15-2', 'e6', 'e16', 'e7', 'e17-1', 'e17-2', closed=True)
