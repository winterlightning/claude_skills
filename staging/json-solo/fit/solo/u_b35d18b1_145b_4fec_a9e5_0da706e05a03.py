"""U (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b35d18b1-145b-4fec-a9e5-0da706e05a03'
SOURCE_PATH = 'icons-json/typeface/u_b35d18b1-145b-4fec-a9e5-0da706e05a03.json'
AUTHOR = 'json_to_solo'

class UB35d18b1(Solo48):
    icon_id = 'u-b35d18b1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('u', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (40, 44))
        self.add_line('e1-1', (8, 4), (9, 36))
        self.add_arc('e1-2', (9, 36), (14, 42), radius_x=9, sweep=False)
        self.add_line('e1-3', (14, 42), (25, 44))
        self.add_arc('e1-4', (25, 44), (27, 44), radius_x=40)
        self.add_arc('e1-5', (27, 44), (35, 41), radius_x=16, sweep=False)
        self.add_arc('e1-6', (35, 41), (40, 33), radius_x=10, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6')
        self.add_contour('c1', 'e0')
        self.relate('connect', 'c0', 'c1')
