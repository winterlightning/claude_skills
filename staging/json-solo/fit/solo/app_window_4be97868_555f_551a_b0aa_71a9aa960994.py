"""App window (apps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4be97868-555f-551a-b0aa-71a9aa960994'
SOURCE_PATH = 'icons-json/apps/app window_4be97868-555f-551a-b0aa-71a9aa960994.json'
AUTHOR = 'json_to_solo'

class AppWindow(Solo48):
    icon_id = 'app-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('app', 'window', 'apps')

    def build(self):
        self.add_line('sym-e0', (42, 16), (24, 16))
        self.add_line('sym-e1', (24, 16), (6, 16))
        self.add_line('sym-e2', (6, 16), (6, 39))
        self.add_arc('sym-e3', (6, 39), (9, 42), radius_x=4, sweep=False)
        self.add_line('sym-e5', (9, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (24, 16))
        self.add_line('sym-e7', (24, 42), (39, 42))
        self.add_arc('sym-e9', (39, 42), (42, 39), radius_x=4, sweep=False)
        self.add_line('sym-e10', (42, 39), (42, 16))
        self.add_line('sym-e11', (42, 16), (42, 10))
        self.add_line('sym-e13-1', (42, 10), (41, 7))
        self.add_arc('sym-e13-2', (41, 7), (39, 6), radius_x=3, sweep=False)
        self.add_line('sym-e15', (39, 6), (24, 6))
        self.add_line('sym-e16', (24, 6), (9, 6))
        self.add_arc('sym-e18-1', (9, 6), (7, 7), radius_x=3, sweep=False)
        self.add_line('sym-e18-2', (7, 7), (6, 10))
        self.add_line('sym-e20', (6, 10), (6, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c1', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13-1', 'sym-e13-2', 'sym-e15', 'sym-e16', 'sym-e18-1', 'sym-e18-2', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
