"""Three lines horizontal (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48ceef16-bc0f-47db-9f92-d1bfe04d9743'
SOURCE_PATH = 'icons-json/symbol/three lines horizontal_48ceef16-bc0f-47db-9f92-d1bfe04d9743.json'
AUTHOR = 'json_to_solo'

class ThreeLinesHorizontalSymbol(Solo48):
    icon_id = 'three-lines-horizontal-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('three', 'lines', 'horizontal', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
