"""Plus (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a49896f-7866-476f-8ec4-e23ccdbe5907'
SOURCE_PATH = 'icons-json/symbol/plus_3a49896f-7866-476f-8ec4-e23ccdbe5907.json'
AUTHOR = 'json_to_solo'

class Plus3a49896f(Solo48):
    icon_id = 'plus-3a49896f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('plus', 'symbol')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (6, 24), (42, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
