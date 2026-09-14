"""Fish rod (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03dbc4e5-5755-4b95-a62e-3b755dafdffb'
SOURCE_PATH = 'icons-json/symbol/fish rod_03dbc4e5-5755-4b95-a62e-3b755dafdffb.json'
AUTHOR = 'json_to_solo'

class FishRod(Solo48):
    icon_id = 'fish-rod'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fish', 'rod', 'symbol')

    def build(self):
        self.add_line('e0', (28, 23), (28, 37))
        self.add_line('e1', (8, 33), (9, 29))
        self.add_line('e2', (9, 29), (13, 33))
        self.add_bezier('e3', (38, 16), ((38.79, 14.791), (39.99, 13.082), (39.99, 11.618)), ((40, 11.556), (40, 11.484), (40, 11.421)), ((40, 11.42), (40, 11.419), (40, 11.418)), ((39.99, 11.273), (39.99, 11.136), (39.98, 11)), ((39.98, 10.245), (39.58, 9.509), (39.23, 8.845)), ((37.73, 6), (34.6, 4.009), (31.06, 4.009)), ((30.991, 4.009), (30.922, 4), (30.853, 4)), ((30.852, 4), (30.851, 4), (30.85, 4)), ((30.78, 4.009), (30.7, 4.009), (30.63, 4.018)), ((24.64, 4.018), (19.33, 10.3), (22.44, 15.391)), ((24.1, 18.109), (28, 19.491), (28, 23)))
        self.add_bezier('e4', (28, 37), ((28, 37.518), (27.72, 37.864), (27.54, 38.345)), ((26.21, 41.891), (21.91, 43.991), (17.95, 43.991)), ((17.72, 43.991), (17.5, 44), (17.27, 44)), ((17.269, 44), (17.268, 44), (17.267, 44)), ((17.208, 44), (17.149, 44), (17.09, 44)), ((12.51, 44), (8, 39.936), (8, 35.809)), ((8, 34.9), (8, 33.909), (8, 33)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1', 'e2')
