"""Cake (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffca9ae9-2486-4950-9183-fda6e50cd3ce'
SOURCE_PATH = 'icons-json/symbol/cake_ffca9ae9-2486-4950-9183-fda6e50cd3ce.json'
AUTHOR = 'json_to_solo'

class Cake(Solo48):
    icon_id = 'cake'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cake', 'symbol')

    def build(self):
        self.add_line('e0', (4, 29), (44, 29))
        self.add_line('e1', (44, 29), (44, 40))
        self.add_line('e2', (44, 40), (4, 40))
        self.add_line('e3', (4, 40), (4, 27))
        self.add_line('e4', (30, 17), (44, 29))
        self.add_arc('e5-top', (19, 14), (31, 14), radius_x=6)
        self.add_arc('e5-bottom', (31, 14), (19, 14), radius_x=6)
        self.add_arc('e6', (4, 27), (19, 13), radius_x=16)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e6')
        self.add_contour('c1', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
