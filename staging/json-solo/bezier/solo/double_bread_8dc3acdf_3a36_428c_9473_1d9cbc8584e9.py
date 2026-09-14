"""Double bread (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dc3acdf-3a36-428c-9473-1d9cbc8584e9'
SOURCE_PATH = 'icons-json/symbol/double bread_8dc3acdf-3a36-428c-9473-1d9cbc8584e9.json'
AUTHOR = 'json_to_solo'

class DoubleBreadSymbol(Solo48):
    icon_id = 'double-bread-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('double', 'bread', 'symbol')

    def build(self):
        self.add_line('e0', (27, 40), (26, 22))
        self.add_line('e1', (7, 22), (6, 40))
        self.add_line('e2', (6, 40), (42, 40))
        self.add_line('e3', (42, 40), (41, 22))
        self.add_line('e4', (30, 8), (24, 10))
        self.add_bezier('e5', (26, 22), ((26.855, 21.39), (27.645, 20.7), (28.245, 19.75)), ((29.991, 16.96), (28.618, 14.25), (26.782, 12.12)), ((26.409, 11.7), (26.036, 11.11), (25.609, 10.78)), ((25.164, 10.43), (24.5, 10.24), (24, 10)), ((21.791, 8.94), (19.418, 8.01), (16.973, 8.01)), ((16.755, 8.01), (16.545, 8), (16.336, 8)), ((16.045, 8), (15.764, 8.02), (15.482, 8.02)), ((11.618, 8.02), (7.2, 9.85), (4.982, 13.46)), ((4.473, 14.28), (4.018, 15.43), (4.018, 16.44)), ((4.018, 16.657), (4, 16.883), (4, 17.1)), ((4, 17.103), (4, 17.107), (4, 17.11)), ((4, 17.34), (4.018, 17.58), (4.018, 17.81)), ((4.018, 19.81), (5.636, 20.98), (7, 22)))
        self.add_bezier('e6', (41, 22), ((42.345, 20.88), (43.982, 19.78), (43.982, 17.72)), ((43.982, 17.5), (44, 17.28), (44, 17.07)), ((44, 17.068), (44, 17.065), (44, 17.063)), ((44, 16.916), (43.991, 16.778), (43.991, 16.63)), ((43.991, 16.12), (43.809, 15.51), (43.673, 15.02)), ((42.573, 10.87), (38.3, 8.92), (34.782, 8.28)), ((34.245, 8.18), (33.655, 8.01), (33.109, 8.01)), ((33.045, 8.01), (32.973, 8), (32.9, 8)), ((32.055, 8), (30.845, 8), (30, 8)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e3', 'e6', 'e4')
