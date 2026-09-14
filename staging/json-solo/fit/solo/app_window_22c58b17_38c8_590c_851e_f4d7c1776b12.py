"""App window (apps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e5', (11, 11), (12, 11), radius_x=11, sweep=False)
        self.add_arc('e6', (21, 11), (22, 11), radius_x=26, sweep=False)
        self.add_arc('e7', (16, 11), (17, 11), radius_x=18)
        self.add_arc('e8', (6, 38), (9, 42), radius_x=5, sweep=False)
        self.add_arc('e9-1', (39, 42), (41, 41), radius_x=3, sweep=False)
        self.add_line('e9-2', (41, 41), (42, 38))
        self.add_arc('e9-3', (42, 38), (42, 36), radius_x=38)
        self.add_line('e10-1', (42, 10), (41, 7))
        self.add_line('e10-2', (41, 7), (37, 6))
        self.add_arc('e11-1', (10, 6), (6, 10), radius_x=4, sweep=False)
        self.add_line('e11-2', (6, 10), (6, 11))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e2', 'e10-1', 'e10-2', 'e3', 'e11-1', 'e11-2', 'e4', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c4')
