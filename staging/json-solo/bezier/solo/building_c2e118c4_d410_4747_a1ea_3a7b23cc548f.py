"""Building (building), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2e118c4-d410-4747-a1ea-3a7b23cc548f'
SOURCE_PATH = 'icons-json/building/building_c2e118c4-d410-4747-a1ea-3a7b23cc548f.json'
AUTHOR = 'json_to_solo'

class Building(Solo48):
    icon_id = 'building'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building',)

    def build(self):
        self.add_line('e0', (23, 19), (8, 19))
        self.add_line('e1', (8, 19), (8, 44))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_line('e3', (40, 44), (40, 16))
        self.add_line('e4', (40, 16), (35, 12))
        self.add_line('e5', (35, 12), (23, 4))
        self.add_line('e6', (23, 4), (23, 44))
        self.add_line('e7', (13, 29), (8, 29))
        self.add_line('e8', (37, 5), (37, 13))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e8')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
