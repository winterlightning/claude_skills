"""Arrow dot left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ebf9acc-12df-4295-afb7-797830fc7f91'
SOURCE_PATH = 'icons-json/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.json'
AUTHOR = 'json_to_solo'

class ArrowDotLeft(Solo48):
    icon_id = 'arrow-dot-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (16, 24), (4, 24))
        self.add_line('e1', (4, 24), (11, 40))
        self.add_line('e2', (4, 24), (11, 8))
        self.add_line('e3', (24, 24), (29, 24))
        self.add_line('e4', (38, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
