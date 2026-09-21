"""Pu (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e41d9405-ab74-46da-af5a-21bfd17b16e3'
SOURCE_PATH = 'icons-json/symbol/pu (text u)_e41d9405-ab74-46da-af5a-21bfd17b16e3.json'
AUTHOR = 'json_to_solo'

class PuTextU(Solo48):
    icon_id = 'pu-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pu', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (16, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (30, 12), (30, 22))
        self.add_line('e4', (40, 12), (40, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_arc('e6-1', (15, 16), (21, 11), radius_x=7, sweep=False)
        self.add_arc('e6-2', (21, 11), (16, 4), radius_x=6, sweep=False)
        self.add_arc('e7', (30, 22), (40, 22), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c1', 'c2')
