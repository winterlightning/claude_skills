"""Building 1 (building), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6adecf4-5959-4f91-a3a7-5bdffc5bac69'
SOURCE_PATH = 'icons-json/building/building 1_a6adecf4-5959-4f91-a3a7-5bdffc5bac69.json'
AUTHOR = 'json_to_solo'

class Building1Building(Solo48):
    icon_id = 'building-1-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building',)

    def build(self):
        self.add_line('e0', (15, 9), (40, 22))
        self.add_line('e1', (40, 22), (40, 44))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (27, 44), (27, 37))
        self.add_line('e4', (15, 44), (15, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
