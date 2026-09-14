"""Tb (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6a3dfcf-edb2-4acf-9789-b669c4727a01'
SOURCE_PATH = 'icons-json/symbol/tb (text u)_c6a3dfcf-edb2-4acf-9789-b669c4727a01.json'
AUTHOR = 'json_to_solo'

class TbTextUSymbol(Solo48):
    icon_id = 'tb-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('tb', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (21, 4))
        self.add_line('e1', (15, 27), (15, 4))
        self.add_line('e2', (30, 4), (30, 20))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_arc('e4-1', (37, 12), (30, 22), radius_x=7, sweep=False)
        self.add_arc('e4-2', (30, 22), (37, 26), radius_x=5, sweep=False)
        self.add_line('e4-3', (37, 26), (39, 24))
        self.add_line('e4-4', (39, 24), (40, 18))
        self.add_arc('e4-5', (40, 18), (39, 14), radius_x=9, sweep=False)
        self.add_line('e4-6', (39, 14), (37, 12))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c4')
