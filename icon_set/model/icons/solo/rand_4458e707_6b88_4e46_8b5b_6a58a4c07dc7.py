"""Rand (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4458e707-6b88-4e46-8b5b-6a58a4c07dc7'
SOURCE_PATH = 'icons-json/money/rand_4458e707-6b88-4e46-8b5b-6a58a4c07dc7.json'
AUTHOR = 'json_to_solo'

class Rand(Solo48):
    icon_id = 'rand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('rand', 'money')

    def build(self):
        self.add_line('e0', (25, 25), (8, 25))
        self.add_line('e1', (8, 44), (8, 26))
        self.add_line('e2', (40, 44), (25, 25))
        self.add_line('e3', (26, 4), (8, 4))
        self.add_line('e4', (8, 4), (8, 26))
        self.add_arc('e5-1', (25, 25), (40, 14), radius_x=13, sweep=False)
        self.add_arc('e5-2', (40, 14), (37, 8), radius_x=9, sweep=False)
        self.add_arc('e5-3', (37, 8), (26, 4), radius_x=18, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e3', 'e4')
        self.relate('connect', 'c0', 'c2')
