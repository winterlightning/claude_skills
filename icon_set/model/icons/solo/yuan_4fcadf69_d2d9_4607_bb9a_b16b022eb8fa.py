"""Yuan (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fcadf69-d2d9-4607-bb9a-b16b022eb8fa'
SOURCE_PATH = 'icons-json/symbol/yuan_4fcadf69-d2d9-4607-bb9a-b16b022eb8fa.json'
AUTHOR = 'json_to_solo'

class Yuan(Solo48):
    icon_id = 'yuan'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('yuan', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (24, 24))
        self.add_line('e1', (24, 24), (40, 4))
        self.add_line('e2', (24, 24), (24, 27))
        self.add_line('e3', (13, 27), (24, 27))
        self.add_line('e4', (24, 27), (24, 44))
        self.add_line('e5', (24, 27), (35, 27))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
