"""4 t (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5439420f-4735-4fc9-a2d7-5bc1b31545d8'
SOURCE_PATH = 'icons-json/text/4 T (text)_5439420f-4735-4fc9-a2d7-5bc1b31545d8.json'
AUTHOR = 'json_to_solo'

class Icon4TText(Solo48):
    icon_id = 'icon-4-t-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('t', 'text')

    def build(self):
        self.add_line('e0', (18, 33), (4, 33))
        self.add_line('e1', (4, 33), (16, 8))
        self.add_line('e2', (16, 8), (16, 40))
        self.add_line('e3', (28, 8), (44, 8))
        self.add_line('e4', (36, 40), (36, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c2', 'c1')
