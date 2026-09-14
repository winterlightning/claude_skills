"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e1b4154-d8c8-4476-9bd1-f79afb9ddf9e'
SOURCE_PATH = 'icons-json/interface-essential/house_7e1b4154-d8c8-4476-9bd1-f79afb9ddf9e.json'
AUTHOR = 'json_to_solo'

class House(Solo48):
    icon_id = 'house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 25), (10, 21))
        self.add_line('e1', (42, 24), (39, 21))
        self.add_line('e2', (20, 34), (20, 42))
        self.add_line('e3', (20, 42), (13, 42))
        self.add_line('e4', (10, 38), (10, 21))
        self.add_line('e5', (10, 21), (24, 6))
        self.add_line('e6', (24, 6), (39, 21))
        self.add_line('e7', (39, 21), (39, 39))
        self.add_line('e8', (37, 42), (29, 42))
        self.add_line('e9', (29, 42), (29, 33))
        self.add_bezier('e10', (29, 33), ((29, 31.454), (28.132, 29.907), (26.536, 29.482)), ((25.841, 29.294), (24.974, 29.384), (24.254, 29.367)), ((23.329, 29.351), (22.298, 29.269), (21.455, 29.744)), ((19.983, 30.57), (20, 32.511), (20, 34)))
        self.add_bezier('e11', (13, 42), ((12.836, 42), (13.045, 42), (12.881, 42)), ((11.637, 42), (10.631, 41.1), (10.222, 39.979)), ((10.001, 39.39), (10, 38.605), (10, 38)))
        self.add_bezier('e12', (39, 39), ((39, 40.105), (38.351, 40.961), (37.557, 41.763)), ((37.418, 41.91), (37.155, 41.869), (37, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e10', 'e2', 'e3', 'e11', 'e4', 'e5', 'e6', 'e7', 'e12', 'e8', 'e9', closed=True)
        self.relate('connect', 'c0', 'c2')
