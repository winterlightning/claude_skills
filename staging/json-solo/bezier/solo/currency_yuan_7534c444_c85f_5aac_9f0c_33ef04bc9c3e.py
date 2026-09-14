"""Currency yuan (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7534c444-c85f-5aac-9f0c-33ef04bc9c3e'
SOURCE_PATH = 'icons-json/money/currency yuan_7534c444-c85f-5aac-9f0c-33ef04bc9c3e.json'
AUTHOR = 'json_to_solo'

class CurrencyYuanMoney(Solo48):
    icon_id = 'currency-yuan-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'yuan', 'money')

    def build(self):
        self.add_line('e0', (8, 4), (24, 24))
        self.add_line('e1', (24, 24), (24, 44))
        self.add_line('e2', (24, 24), (40, 4))
        self.add_line('e3', (13, 27), (35, 27))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
