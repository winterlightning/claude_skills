"""Peso (money), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfac5a0c-eae9-420e-af5e-4ac03cb24f16'
SOURCE_PATH = 'icons-json/money/peso_bfac5a0c-eae9-420e-af5e-4ac03cb24f16.json'
AUTHOR = 'json_to_solo'

class PesoMoney(Solo48):
    icon_id = 'peso-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('peso', 'money')

    def build(self):
        self.add_line('e0', (6, 24), (32, 24))
        self.add_line('e1', (23, 6), (14, 6))
        self.add_line('e2', (14, 6), (14, 42))
        self.add_arc('e3-1', (32, 24), (42, 16), radius_x=9, sweep=False)
        self.add_arc('e3-2', (42, 16), (37, 8), radius_x=10, sweep=False)
        self.add_arc('e3-3', (37, 8), (32, 6), radius_x=14, sweep=False)
        self.add_line('e3-4', (32, 6), (26, 6))
        self.add_arc('e3-5', (26, 6), (23, 6), radius_x=52)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e1', 'e2')
