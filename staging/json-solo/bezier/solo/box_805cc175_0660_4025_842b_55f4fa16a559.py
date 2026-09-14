"""Box (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '805cc175-0660-4025-842b-55f4fa16a559'
SOURCE_PATH = 'icons-json/shipping/box_805cc175-0660-4025-842b-55f4fa16a559.json'
AUTHOR = 'json_to_solo'

class Box(Solo48):
    icon_id = 'box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping')

    def build(self):
        self.add_line('sym-e0', (24, 19), (24, 6))
        self.add_line('sym-e1', (24, 6), (39, 6))
        self.add_bezier('sym-e2', (39, 6), ((39.025, 6), (38.975, 6), (39, 6)))
        self.add_bezier('sym-e3', (39, 6), ((40.555, 6), (41.591, 7.74), (42, 9)))
        self.add_line('sym-e4', (42, 9), (42, 39))
        self.add_bezier('sym-e5', (42, 39), ((41.599, 40.285), (40.628, 42), (39, 42)))
        self.add_bezier('sym-e6', (39, 42), ((38.951, 42), (39.049, 42), (39, 42)))
        self.add_line('sym-e7', (39, 42), (24, 42))
        self.add_line('sym-e8', (24, 42), (9, 42))
        self.add_bezier('sym-e9', (9, 42), ((8.951, 42), (9.049, 42), (9, 42)))
        self.add_bezier('sym-e10', (9, 42), ((7.372, 42), (6.401, 40.285), (6, 39)))
        self.add_line('sym-e11', (6, 39), (6, 9))
        self.add_bezier('sym-e12', (6, 9), ((6.409, 7.74), (7.445, 6), (9, 6)))
        self.add_bezier('sym-e13', (9, 6), ((9.025, 6), (8.975, 6), (9, 6)))
        self.add_line('sym-e14', (9, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
