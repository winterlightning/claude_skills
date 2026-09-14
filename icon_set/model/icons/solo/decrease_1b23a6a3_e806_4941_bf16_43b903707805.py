"""Decrease (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b23a6a3-e806-4941-bf16-43b903707805'
SOURCE_PATH = 'icons-json/symbol/decrease_1b23a6a3-e806-4941-bf16-43b903707805.json'
AUTHOR = 'json_to_solo'

class DecreaseSymbol(Solo48):
    icon_id = 'decrease-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('decrease', 'symbol')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_line('e1', (25, 42), (42, 42))
        self.add_line('e2', (42, 25), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
