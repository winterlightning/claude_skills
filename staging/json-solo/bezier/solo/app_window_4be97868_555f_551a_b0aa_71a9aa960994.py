"""App window (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e3', (6, 39), ((6, 40.285), (7.666, 42), (9, 42)))
        self.add_bezier('sym-e4', (9, 42), ((9.074, 42), (8.926, 41.992), (9, 42)))
        self.add_line('sym-e5', (9, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (24, 16))
        self.add_line('sym-e7', (24, 42), (39, 42))
        self.add_bezier('sym-e8', (39, 42), ((39.074, 41.992), (38.926, 42), (39, 42)))
        self.add_bezier('sym-e9', (39, 42), ((40.334, 42), (42, 40.285), (42, 39)))
        self.add_line('sym-e10', (42, 39), (42, 16))
        self.add_line('sym-e11', (42, 16), (42, 10))
        self.add_bezier('sym-e12', (42, 10), ((42, 9.853), (42, 10.147), (42, 10)))
        self.add_bezier('sym-e13', (42, 10), ((42, 8.429), (40.743, 6), (39, 6)))
        self.add_bezier('sym-e14', (39, 6), ((38.935, 6), (39.065, 6), (39, 6)))
        self.add_line('sym-e15', (39, 6), (24, 6))
        self.add_line('sym-e16', (24, 6), (9, 6))
        self.add_bezier('sym-e17', (9, 6), ((8.935, 6), (9.065, 6), (9, 6)))
        self.add_bezier('sym-e18', (9, 6), ((7.257, 6), (6, 8.429), (6, 10)))
        self.add_bezier('sym-e19', (6, 10), ((6, 10.147), (6, 9.853), (6, 10)))
        self.add_line('sym-e20', (6, 10), (6, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
