"""Hexagon (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b80eece-f8c5-5b40-be2c-8ab9383900e3'
SOURCE_PATH = 'icons-json/design/hexagon_3b80eece-f8c5-5b40-be2c-8ab9383900e3.json'
AUTHOR = 'json_to_solo'

class Hexagon(Solo48):
    icon_id = 'hexagon-3b80eece'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'design')

    def build(self):
        self.add_line('e0', (23, 44), (10, 35))
        self.add_line('e1', (8, 31), (8, 16))
        self.add_line('e2', (11, 12), (22, 5))
        self.add_line('e3', (26, 5), (38, 12))
        self.add_line('e4', (40, 17), (40, 32))
        self.add_line('e5', (37, 36), (26, 43))
        self.add_line('e6', (26, 43), (23, 44))
        self.add_line('e7-1', (10, 35), (8, 32))
        self.add_line('e7-2', (8, 32), (8, 31))
        self.add_line('e8-1', (8, 16), (8, 15))
        self.add_line('e8-2', (8, 15), (11, 12))
        self.add_arc('e9-1', (22, 5), (24, 4), radius_x=3)
        self.add_arc('e9-2', (24, 4), (26, 5), radius_x=3)
        self.add_arc('e10-1', (38, 12), (40, 15), radius_x=4)
        self.add_arc('e10-2', (40, 15), (40, 17), radius_x=23, sweep=False)
        self.add_line('e11-1', (40, 32), (39, 35))
        self.add_line('e11-2', (39, 35), (37, 36))
        self.add_contour('c0', 'e6', 'e0', 'e7-1', 'e7-2', 'e1', 'e8-1', 'e8-2', 'e2', 'e9-1', 'e9-2', 'e3', 'e10-1', 'e10-2', 'e4', 'e11-1', 'e11-2', 'e5', closed=True)
