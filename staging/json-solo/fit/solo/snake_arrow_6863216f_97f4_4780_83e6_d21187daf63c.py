"""Snake arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6863216f-97f4-4780-83e6-d21187daf63c'
SOURCE_PATH = 'icons-json/arrows/snake arrow_6863216f-97f4-4780-83e6-d21187daf63c.json'
AUTHOR = 'json_to_solo'

class SnakeArrowArrows(Solo48):
    icon_id = 'snake-arrow-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('snake', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (22, 6), (22, 13))
        self.add_line('e1', (24, 14), (38, 14))
        self.add_line('e2', (38, 22), (10, 22))
        self.add_line('e3', (10, 31), (22, 31))
        self.add_line('e4', (25, 34), (25, 42))
        self.add_line('e5', (25, 42), (20, 37))
        self.add_line('e6', (25, 42), (30, 37))
        self.add_line('e7', (22, 13), (24, 14))
        self.add_arc('e8-1', (38, 14), (42, 18), radius_x=4)
        self.add_arc('e8-2', (42, 18), (38, 22), radius_x=4)
        self.add_arc('e9-1', (10, 22), (6, 26), radius_x=4, sweep=False)
        self.add_line('e9-2', (6, 26), (7, 29))
        self.add_arc('e9-3', (7, 29), (10, 31), radius_x=5, sweep=False)
        self.add_arc('e10', (22, 31), (25, 34), radius_x=4)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e2', 'e9-1', 'e9-2', 'e9-3', 'e3', 'e10', 'e4', 'e5')
        self.add_contour('c1', 'e6')
        self.relate('connect', 'c0', 'c1')
