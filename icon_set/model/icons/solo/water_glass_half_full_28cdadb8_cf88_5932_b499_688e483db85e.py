"""Water glass half full (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '28cdadb8-cf88-5932-b499-688e483db85e'
SOURCE_PATH = 'icons-json/drinks/water glass half full_28cdadb8-cf88-5932-b499-688e483db85e.json'
AUTHOR = 'gpt-6'

class WaterGlassHalfFull(Solo48):
    icon_id = 'water-glass-half-full'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('water', 'glass', 'half', 'full', 'drinks')

    def build(self):
        self.add_line('sym-e0', (38, 18), (10, 18))
        self.add_arc('sym-e1', (36, 39), (33, 44), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e2', (33, 44), (16, 44))
        self.add_arc('sym-e5', (16, 44), (15, 44), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (15, 44), (12, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e7', (12, 39), (8, 4))
        self.add_line('sym-e8', (8, 4), (40, 4))
        self.add_line('sym-e10', (40, 4), (36, 39))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
