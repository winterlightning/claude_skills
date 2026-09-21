"""2-1 (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17d5ec75-09d3-4664-bd59-09488d4395a3'
SOURCE_PATH = 'icons-json/symbol/2-1 (text)_17d5ec75-09d3-4664-bd59-09488d4395a3.json'
AUTHOR = 'json_to_solo'

class Icon21Text(Solo48):
    icon_id = 'icon-2-1-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('text', 'symbol')

    def build(self):
        self.add_line('e0', (11, 24), (4, 40))
        self.add_line('e1', (4, 40), (13, 40))
        self.add_line('e2', (44, 8), (44, 40))
        self.add_line('e3', (25, 22), (29, 22))
        self.add_arc('e4-1', (4, 14), (8, 8), radius_x=9)
        self.add_arc('e4-2', (8, 8), (11, 24), radius_x=11)
        self.add_arc('e5', (39, 14), (44, 8), radius_x=21, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e0', 'e1')
        self.add_contour('c1', 'e5', 'e2')
        self.add_contour('c2', 'e3')
