"""Cup 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f748c868-065c-4348-8b9f-0e60c63d3e9f'
SOURCE_PATH = 'icons-json/symbol/cup 1_f748c868-065c-4348-8b9f-0e60c63d3e9f.json'
AUTHOR = 'json_to_solo'

class Cup1Symbol(Solo48):
    icon_id = 'cup-1-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cup', 'symbol')

    def build(self):
        self.add_line('e0', (34, 13), (37, 13))
        self.add_line('e1', (34, 13), (34, 30))
        self.add_line('e2', (34, 13), (34, 8))
        self.add_line('e3', (34, 8), (4, 8))
        self.add_line('e4', (4, 8), (4, 31))
        self.add_line('e5', (15, 40), (24, 40))
        self.add_arc('e6-1', (37, 13), (43, 16), radius_x=7)
        self.add_line('e6-2', (43, 16), (44, 22))
        self.add_line('e6-3', (44, 22), (43, 26))
        self.add_arc('e6-4', (43, 26), (40, 29), radius_x=6)
        self.add_arc('e6-5', (40, 29), (34, 30), radius_x=15)
        self.add_arc('e7-1', (4, 31), (14, 40), radius_x=11, sweep=False)
        self.add_arc('e7-2', (14, 40), (15, 40), radius_x=22)
        self.add_arc('e8', (24, 40), (34, 30), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e7-1', 'e7-2', 'e5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
