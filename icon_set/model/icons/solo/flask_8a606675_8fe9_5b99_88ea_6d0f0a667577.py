"""Flask (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a606675-8fe9-5b99-88ea-6d0f0a667577'
SOURCE_PATH = 'icons-json/drinks/flask_8a606675-8fe9-5b99-88ea-6d0f0a667577.json'
AUTHOR = 'gpt-6'

class Flask(Solo48):
    icon_id = 'flask'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('flask', 'drinks')

    def build(self):
        self.add_line('e0', (35, 29), (13, 29))
        self.add_line('e1', (31, 4), (17, 4))
        self.add_line('e2', (29, 4), (29, 15))
        self.add_line('e4', (33, 44), (14, 44))
        self.add_line('e5', (9, 35), (18, 19))
        self.add_line('e6', (19, 14), (19, 4))
        self.add_line('e7', (29, 15), (39, 35))
        self.add_arc('e8-1', (39, 35), (40, 38), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e8-2', (40, 38), (37, 43), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('e8-3', (37, 43), (33, 44))
        self.add_arc('e9-1', (14, 44), (8, 38), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e9-2', (8, 38), (9, 35), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e10', (18, 19), (19, 14))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e7', 'e8-1', 'e8-2', 'e8-3', 'e4', 'e9-1', 'e9-2', 'e5', 'e10', 'e6', closed=False)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
