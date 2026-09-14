"""Material tile (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4d78781-45cc-57cc-9c82-6d29cec0be1d'
SOURCE_PATH = 'icons-json/construction/material tile_f4d78781-45cc-57cc-9c82-6d29cec0be1d.json'
AUTHOR = 'json_to_solo'

class MaterialTileConstruction(Solo48):
    icon_id = 'material-tile-construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('material', 'tile', 'construction')

    def build(self):
        self.add_line('sym-e0', (42, 24), (6, 24))
        self.add_line('sym-e1', (6, 24), (6, 40))
        self.add_bezier('sym-e2', (6, 40), ((6, 41.587), (7.904, 42), (9, 42)))
        self.add_bezier('sym-e3', (9, 42), ((9.221, 42), (9.779, 42), (10, 42)))
        self.add_line('sym-e4', (10, 42), (24, 42))
        self.add_line('sym-e5', (24, 42), (24, 6))
        self.add_line('sym-e6', (24, 6), (38, 6))
        self.add_bezier('sym-e7', (38, 6), ((38.221, 6), (38.779, 6), (39, 6)))
        self.add_bezier('sym-e8', (39, 6), ((40.096, 6), (42, 6.413), (42, 8)))
        self.add_line('sym-e9', (42, 8), (42, 24))
        self.add_line('sym-e10', (42, 24), (42, 40))
        self.add_bezier('sym-e11', (42, 40), ((42, 41.587), (40.096, 42), (39, 42)))
        self.add_bezier('sym-e12', (39, 42), ((38.779, 42), (38.221, 42), (38, 42)))
        self.add_line('sym-e13', (38, 42), (24, 42))
        self.add_line('sym-e14', (6, 24), (6, 8))
        self.add_bezier('sym-e15', (6, 8), ((6, 6.413), (7.904, 6), (9, 6)))
        self.add_bezier('sym-e16', (9, 6), ((9.221, 6), (9.779, 6), (10, 6)))
        self.add_line('sym-e17', (10, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
