"""Pr (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55570d4b-1ccd-4b43-bac8-4449335b0c0c'
SOURCE_PATH = 'icons-json/symbol/Pr_55570d4b-1ccd-4b43-bac8-4449335b0c0c.json'
AUTHOR = 'json_to_solo'

class PrSymbol(Solo48):
    icon_id = 'pr-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pr', 'symbol')

    def build(self):
        self.add_line('e0', (4, 25), (14, 25))
        self.add_line('e1', (14, 8), (4, 8))
        self.add_line('e2', (4, 8), (4, 40))
        self.add_line('e3', (33, 20), (33, 40))
        self.add_arc('e4-1', (14, 25), (21, 20), radius_x=9, sweep=False)
        self.add_arc('e4-2', (21, 20), (14, 8), radius_x=9, sweep=False)
        self.add_arc('e5', (44, 21), (33, 26), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c2', 'c1')
