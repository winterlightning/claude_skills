"""Twitter logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cce9d468-ea2e-4285-afbc-349265e00c73'
SOURCE_PATH = 'icons-json/logos/twitter logo 1_cce9d468-ea2e-4285-afbc-349265e00c73.json'
AUTHOR = 'json_to_solo'

class TwitterLogo1Logos(Solo48):
    icon_id = 'twitter-logo-1-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('twitter', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (20, 24), (20, 30))
        self.add_line('e1', (23, 34), (35, 34))
        self.add_line('e2', (35, 44), (22, 44))
        self.add_line('e3', (8, 30), (8, 9))
        self.add_line('e4', (19, 9), (19, 13))
        self.add_line('e5', (19, 13), (34, 13))
        self.add_line('e6', (34, 23), (20, 23))
        self.add_bezier('e7', (20, 30), ((20, 31.473), (21.04, 33.491), (22.66, 33.855)), ((22.78, 33.882), (22.87, 34), (23, 34)))
        self.add_bezier('e8', (35, 34), ((35.05, 34), (35.35, 34.136), (35.44, 34.155)), ((37.52, 34.555), (39.98, 36.855), (39.98, 38.873)), ((39.98, 38.973), (40, 39.073), (40, 39.173)), ((40, 39.174), (40, 39.175), (40, 39.176)), ((40, 39.247), (39.99, 39.31), (39.99, 39.382)), ((39.99, 41.318), (37.3, 43.991), (35.11, 43.991)), ((35.07, 43.991), (35.04, 44), (35, 44)))
        self.add_bezier('e9', (22, 44), ((21.91, 43.991), (21.82, 43.991), (21.73, 43.982)), ((20.96, 43.982), (20.11, 43.745), (19.38, 43.555)), ((14.06, 42.218), (10.09, 38.082), (8.63, 33.327)), ((8.36, 32.427), (8.01, 31.409), (8.01, 30.473)), ((8.01, 30.436), (8, 30.036), (8, 30)))
        self.add_bezier('e10', (8, 9), ((8, 8.964), (8.01, 8.464), (8.01, 8.427)), ((8.01, 6.336), (11.07, 4.009), (13.26, 4.009)), ((13.368, 4.009), (13.477, 4), (13.585, 4)), ((13.587, 4), (13.588, 4), (13.59, 4)), ((13.73, 4), (13.87, 4.018), (14.01, 4.018)), ((16.48, 4.018), (19, 6.773), (19, 9)))
        self.add_bezier('e11', (34, 13), ((34.7, 13), (35.67, 13.591), (36.25, 13.936)), ((39.71, 15.991), (39.84, 21.027), (35.78, 22.609)), ((35.29, 22.8), (34.53, 23), (34, 23)))
        self.add_bezier('e12', (20, 23), ((20, 23.3), (20, 23.7), (20, 24)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e5', 'e11', 'e6', 'e12', closed=True)
