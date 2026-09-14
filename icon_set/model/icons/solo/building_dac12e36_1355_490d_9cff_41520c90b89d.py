"""Building (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dac12e36-1355-490d-9cff-41520c90b89d'
SOURCE_PATH = 'icons-json/building/building_dac12e36-1355-490d-9cff-41520c90b89d.json'
AUTHOR = 'json_to_solo'

class BuildingDac12e36(Solo48):
    icon_id = 'building-dac12e36'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building',)

    def build(self):
        self.add_line('e0', (33, 19), (42, 23))
        self.add_line('e1', (42, 23), (42, 42))
        self.add_line('e2', (42, 42), (6, 42))
        self.add_line('e3', (33, 42), (33, 6))
        self.add_line('e4', (33, 6), (11, 6))
        self.add_line('e5', (11, 6), (11, 42))
        self.add_line('e6', (19, 17), (24, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
