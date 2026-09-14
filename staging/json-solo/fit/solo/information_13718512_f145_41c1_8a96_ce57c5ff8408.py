"""Information (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13718512-f145-41c1-8a96-ce57c5ff8408'
SOURCE_PATH = 'icons-json/symbol/information_13718512-f145-41c1-8a96-ce57c5ff8408.json'
AUTHOR = 'json_to_solo'

class InformationSymbol(Solo48):
    icon_id = 'information-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('information', 'symbol')

    def build(self):
        self.add_line('e0', (27, 4), (16, 4))
        self.add_line('e1', (8, 17), (24, 18))
        self.add_line('e2', (24, 18), (24, 44))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c1', 'c2')
