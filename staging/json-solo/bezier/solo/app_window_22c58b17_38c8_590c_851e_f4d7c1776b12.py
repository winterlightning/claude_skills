"""App window (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22c58b17-38c8-590c-851e-f4d7c1776b12'
SOURCE_PATH = 'icons-json/apps/app window_22c58b17-38c8-590c-851e-f4d7c1776b12.json'
AUTHOR = 'json_to_solo'

class AppWindow22c58b17(Solo48):
    icon_id = 'app-window-22c58b17'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('app', 'window', 'apps')

    def build(self):
        self.add_line('e0', (42, 16), (6, 16))
        self.add_line('e1', (9, 42), (39, 42))
        self.add_line('e2', (42, 36), (42, 10))
        self.add_line('e3', (37, 6), (10, 6))
        self.add_line('e4', (6, 11), (6, 38))
        self.add_bezier('e5', (11, 11), ((11.27, 11), (11.73, 11), (12, 11)))
        self.add_bezier('e6', (21, 11), ((21.27, 11), (21.73, 11), (22, 11)))
        self.add_bezier('e7', (16, 11), ((16.27, 11), (16.73, 11), (17, 11)))
        self.add_bezier('e8', (6, 38), ((6, 38.082), (6, 38.073), (6, 38.155)), ((6, 39.635), (7.372, 42), (9, 42)))
        self.add_bezier('e9', (39, 42), ((39.131, 42), (38.981, 41.992), (39.112, 41.992)), ((40.593, 41.992), (41.984, 40.388), (41.984, 38.932)), ((41.984, 38.793), (42, 38.654), (42, 38.506)), ((42, 37.762), (42, 36.745), (42, 36)))
        self.add_bezier('e10', (42, 10), ((42, 9.926), (41.992, 9.952), (41.992, 9.878)), ((41.992, 7.579), (39.995, 6.016), (37.827, 6.016)), ((37.582, 6.016), (37.245, 6), (37, 6)))
        self.add_bezier('e11', (10, 6), ((9.869, 6), (9.829, 6.008), (9.698, 6.008)), ((8.168, 6.008), (6.008, 7.972), (6.008, 9.543)), ((6.008, 9.608), (6, 9.674), (6, 9.739)), ((6, 9.805), (6, 9.87), (6.008, 9.935)), ((6.008, 10.066), (6.008, 10.197), (6.008, 10.328)), ((6.008, 10.394), (6, 10.459), (6, 10.525)), ((6, 10.655), (6, 10.869), (6, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c4')
