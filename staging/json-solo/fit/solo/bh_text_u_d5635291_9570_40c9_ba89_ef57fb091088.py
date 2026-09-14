"""Bh (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5635291-9570-40c9-ba89-ef57fb091088'
SOURCE_PATH = 'icons-json/symbol/bh (text u)_d5635291-9570-40c9-ba89-ef57fb091088.json'
AUTHOR = 'json_to_solo'

class BhTextUSymbol(Solo48):
    icon_id = 'bh-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bh', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (15, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (13, 27))
        self.add_line('e3', (16, 15), (8, 15))
        self.add_line('e4', (30, 4), (30, 27))
        self.add_line('e5', (40, 19), (40, 27))
        self.add_line('e6', (8, 44), (40, 44))
        self.add_arc('e7-1', (13, 27), (21, 19), radius_x=7, sweep=False)
        self.add_arc('e7-2', (21, 19), (16, 15), radius_x=6, sweep=False)
        self.add_arc('e7-3', (16, 15), (20, 11), radius_x=6, sweep=False)
        self.add_arc('e7-4', (20, 11), (15, 4), radius_x=6, sweep=False)
        self.add_arc('e8-1', (30, 15), (37, 12), radius_x=5)
        self.add_arc('e8-2', (37, 12), (39, 14), radius_x=4)
        self.add_line('e8-3', (39, 14), (40, 18))
        self.add_line('e8-4', (40, 18), (40, 19))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
