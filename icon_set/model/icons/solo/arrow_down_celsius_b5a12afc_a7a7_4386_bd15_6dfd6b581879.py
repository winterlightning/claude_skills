"""Arrow down celsius (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5a12afc-a7a7-4386-bd15-6dfd6b581879'
SOURCE_PATH = 'icons-json/state/arrow down celsius_b5a12afc-a7a7-4386-bd15-6dfd6b581879.json'
AUTHOR = 'json_to_solo'

class ArrowDownCelsius(Solo48):
    icon_id = 'arrow-down-celsius'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'down', 'celsius', 'state')

    def build(self):
        self.add_line('e0', (8, 31), (24, 44))
        self.add_line('e1', (24, 4), (24, 44))
        self.add_line('e2', (39, 31), (24, 44))
        self.add_line('e3', (24, 44), (40, 44))
        self.add_line('e4', (24, 44), (8, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
