"""Opposite arrows 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3af4f137-8a21-4788-937a-706e5d42fe1d'
SOURCE_PATH = 'icons-json/symbol/opposite arrows 1_3af4f137-8a21-4788-937a-706e5d42fe1d.json'
AUTHOR = 'json_to_solo'

class OppositeArrows1Symbol(Solo48):
    icon_id = 'opposite-arrows-1-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('opposite', 'arrows', 'symbol')

    def build(self):
        self.add_line('e0', (36, 8), (44, 16))
        self.add_line('e1', (44, 16), (6, 16))
        self.add_line('e2', (12, 40), (4, 32))
        self.add_line('e3', (4, 32), (42, 32))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
