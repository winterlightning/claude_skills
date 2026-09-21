"""H (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96d68a91-3a00-41a4-a897-167cf369ad6f'
SOURCE_PATH = 'icons-json/symbol/h (text u)_96d68a91-3a00-41a4-a897-167cf369ad6f.json'
AUTHOR = 'json_to_solo'

class HTextU(Solo48):
    icon_id = 'h-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('h', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 33))
        self.add_line('e1', (40, 19), (8, 19))
        self.add_line('e2', (40, 33), (40, 4))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
