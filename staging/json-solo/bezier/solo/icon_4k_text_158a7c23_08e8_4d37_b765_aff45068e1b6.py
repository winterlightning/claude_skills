"""4k (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '158a7c23-08e8-4d37-b765-aff45068e1b6'
SOURCE_PATH = 'icons-json/text/4K (text)_158a7c23-08e8-4d37-b765-aff45068e1b6.json'
AUTHOR = 'json_to_solo'

class Icon4kTextText(Solo48):
    icon_id = 'icon-4k-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('4k', 'text')

    def build(self):
        self.add_line('e0', (19, 33), (4, 33))
        self.add_line('e1', (4, 33), (16, 8))
        self.add_line('e2', (16, 8), (16, 40))
        self.add_line('e3', (29, 8), (29, 26))
        self.add_line('e4', (29, 26), (31, 23))
        self.add_line('e5', (29, 40), (29, 23))
        self.add_line('e6', (44, 40), (31, 23))
        self.add_line('e7', (31, 23), (42, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6', 'e7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c1')
