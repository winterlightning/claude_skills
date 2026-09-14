"""Arrow thick top (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4'
SOURCE_PATH = 'icons-json/symbol/arrow thick top_e3d7b5b6-09dd-4914-98aa-6e9e8e9481e4.json'
AUTHOR = 'json_to_solo'

class ArrowThickTopSymbol(Solo48):
    icon_id = 'arrow-thick-top-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'symbol')

    def build(self):
        self.add_line('e0', (8, 24), (24, 4))
        self.add_line('e1', (24, 4), (38, 22))
        self.add_line('e2', (38, 22), (40, 24))
        self.add_line('e3', (40, 24), (32, 24))
        self.add_line('e4', (32, 24), (32, 42))
        self.add_line('e5', (31, 44), (16, 44))
        self.add_line('e6', (16, 44), (16, 24))
        self.add_line('e7', (16, 24), (8, 24))
        self.add_arc('e8', (32, 42), (31, 44), radius_x=2)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e8', 'e5', 'e6', 'e7', closed=True)
