"""Building (building), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '929733e7-35b6-4e6e-bcee-05768cc7b7d3'
SOURCE_PATH = 'icons-json/building/building_929733e7-35b6-4e6e-bcee-05768cc7b7d3.json'
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
        self.add_line('e0', (8, 44), (40, 44))
        self.add_line('e1', (40, 44), (40, 16))
        self.add_line('e2', (40, 16), (24, 16))
        self.add_line('e3', (24, 16), (24, 44))
        self.add_line('e4', (30, 16), (30, 4))
        self.add_line('e5', (30, 4), (13, 4))
        self.add_line('e6', (13, 4), (13, 44))
        self.add_line('e7', (31, 24), (33, 24))
        self.add_bezier('e8', (14, 44), ((13.436, 44), (12.564, 44), (12, 44)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
