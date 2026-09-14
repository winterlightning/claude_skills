"""Drop bottle (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48eb833d-db76-44ba-9351-6d92a11f756c'
SOURCE_PATH = 'icons-json/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.json'
AUTHOR = 'json_to_solo'

class DropBottleSymbol(Solo48):
    icon_id = 'drop-bottle-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('drop', 'bottle', 'symbol')

    def build(self):
        self.add_line('sym-e0', (10, 20), (38, 20))
        self.add_line('sym-e1', (38, 20), (38, 17))
        self.add_bezier('sym-e2', (38, 17), ((37.488, 16.255), (36.992, 15.591), (36, 15)))
        self.add_bezier('sym-e3', (36, 15), ((34.528, 14.118), (33.024, 13.1), (32, 12)))
        self.add_bezier('sym-e4', (32, 12), ((29.744, 9.582), (32.672, 6.773), (28, 5)))
        self.add_bezier('sym-e5', (28, 5), ((27.024, 4.627), (25.184, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((23.827, 4), (24.16, 4.002), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((23.84, 4.002), (24.173, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((22.816, 4), (20.976, 4.627), (20, 5)))
        self.add_bezier('sym-e9', (20, 5), ((15.328, 6.773), (18.256, 9.582), (16, 12)))
        self.add_bezier('sym-e10', (16, 12), ((14.976, 13.1), (13.472, 14.118), (12, 15)))
        self.add_bezier('sym-e11', (12, 15), ((11.008, 15.591), (10.512, 16.255), (10, 17)))
        self.add_line('sym-e12', (10, 17), (10, 20))
        self.add_line('sym-e13', (10, 20), (10, 21))
        self.add_bezier('sym-e14', (10, 21), ((9.392, 21.491), (8, 22.336), (8, 23)))
        self.add_bezier('sym-e15', (8, 23), ((8, 23.027), (8.016, 22.973), (8, 23)))
        self.add_line('sym-e16', (8, 23), (8, 40))
        self.add_bezier('sym-e17', (8, 40), ((9.152, 42.064), (10.448, 43.3), (14, 44)))
        self.add_line('sym-e18', (14, 44), (24, 44))
        self.add_line('sym-e19', (24, 44), (34, 44))
        self.add_bezier('sym-e20', (34, 44), ((37.552, 43.3), (38.848, 42.064), (40, 40)))
        self.add_line('sym-e21', (40, 40), (40, 23))
        self.add_bezier('sym-e22', (40, 23), ((39.984, 22.973), (40, 23.027), (40, 23)))
        self.add_bezier('sym-e23', (40, 23), ((40, 22.336), (38.608, 21.491), (38, 21)))
        self.add_line('sym-e24', (38, 21), (38, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
