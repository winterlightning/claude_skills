"""Car dashboard e 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98f23329-d944-4453-ac48-9d771dfe4fae'
SOURCE_PATH = 'icons-json/symbol/car dashboard e 1_98f23329-d944-4453-ac48-9d771dfe4fae.json'
AUTHOR = 'json_to_solo'

class CarDashboardE1Symbol(Solo48):
    icon_id = 'car-dashboard-e-1-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('car', 'dashboard', 'e', 'symbol')

    def build(self):
        self.add_line('e0', (20, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (19, 27))
        self.add_line('e3', (8, 16), (18, 16))
        self.add_line('e4', (40, 18), (14, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c0')
