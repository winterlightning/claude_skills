"""U uranium (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e3-1', (13, 20), (29, 30), radius_x=11, sweep=False)
        self.add_arc('e3-2', (29, 30), (36, 16), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c1', 'e2')
