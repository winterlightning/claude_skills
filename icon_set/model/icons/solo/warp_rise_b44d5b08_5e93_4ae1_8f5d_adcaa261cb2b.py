"""Warp rise (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b44d5b08-5e93-4ae1-8f5d-adcaa261cb2b'
SOURCE_PATH = 'icons-json/design/warp rise_b44d5b08-5e93-4ae1-8f5d-adcaa261cb2b.json'
AUTHOR = 'json_to_solo'

class WarpRise(Solo48):
    icon_id = 'warp-rise'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'rise', 'design')

    def build(self):
        self.add_line('e0', (22, 28), (28, 22))
        self.add_line('e1', (6, 33), (6, 42))
        self.add_line('e2', (24, 36), (31, 30))
        self.add_line('e3', (42, 25), (42, 17))
        self.add_line('e4', (6, 33), (6, 22))
        self.add_line('e5', (21, 17), (26, 12))
        self.add_line('e6', (42, 6), (42, 17))
        self.add_arc('e7', (6, 33), (22, 28), radius_x=17, sweep=False)
        self.add_arc('e8', (28, 22), (42, 17), radius_x=18)
        self.add_line('e9-1', (6, 42), (13, 42))
        self.add_arc('e9-2', (13, 42), (19, 40), radius_x=22, sweep=False)
        self.add_arc('e9-3', (19, 40), (24, 36), radius_x=20, sweep=False)
        self.add_arc('e10', (31, 30), (42, 25), radius_x=15)
        self.add_arc('e11', (6, 22), (21, 17), radius_x=17, sweep=False)
        self.add_arc('e12-1', (26, 12), (39, 6), radius_x=19)
        self.add_line('e12-2', (39, 6), (42, 6))
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4', 'e11', 'e5', 'e12-1', 'e12-2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
