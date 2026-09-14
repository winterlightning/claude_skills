"""Canoe paddles (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '481229e1-4318-5a89-838e-674d0da6757e'
SOURCE_PATH = 'icons-json/outdoors/canoe paddles_481229e1-4318-5a89-838e-674d0da6757e.json'
AUTHOR = 'json_to_solo'

class CanoePaddles481229e1(Solo48):
    icon_id = 'canoe-paddles-481229e1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddles', 'outdoors')

    def build(self):
        self.add_bezier('sym-e0', (31, 19), ((32.44, 19.049), (33.838, 19.162), (35, 18)))
        self.add_line('sym-e1', (35, 18), (40, 13))
        self.add_bezier('sym-e2', (40, 13), ((40.655, 12.345), (42, 11.998), (42, 11)))
        self.add_bezier('sym-e3', (42, 11), ((42, 10.943), (41.992, 10.057), (42, 10)))
        self.add_bezier('sym-e4', (42, 10), ((42, 9.648), (42, 9.286), (42, 9)))
        self.add_bezier('sym-e5', (42, 9), ((41.64, 8.485), (40.434, 8.45), (40, 8)))
        self.add_bezier('sym-e6', (40, 8), ((39.386, 7.362), (39.047, 6), (38, 6)))
        self.add_bezier('sym-e7', (38, 6), ((37.264, 6), (35.507, 7.493), (35, 8)))
        self.add_line('sym-e8', (35, 8), (31, 13))
        self.add_bezier('sym-e9', (31, 13), ((30.141, 13.859), (29.705, 14.83), (30, 16)))
        self.add_line('sym-e10', (30, 16), (31, 19))
        self.add_line('sym-e11', (31, 19), (24, 26))
        self.add_line('sym-e12', (24, 26), (38, 42))
        self.add_bezier('sym-e13', (17, 19), ((15.56, 19.049), (14.162, 19.162), (13, 18)))
        self.add_line('sym-e14', (13, 18), (8, 13))
        self.add_bezier('sym-e15', (8, 13), ((7.345, 12.345), (6, 11.998), (6, 11)))
        self.add_bezier('sym-e16', (6, 11), ((6, 10.943), (6.008, 10.057), (6, 10)))
        self.add_bezier('sym-e17', (6, 10), ((6, 9.648), (6, 9.286), (6, 9)))
        self.add_bezier('sym-e18', (6, 9), ((6.36, 8.485), (7.566, 8.45), (8, 8)))
        self.add_bezier('sym-e19', (8, 8), ((8.614, 7.362), (8.953, 6), (10, 6)))
        self.add_bezier('sym-e20', (10, 6), ((10.736, 6), (12.493, 7.493), (13, 8)))
        self.add_line('sym-e21', (13, 8), (17, 13))
        self.add_bezier('sym-e22', (17, 13), ((17.859, 13.859), (18.295, 14.83), (18, 16)))
        self.add_line('sym-e23', (18, 16), (17, 19))
        self.add_line('sym-e24', (17, 19), (24, 26))
        self.add_line('sym-e25', (24, 26), (10, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c1')
