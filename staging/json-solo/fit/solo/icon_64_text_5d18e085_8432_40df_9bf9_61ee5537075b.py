"""64 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d18e085-8432-40df-9bf9-61ee5537075b'
SOURCE_PATH = 'icons-json/text/64 (text)_5d18e085-8432-40df-9bf9-61ee5537075b.json'
AUTHOR = 'json_to_solo'

class Icon64TextText(Solo48):
    icon_id = 'icon-64-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (44, 33), (29, 33))
        self.add_line('e1', (29, 33), (41, 8))
        self.add_line('e2', (41, 8), (41, 40))
        self.add_arc('e3-1', (19, 13), (12, 8), radius_x=8, sweep=False)
        self.add_arc('e3-2', (12, 8), (5, 15), radius_x=9, sweep=False)
        self.add_line('e3-3', (5, 15), (4, 26))
        self.add_line('e3-4', (4, 26), (4, 29))
        self.add_line('e4-1', (4, 29), (6, 37))
        self.add_arc('e4-2', (6, 37), (8, 39), radius_x=8, sweep=False)
        self.add_line('e4-3', (8, 39), (12, 40))
        self.add_arc('e4-4', (12, 40), (17, 23), radius_x=11, sweep=False)
        self.add_arc('e4-5', (17, 23), (8, 21), radius_x=7, sweep=False)
        self.add_arc('e4-6', (8, 21), (4, 29), radius_x=12, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
        self.add_contour('c1', 'e0', 'e1', 'e2')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', closed=True)
        self.relate('connect', 'c0', 'c2')
