"""Building (building), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68b98b76-99c3-4bca-a93b-dc7b4a54ff1a'
SOURCE_PATH = 'icons-json/building/building_68b98b76-99c3-4bca-a93b-dc7b4a54ff1a.json'
AUTHOR = 'json_to_solo'

class Building68b98b76(Solo48):
    icon_id = 'building-68b98b76'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building',)

    def build(self):
        self.add_line('e0', (24, 26), (20, 22))
        self.add_line('e1', (20, 22), (8, 22))
        self.add_line('e2', (24, 44), (24, 13))
        self.add_line('e3', (24, 13), (40, 4))
        self.add_line('e4', (40, 4), (40, 44))
        self.add_line('e5', (40, 44), (8, 44))
        self.add_line('e6', (8, 44), (8, 22))
        self.add_line('e7', (27, 11), (27, 5))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.add_contour('c3', 'e7')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c3', 'c2')
