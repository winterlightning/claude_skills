"""Rocky mountain (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84a801ec-9a72-520e-9d5e-e141e4bfa565'
SOURCE_PATH = 'icons-json/outdoors/rocky mountain_84a801ec-9a72-520e-9d5e-e141e4bfa565.json'
AUTHOR = 'json_to_solo'

class RockyMountainOutdoors(Solo48):
    icon_id = 'rocky-mountain-outdoors'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('rocky', 'mountain', 'outdoors')

    def build(self):
        self.add_line('e0', (24, 30), (17, 18))
        self.add_line('e1', (15, 18), (4, 37))
        self.add_line('e2', (6, 40), (40, 40))
        self.add_line('e3', (43, 35), (29, 10))
        self.add_line('e4', (29, 10), (27, 8))
        self.add_line('e5', (27, 8), (19, 21))
        self.add_line('e6', (17, 18), (15, 18))
        self.add_arc('e7-1', (4, 37), (4, 39), radius_x=15)
        self.add_line('e7-2', (4, 39), (6, 40))
        self.add_line('e8-1', (40, 40), (42, 40))
        self.add_line('e8-2', (42, 40), (44, 37))
        self.add_line('e8-3', (44, 37), (43, 35))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2', 'e8-3', 'e3', 'e4', 'e5')
