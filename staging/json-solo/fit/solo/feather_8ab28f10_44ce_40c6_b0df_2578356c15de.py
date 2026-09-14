"""Feather (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH = 'icons-json/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.json'
AUTHOR = 'json_to_solo'

class FeatherSymbol(Solo48):
    icon_id = 'feather-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('feather', 'symbol')

    def build(self):
        self.add_line('e0', (8, 44), (13, 37))
        self.add_line('e1', (13, 37), (31, 14))
        self.add_arc('e2-1', (13, 37), (13, 22), radius_x=12)
        self.add_arc('e2-2', (13, 22), (38, 4), radius_x=63)
        self.add_arc('e2-3', (38, 4), (40, 12), radius_x=20)
        self.add_arc('e2-4', (40, 12), (38, 20), radius_x=17)
        self.add_arc('e2-5', (38, 20), (28, 25), radius_x=54)
        self.add_arc('e3', (36, 24), (13, 37), radius_x=28)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5')
        self.add_contour('c1', 'e3', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
