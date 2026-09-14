"""U turn right (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cd89078-9ea5-43e7-8b53-fc1e7797e607'
SOURCE_PATH = 'icons-json/transportation/u turn right_3cd89078-9ea5-43e7-8b53-fc1e7797e607.json'
AUTHOR = 'json_to_solo'

class UTurnRight(Solo48):
    icon_id = 'u-turn-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('u', 'turn', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (6, 42), (6, 22))
        self.add_line('e1', (35, 27), (35, 34))
        self.add_line('e2', (35, 34), (42, 25))
        self.add_line('e3', (35, 34), (24, 24))
        self.add_line('e4-1', (6, 22), (7, 15))
        self.add_arc('e4-2', (7, 15), (20, 6), radius_x=14)
        self.add_line('e4-3', (20, 6), (26, 7))
        self.add_arc('e4-4', (26, 7), (32, 12), radius_x=14)
        self.add_arc('e4-5', (32, 12), (35, 27), radius_x=23)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
