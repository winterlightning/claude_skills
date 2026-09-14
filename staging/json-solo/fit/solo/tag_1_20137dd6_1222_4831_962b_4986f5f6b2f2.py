"""Tag 1 (war), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20137dd6-1222-4831-962b-4986f5f6b2f2'
SOURCE_PATH = 'icons-json/war/tag 1_20137dd6-1222-4831-962b-4986f5f6b2f2.json'
AUTHOR = 'json_to_solo'

class Tag1War(Solo48):
    icon_id = 'tag-1-war'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('tag', 'war')

    def build(self):
        self.add_line('e0', (8, 42), (8, 18))
        self.add_line('e1', (9, 16), (24, 4))
        self.add_line('e2', (26, 5), (39, 16))
        self.add_line('e3', (40, 17), (40, 42))
        self.add_line('e4', (38, 44), (10, 44))
        self.add_arc('e5', (8, 18), (9, 16), radius_x=9)
        self.add_arc('e6', (24, 4), (26, 5), radius_x=6)
        self.add_arc('e7', (39, 16), (40, 17), radius_x=23)
        self.add_arc('e8', (40, 42), (38, 44), radius_x=2)
        self.add_arc('e9', (10, 44), (8, 42), radius_x=2)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
