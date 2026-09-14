"""Plane (travel), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9b25762-c771-4473-9538-0c3ff813a1dd'
SOURCE_PATH = 'icons-json/travel/plane_c9b25762-c771-4473-9538-0c3ff813a1dd.json'
AUTHOR = 'json_to_solo'

class PlaneTravel(Solo48):
    icon_id = 'plane-travel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (44, 8), (18, 37))
        self.add_line('e1', (7, 34), (4, 30))
        self.add_line('e2', (34, 19), (14, 8))
        self.add_arc('e3-1', (18, 37), (13, 40), radius_x=6)
        self.add_arc('e3-2', (13, 40), (7, 34), radius_x=11)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c1', 'e2')
        self.relate('connect', 'c1', 'c0')
