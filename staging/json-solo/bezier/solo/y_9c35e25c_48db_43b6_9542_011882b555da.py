"""Y (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c35e25c-48db-43b6-9542-011882b555da'
SOURCE_PATH = 'icons-json/typeface/y_9c35e25c-48db-43b6-9542-011882b555da.json'
AUTHOR = 'json_to_solo'

class Y9c35e25c(Solo48):
    icon_id = 'y-9c35e25c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('y', 'typeface')

    def build(self):
        self.add_line('e0', (8, 5), (25, 32))
        self.add_line('e1', (40, 4), (24, 35))
        self.add_bezier('e2', (24, 35), ((23.557, 35.845), (22.782, 36.582), (22.154, 37.355)), ((19.471, 40.645), (17.391, 42.3), (12.308, 43.445)), ((11.409, 43.645), (10.265, 43.991), (9.305, 43.991)), ((9.28, 43.991), (9.025, 44), (9, 44)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
