"""Rupee (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de51d7c7-9816-483e-a837-47c58e3e6f91'
SOURCE_PATH = 'icons-json/money/rupee_de51d7c7-9816-483e-a837-47c58e3e6f91.json'
AUTHOR = 'json_to_solo'

class RupeeMoney(Solo48):
    icon_id = 'rupee-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('rupee', 'money')

    def build(self):
        self.add_line('e0', (30, 14), (40, 14))
        self.add_line('e1', (40, 4), (9, 4))
        self.add_line('e2', (23, 4), (28, 9))
        self.add_line('e3', (28, 9), (30, 14))
        self.add_line('e4', (30, 14), (8, 14))
        self.add_line('e5', (28, 44), (8, 25))
        self.add_arc('e6-1', (8, 25), (25, 23), radius_x=32, sweep=False)
        self.add_arc('e6-2', (25, 23), (30, 14), radius_x=11, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c2', 'c1')
