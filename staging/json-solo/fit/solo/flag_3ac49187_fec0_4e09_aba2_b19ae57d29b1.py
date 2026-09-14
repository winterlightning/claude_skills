"""Flag (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ac49187-fec0-4e09-aba2-b19ae57d29b1'
SOURCE_PATH = 'icons-json/social/flag_3ac49187-fec0-4e09-aba2-b19ae57d29b1.json'
AUTHOR = 'json_to_solo'

class Flag3ac49187(Solo48):
    icon_id = 'flag-3ac49187'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (12, 4), (12, 8))
        self.add_line('e1', (8, 44), (16, 44))
        self.add_line('e2', (23, 6), (29, 8))
        self.add_line('e3', (40, 7), (40, 23))
        self.add_line('e4', (29, 24), (23, 22))
        self.add_line('e5', (12, 8), (12, 24))
        self.add_line('e6', (12, 24), (12, 44))
        self.add_arc('e7', (12, 8), (23, 6), radius_x=15)
        self.add_arc('e8', (29, 8), (40, 7), radius_x=17, sweep=False)
        self.add_arc('e9', (40, 23), (29, 24), radius_x=13)
        self.add_arc('e10', (23, 22), (12, 24), radius_x=16, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c1')
