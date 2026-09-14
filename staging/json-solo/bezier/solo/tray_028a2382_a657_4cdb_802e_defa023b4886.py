"""Tray (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (41, 40), ((40.973, 35.631), (41.536, 31.102), (40.609, 26.855)), ((38.445, 16.935), (31.791, 9.686), (24, 10.462)), ((16.791, 11.175), (11.682, 14.683), (8.391, 23.729)), ((7.627, 25.834), (7, 28.625), (7, 31)))
        self.add_bezier('e4', (24, 8), ((24, 8.825), (24, 9.175), (24, 10)))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c2', 'c0')
