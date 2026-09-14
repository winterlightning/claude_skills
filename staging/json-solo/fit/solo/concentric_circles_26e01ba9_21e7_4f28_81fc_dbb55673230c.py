"""Concentric circles (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26e01ba9-21e7-4f28-81fc-dbb55673230c'
SOURCE_PATH = 'icons-json/symbol/concentric circles_26e01ba9-21e7-4f28-81fc-dbb55673230c.json'
AUTHOR = 'json_to_solo'

class ConcentricCirclesSymbol(Solo48):
    icon_id = 'concentric-circles-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('concentric', 'circles', 'symbol')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (13, 24), (35, 24), radius_x=11)
        self.add_arc('e1-bottom', (35, 24), (13, 24), radius_x=11)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
