"""+1 (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '014b4126-429a-4160-8632-9d676a0117a8'
SOURCE_PATH = 'icons-json/symbol/+1 (text)_014b4126-429a-4160-8632-9d676a0117a8.json'
AUTHOR = 'json_to_solo'

class Icon1Text(Solo48):
    icon_id = 'icon-1-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('text', 'symbol')

    def build(self):
        self.add_line('e0', (33, 15), (44, 8))
        self.add_line('e1', (44, 8), (40, 40))
        self.add_line('e2', (15, 13), (15, 35))
        self.add_line('e3', (4, 24), (26, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
