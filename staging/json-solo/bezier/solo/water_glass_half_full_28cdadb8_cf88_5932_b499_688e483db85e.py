"""Water glass half full (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28cdadb8-cf88-5932-b499-688e483db85e'
SOURCE_PATH = 'icons-json/drinks/water glass half full_28cdadb8-cf88-5932-b499-688e483db85e.json'
AUTHOR = 'json_to_solo'

class WaterGlassHalfFullDrinks(Solo48):
    icon_id = 'water-glass-half-full-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('water', 'glass', 'half', 'full', 'drinks')

    def build(self):
        self.add_line('sym-e0', (38, 18), (10, 18))
        self.add_bezier('sym-e1', (36, 39), ((35.79, 40.9), (34.95, 43.182), (33, 44)))
        self.add_bezier('sym-e2', (33, 44), ((32.78, 44), (32.22, 43.918), (32, 44)))
        self.add_line('sym-e3', (32, 44), (24, 44))
        self.add_line('sym-e4', (24, 44), (16, 44))
        self.add_bezier('sym-e5', (16, 44), ((15.78, 43.918), (15.22, 44), (15, 44)))
        self.add_bezier('sym-e6', (15, 44), ((13.05, 43.182), (12.21, 40.9), (12, 39)))
        self.add_line('sym-e7', (12, 39), (8, 4))
        self.add_line('sym-e8', (8, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (40, 4))
        self.add_line('sym-e10', (40, 4), (36, 39))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
