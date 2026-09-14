"""Code 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '522a83e8-d72f-4794-850f-d282fc290164'
SOURCE_PATH = 'icons-json/symbol/code 1_522a83e8-d72f-4794-850f-d282fc290164.json'
AUTHOR = 'json_to_solo'

class Code1(Solo48):
    icon_id = 'code-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('code', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (17, 24))
        self.add_line('e1', (17, 24), (4, 40))
        self.add_line('e2', (28, 30), (44, 30))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
