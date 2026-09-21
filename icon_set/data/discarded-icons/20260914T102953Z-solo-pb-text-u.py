"""Pb (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a86d4c64-5422-40b0-81a1-1820524ddd2f'
SOURCE_PATH = 'icons-json/symbol/pb (text u)_a86d4c64-5422-40b0-81a1-1820524ddd2f.json'
AUTHOR = 'json_to_solo'

class PbTextU(Solo48):
    icon_id = 'pb-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pb', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (29, 4), (29, 20))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5-1', (15, 16), (20, 10), radius_x=6, sweep=False)
        self.add_arc('e5-2', (20, 10), (15, 4), radius_x=6, sweep=False)
        self.add_arc('e6-1', (37, 12), (31, 13), radius_x=5, sweep=False)
        self.add_arc('e6-2', (31, 13), (32, 26), radius_x=10, sweep=False)
        self.add_arc('e6-3', (32, 26), (38, 25), radius_x=6, sweep=False)
        self.add_arc('e6-4', (38, 25), (40, 21), radius_x=8, sweep=False)
        self.add_arc('e6-5', (40, 21), (40, 18), radius_x=18)
        self.add_line('e6-6', (40, 18), (39, 14))
        self.add_arc('e6-7', (39, 14), (37, 12), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', closed=True)
        self.relate('connect', 'c1', 'c3')
