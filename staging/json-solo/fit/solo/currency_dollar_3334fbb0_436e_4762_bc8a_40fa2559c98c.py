"""Currency dollar (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3334fbb0-436e-4762-bc8a-40fa2559c98c'
SOURCE_PATH = 'icons-json/money/currency dollar_3334fbb0-436e-4762-bc8a-40fa2559c98c.json'
AUTHOR = 'json_to_solo'

class CurrencyDollarMoney(Solo48):
    icon_id = 'currency-dollar-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'dollar', 'money')

    def build(self):
        self.add_line('e0', (24, 4), (24, 10))
        self.add_line('e1', (24, 44), (24, 38))
        self.add_arc('e2-1', (8, 36), (31, 37), radius_x=57, sweep=False)
        self.add_arc('e2-2', (31, 37), (40, 31), radius_x=9, sweep=False)
        self.add_arc('e2-3', (40, 31), (37, 27), radius_x=5, sweep=False)
        self.add_arc('e2-4', (37, 27), (31, 25), radius_x=22, sweep=False)
        self.add_line('e2-5', (31, 25), (13, 22))
        self.add_arc('e2-6', (13, 22), (8, 17), radius_x=6)
        self.add_arc('e2-7', (8, 17), (16, 11), radius_x=8)
        self.add_arc('e2-8', (16, 11), (37, 12), radius_x=47)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
