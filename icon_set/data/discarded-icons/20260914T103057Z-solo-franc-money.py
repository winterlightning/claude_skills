"""Franc (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a131a416-d088-45b5-bce4-841f689e7c6f'
SOURCE_PATH = 'icons-json/money/franc_a131a416-d088-45b5-bce4-841f689e7c6f.json'
AUTHOR = 'json_to_solo'

class FrancMoney(Solo48):
    icon_id = 'franc-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('franc', 'money')

    def build(self):
        self.add_line('e0', (40, 4), (16, 4))
        self.add_line('e1', (16, 4), (16, 44))
        self.add_line('e2', (8, 25), (34, 25))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
