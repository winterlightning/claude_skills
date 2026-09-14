"""Trash (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '809378b8-e0d0-4cfb-9e28-6f64d31ac4f8'
SOURCE_PATH = 'icons-json/symbol/trash_809378b8-e0d0-4cfb-9e28-6f64d31ac4f8.json'
AUTHOR = 'json_to_solo'

class Trash(Solo48):
    icon_id = 'trash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'symbol')

    def build(self):
        self.add_line('sym-e0', (17, 13), (31, 13))
        self.add_bezier('sym-e1', (31, 13), ((30.995, 12.867), (31, 13.135), (31, 13)))
        self.add_bezier('sym-e2', (31, 13), ((31, 10.783), (32.028, 8.504), (30, 7)))
        self.add_bezier('sym-e3', (30, 7), ((29.575, 6.681), (28.556, 6), (28, 6)))
        self.add_bezier('sym-e4', (28, 6), ((27.959, 6), (28.041, 6.008), (28, 6)))
        self.add_line('sym-e5', (28, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (20, 6))
        self.add_bezier('sym-e7', (20, 6), ((19.959, 6.008), (20.041, 6), (20, 6)))
        self.add_bezier('sym-e8', (20, 6), ((19.444, 6), (18.425, 6.681), (18, 7)))
        self.add_bezier('sym-e9', (18, 7), ((15.972, 8.504), (17, 10.783), (17, 13)))
        self.add_bezier('sym-e10', (17, 13), ((17, 13.135), (17.005, 12.867), (17, 13)))
        self.add_line('sym-e11', (17, 13), (8, 13))
        self.add_line('sym-e12', (8, 13), (6, 13))
        self.add_line('sym-e13', (42, 13), (40, 13))
        self.add_line('sym-e14', (40, 13), (36, 40))
        self.add_bezier('sym-e15', (36, 40), ((35.583, 40.941), (35.015, 41.575), (34, 42)))
        self.add_bezier('sym-e16', (34, 42), ((33.812, 42), (34.18, 41.935), (34, 42)))
        self.add_line('sym-e17', (34, 42), (24, 42))
        self.add_line('sym-e18', (24, 42), (14, 42))
        self.add_bezier('sym-e19', (14, 42), ((13.82, 41.935), (14.188, 42), (14, 42)))
        self.add_bezier('sym-e20', (14, 42), ((12.985, 41.575), (12.417, 40.941), (12, 40)))
        self.add_line('sym-e21', (12, 40), (8, 13))
        self.add_line('sym-e22', (31, 13), (40, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c2', 'sym-e22')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
