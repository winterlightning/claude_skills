"""Flask (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a606675-8fe9-5b99-88ea-6d0f0a667577'
SOURCE_PATH = 'icons-json/drinks/flask_8a606675-8fe9-5b99-88ea-6d0f0a667577.json'
AUTHOR = 'json_to_solo'

class FlaskDrinks(Solo48):
    icon_id = 'flask-drinks'
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
        self.add_line('e3', (31, 19), (39, 35))
        self.add_line('e4', (33, 44), (14, 44))
        self.add_line('e5', (9, 35), (18, 19))
        self.add_line('e6', (19, 14), (19, 4))
        self.add_bezier('e7', (29, 15), ((29, 16.636), (30.27, 17.582), (31, 19)))
        self.add_bezier('e8', (39, 35), ((39.39, 35.764), (39.99, 36.782), (39.99, 37.636)), ((39.99, 37.709), (40, 37.782), (40, 37.855)), ((40, 37.856), (40, 37.857), (40, 37.858)), ((40, 37.93), (40, 38.001), (40, 38.073)), ((40, 40.682), (36.91, 43.991), (33.92, 43.991)), ((33.77, 43.991), (33.62, 44), (33.46, 44)), ((33.31, 44), (33.15, 44), (33, 44)))
        self.add_bezier('e9', (14, 44), ((11.13, 44), (8.02, 41.236), (8.02, 38.609)), ((8.01, 38.473), (8.01, 38.327), (8, 38.182)), ((8, 38.181), (8, 38.18), (8, 38.179)), ((8, 38.116), (8, 38.044), (8.01, 37.973)), ((8.01, 36.991), (8.52, 35.873), (9, 35)))
        self.add_bezier('e10', (18, 19), ((18.8, 17.545), (19, 15.591), (19, 14)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
