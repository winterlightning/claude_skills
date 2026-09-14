"""Road curvy (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4833709a-4df3-5540-afa1-9f941f965c93'
SOURCE_PATH = 'icons-json/transportation/road curvy_4833709a-4df3-5540-afa1-9f941f965c93.json'
AUTHOR = 'json_to_solo'

class RoadCurvy(Solo48):
    icon_id = 'road-curvy'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('road', 'curvy', 'transportation')

    def build(self):
        self.add_line('e0', (33, 9), (38, 4))
        self.add_line('e1', (38, 4), (32, 5))
        self.add_line('e2', (13, 41), (8, 44))
        self.add_bezier('e3', (37, 44), ((38.38, 41.509), (39.99, 38.036), (39.99, 35.2)), ((39.99, 35.048), (40, 34.896), (40, 34.744)), ((40, 34.741), (40, 34.739), (40, 34.736)), ((40, 34.436), (39.99, 34.136), (39.99, 33.836)), ((39.99, 30.327), (38.09, 26.845), (35.35, 24.409)), ((33.92, 23.145), (32.14, 22.055), (30.88, 20.636)), ((28.47, 17.927), (28.44, 14.482), (30.38, 11.573)), ((31.11, 10.482), (32.01, 9.9), (33, 9)))
        self.add_bezier('e4', (32, 5), ((31.05, 5.145), (30.07, 5.427), (29.16, 5.709)), ((24.11, 7.282), (18.68, 10.082), (16.47, 14.736)), ((15.97, 15.791), (15.6, 17.009), (15.69, 18.164)), ((15.97, 21.991), (19.05, 23.991), (20.37, 27.245)), ((22.31, 32.018), (19.42, 36.218), (15.59, 39.355)), ((14.78, 40.018), (13.94, 40.491), (13, 41)))
        self.add_contour('c0', 'e3', 'e0', 'e1', 'e4', 'e2')
