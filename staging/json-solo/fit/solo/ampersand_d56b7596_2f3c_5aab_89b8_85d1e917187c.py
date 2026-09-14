"""Ampersand (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd56b7596-2f3c-5aab-89b8-85d1e917187c'
SOURCE_PATH = 'icons-json/interface-essential/ampersand_d56b7596-2f3c-5aab-89b8-85d1e917187c.json'
AUTHOR = 'json_to_solo'

class AmpersandInterfaceEssential(Solo48):
    icon_id = 'ampersand-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('ampersand', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 25), (23, 19))
        self.add_line('e1', (18, 16), (35, 37))
        self.add_line('e2', (35, 37), (40, 42))
        self.add_arc('e3-1', (40, 31), (19, 44), radius_x=30)
        self.add_line('e3-2', (19, 44), (12, 42))
        self.add_arc('e3-3', (12, 42), (8, 35), radius_x=9)
        self.add_arc('e3-4', (8, 35), (14, 25), radius_x=13)
        self.add_arc('e4-1', (23, 19), (29, 11), radius_x=15, sweep=False)
        self.add_arc('e4-2', (29, 11), (22, 4), radius_x=7, sweep=False)
        self.add_arc('e4-3', (22, 4), (18, 16), radius_x=7, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1', 'e2')
