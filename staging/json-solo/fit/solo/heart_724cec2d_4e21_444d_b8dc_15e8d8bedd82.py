"""Heart (romance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '724cec2d-4e21-444d-b8dc-15e8d8bedd82'
SOURCE_PATH = 'icons-json/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.json'
AUTHOR = 'json_to_solo'

class Heart724cec2d(Solo48):
    icon_id = 'heart-724cec2d'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('heart', 'romance')

    def build(self):
        self.add_line('e0', (24, 40), (8, 25))
        self.add_line('e1', (40, 25), (24, 40))
        self.add_arc('e2-1', (8, 25), (4, 18), radius_x=9)
        self.add_arc('e2-2', (4, 18), (14, 8), radius_x=10)
        self.add_arc('e2-3', (14, 8), (24, 12), radius_x=17)
        self.add_arc('e2-4', (24, 12), (34, 8), radius_x=16)
        self.add_arc('e2-5', (34, 8), (44, 18), radius_x=10)
        self.add_arc('e2-6', (44, 18), (40, 25), radius_x=9)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e1', closed=True)
