"""Te (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c11d8345-5e6e-493f-985d-ee6acb6e9b09'
SOURCE_PATH = 'icons-json/symbol/te (text u)_c11d8345-5e6e-493f-985d-ee6acb6e9b09.json'
AUTHOR = 'json_to_solo'

class TeTextUSymbol(Solo48):
    icon_id = 'te-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('te', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (22, 4))
        self.add_line('e1', (16, 27), (16, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_arc('e3-1', (30, 19), (40, 17), radius_x=7, sweep=False)
        self.add_arc('e3-2', (40, 17), (35, 12), radius_x=5, sweep=False)
        self.add_arc('e3-3', (35, 12), (30, 20), radius_x=7, sweep=False)
        self.add_arc('e3-4', (30, 20), (33, 26), radius_x=7, sweep=False)
        self.add_arc('e3-5', (33, 26), (40, 23), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c1', 'c0')
