"""Tag 1 (war), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (8, 18), ((8.28, 17.327), (8.57, 16.618), (9, 16)))
        self.add_bezier('e6', (24, 4), ((24.61, 4.255), (25.48, 4.564), (26, 5)))
        self.add_bezier('e7', (39, 16), ((39.35, 16.291), (39.67, 16.7), (40, 17)))
        self.add_bezier('e8', (40, 42), ((40, 42.055), (39.99, 42.3), (39.99, 42.355)), ((39.99, 42.6), (39.87, 43.009), (39.71, 43.209)), ((38.93, 44), (38.85, 43.736), (38, 44)))
        self.add_bezier('e9', (10, 44), ((9.93, 44), (9.87, 44), (9.8, 43.991)), ((8.77, 43.991), (8, 42.891), (8, 42)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
