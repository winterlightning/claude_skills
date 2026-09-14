"""Building (building), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '735a4c8f-9008-4cdc-be93-7882c6bfd595'
SOURCE_PATH = 'icons-json/building/building_735a4c8f-9008-4cdc-be93-7882c6bfd595.json'
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
        self.add_line('e0', (23, 13), (40, 4))
        self.add_line('e1', (40, 4), (40, 40))
        self.add_line('e2', (8, 42), (8, 29))
        self.add_line('e3', (8, 29), (15, 23))
        self.add_line('e4', (15, 23), (15, 9))
        self.add_line('e5', (15, 9), (29, 17))
        self.add_line('e6', (29, 17), (29, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
