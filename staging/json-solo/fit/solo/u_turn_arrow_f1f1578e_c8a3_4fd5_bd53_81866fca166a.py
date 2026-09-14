"""U turn arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1f1578e-c8a3-4fd5-bd53-81866fca166a'
SOURCE_PATH = 'icons-json/symbol/u turn arrow_f1f1578e-c8a3-4fd5-bd53-81866fca166a.json'
AUTHOR = 'json_to_solo'

class UTurnArrowSymbol(Solo48):
    icon_id = 'u-turn-arrow-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('u', 'turn', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (33, 39), (33, 16))
        self.add_line('e1', (33, 39), (27, 32))
        self.add_line('e2', (33, 39), (40, 32))
        self.add_line('e3', (8, 17), (8, 44))
        self.add_arc('e4', (33, 16), (21, 4), radius_x=12, sweep=False)
        self.add_arc('e5', (21, 4), (8, 17), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
