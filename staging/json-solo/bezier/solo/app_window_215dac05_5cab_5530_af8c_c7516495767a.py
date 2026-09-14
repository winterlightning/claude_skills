"""App window (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '215dac05-5cab-5530-af8c-c7516495767a'
SOURCE_PATH = 'icons-json/apps/app window_215dac05-5cab-5530-af8c-c7516495767a.json'
AUTHOR = 'json_to_solo'

class AppWindow215dac05(Solo48):
    icon_id = 'app-window-215dac05'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('app', 'window', 'apps')

    def build(self):
        self.add_line('sym-e0', (42, 16), (6, 16))
        self.add_line('sym-e1', (6, 16), (6, 39))
        self.add_bezier('sym-e2', (6, 39), ((6, 40.432), (7.486, 42), (9, 42)))
        self.add_bezier('sym-e3', (9, 42), ((9.123, 42), (8.877, 41.992), (9, 42)))
        self.add_line('sym-e4', (9, 42), (24, 42))
        self.add_line('sym-e5', (24, 42), (39, 42))
        self.add_bezier('sym-e6', (39, 42), ((39.123, 41.992), (38.877, 42), (39, 42)))
        self.add_bezier('sym-e7', (39, 42), ((40.514, 42), (42, 40.432), (42, 39)))
        self.add_line('sym-e8', (42, 39), (42, 16))
        self.add_line('sym-e9', (42, 16), (42, 9))
        self.add_bezier('sym-e10', (42, 9), ((42, 8.861), (42, 9.139), (42, 9)))
        self.add_bezier('sym-e11', (42, 9), ((42, 7.388), (40.571, 6), (39, 6)))
        self.add_bezier('sym-e12', (39, 6), ((38.918, 6), (39.082, 6), (39, 6)))
        self.add_line('sym-e13', (39, 6), (24, 6))
        self.add_line('sym-e14', (24, 6), (9, 6))
        self.add_bezier('sym-e15', (9, 6), ((8.918, 6), (9.082, 6), (9, 6)))
        self.add_bezier('sym-e16', (9, 6), ((7.429, 6), (6, 7.388), (6, 9)))
        self.add_bezier('sym-e17', (6, 9), ((6, 9.139), (6, 8.861), (6, 9)))
        self.add_line('sym-e18', (6, 9), (6, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
