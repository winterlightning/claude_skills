"""U uranium (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee5f8122-b5e6-48ad-a907-9d33fc60a8b5'
SOURCE_PATH = 'icons-json/symbol/U Uranium_ee5f8122-b5e6-48ad-a907-9d33fc60a8b5.json'
AUTHOR = 'json_to_solo'

class UUraniumSymbol(Solo48):
    icon_id = 'u-uranium-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('u', 'uranium', 'symbol')

    def build(self):
        self.add_line('e0', (13, 4), (13, 20))
        self.add_line('e1', (36, 16), (36, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (13, 20), ((13, 20.873), (12.97, 22.136), (13.15, 23.009)), ((13.49, 24.636), (14.47, 26.027), (15.66, 27.245)), ((20.03, 31.736), (26.72, 32.109), (31.8, 28.391)), ((36, 25.3), (36, 20.464), (36, 16)))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('c1', 'e2')
