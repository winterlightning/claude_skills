"""Tray (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '028a2382-a657-4cdb-802e-defa023b4886'
SOURCE_PATH = 'icons-json/symbol/tray_028a2382-a657-4cdb-802e-defa023b4886.json'
AUTHOR = 'json_to_solo'

class TraySymbol(Solo48):
    icon_id = 'tray-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('tray', 'symbol')

    def build(self):
        self.add_line('e0', (4, 40), (41, 40))
        self.add_line('e1', (7, 31), (7, 40))
        self.add_line('e2', (44, 40), (41, 40))
        self.add_arc('e3-1', (41, 40), (29, 11), radius_x=27, sweep=False)
        self.add_arc('e3-2', (29, 11), (7, 31), radius_x=19, sweep=False)
        self.add_line('e4', (24, 8), (24, 10))
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c2', 'c0')
