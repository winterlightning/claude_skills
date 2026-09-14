"""Flag (social), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a4a1a0c-2f0a-46a0-9358-c8b505f82bb9'
SOURCE_PATH = 'icons-json/social/flag_9a4a1a0c-2f0a-46a0-9358-c8b505f82bb9.json'
AUTHOR = 'json_to_solo'

class Flag9a4a1a0c(Solo48):
    icon_id = 'flag-9a4a1a0c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (8, 4), (8, 8))
        self.add_line('e1', (8, 44), (8, 28))
        self.add_line('e2', (20, 9), (27, 7))
        self.add_line('e3', (40, 9), (37, 16))
        self.add_line('e4', (36, 18), (40, 28))
        self.add_line('e5', (28, 26), (21, 29))
        self.add_line('e6', (8, 8), (8, 28))
        self.add_arc('e7', (8, 8), (20, 9), radius_x=16, sweep=False)
        self.add_arc('e8', (27, 7), (40, 9), radius_x=14)
        self.add_arc('e9', (37, 16), (36, 18), radius_x=10, sweep=False)
        self.add_arc('e10', (40, 28), (28, 26), radius_x=15, sweep=False)
        self.add_arc('e11', (21, 29), (8, 28), radius_x=18)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
