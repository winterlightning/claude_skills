"""Arrow undo left (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7537cdc-4cea-48b0-984d-3fbfb720fe25'
SOURCE_PATH = 'icons-json/symbol/arrow undo left_e7537cdc-4cea-48b0-984d-3fbfb720fe25.json'
AUTHOR = 'json_to_solo'

class ArrowUndoLeft(Solo48):
    icon_id = 'arrow-undo-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'undo', 'left', 'symbol')

    def build(self):
        self.add_line('e0', (25, 8), (33, 8))
        self.add_line('e1', (36, 31), (4, 31))
        self.add_line('e2', (13, 21), (4, 31))
        self.add_line('e3', (13, 40), (4, 31))
        self.add_arc('e4-1', (33, 8), (44, 20), radius_x=13)
        self.add_line('e4-2', (44, 20), (42, 27))
        self.add_arc('e4-3', (42, 27), (36, 31), radius_x=8)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
