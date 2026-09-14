"""Canoe paddles (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '481229e1-4318-5a89-838e-674d0da6757e'
SOURCE_PATH = 'icons-json/outdoors/canoe paddles_481229e1-4318-5a89-838e-674d0da6757e.json'
AUTHOR = 'json_to_solo'

class CanoePaddles(Solo48):
    icon_id = 'canoe-paddles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddles', 'outdoors')

    def build(self):
        self.add_arc('sym-e0', (31, 19), (35, 18), radius_x=6, sweep=False)
        self.add_line('sym-e1', (35, 18), (40, 13))
        self.add_arc('sym-e2', (40, 13), (42, 11), radius_x=4, sweep=False)
        self.add_arc('sym-e3', (42, 11), (42, 10), radius_x=1)
        self.add_line('sym-e4', (42, 10), (42, 9))
        self.add_line('sym-e5', (42, 9), (40, 8))
        self.add_arc('sym-e6', (40, 8), (38, 6), radius_x=4, sweep=False)
        self.add_line('sym-e7', (38, 6), (35, 8))
        self.add_line('sym-e8', (35, 8), (31, 13))
        self.add_arc('sym-e9', (31, 13), (30, 16), radius_x=3, sweep=False)
        self.add_line('sym-e10', (30, 16), (31, 19))
        self.add_line('sym-e11', (31, 19), (24, 26))
        self.add_line('sym-e12', (24, 26), (38, 42))
        self.add_arc('sym-e13', (17, 19), (13, 18), radius_x=6)
        self.add_line('sym-e14', (13, 18), (8, 13))
        self.add_arc('sym-e15', (8, 13), (6, 11), radius_x=4)
        self.add_line('sym-e16', (6, 11), (6, 10))
        self.add_line('sym-e17', (6, 10), (6, 9))
        self.add_line('sym-e18', (6, 9), (8, 8))
        self.add_arc('sym-e19', (8, 8), (10, 6), radius_x=4)
        self.add_line('sym-e20', (10, 6), (13, 8))
        self.add_line('sym-e21', (13, 8), (17, 13))
        self.add_arc('sym-e22', (17, 13), (18, 16), radius_x=3)
        self.add_line('sym-e23', (18, 16), (17, 19))
        self.add_line('sym-e24', (17, 19), (24, 26))
        self.add_line('sym-e25', (24, 26), (10, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c1')
