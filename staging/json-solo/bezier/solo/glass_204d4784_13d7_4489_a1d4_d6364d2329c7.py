"""Glass (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204d4784-13d7-4489-a1d4-d6364d2329c7'
SOURCE_PATH = 'icons-json/drinks/glass_204d4784-13d7-4489-a1d4-d6364d2329c7.json'
AUTHOR = 'json_to_solo'

class Glass204d4784(Solo48):
    icon_id = 'glass-204d4784'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('glass', 'drinks')

    def build(self):
        self.add_line('e0', (24, 44), (24, 29))
        self.add_line('e1', (14, 44), (34, 44))
        self.add_line('e2', (8, 14), (8, 4))
        self.add_line('e3', (8, 4), (40, 4))
        self.add_line('e4', (40, 4), (40, 16))
        self.add_bezier('e5', (40, 16), ((40, 16.845), (39.31, 18.355), (38.95, 19.191)), ((36.49, 24.873), (30.66, 28.5), (24, 28.545)), ((17.14, 28.6), (10.92, 24.309), (8.81, 18.418)), ((8.38, 17.227), (8.02, 15.909), (8.02, 14.645)), ((8.01, 14.5), (8.01, 14.355), (8, 14.218)), ((8, 14.145), (8, 14.073), (8, 14)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
