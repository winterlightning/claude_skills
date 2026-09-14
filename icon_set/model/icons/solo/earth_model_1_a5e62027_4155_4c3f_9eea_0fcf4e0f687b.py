"""Earth model 1 (maps), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5e62027-4155-4c3f-9eea-0fcf4e0f687b'
SOURCE_PATH = 'icons-json/maps/earth model 1_a5e62027-4155-4c3f-9eea-0fcf4e0f687b.json'
AUTHOR = 'json_to_solo'

class EarthModel1(Solo48):
    icon_id = 'earth-model-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'model', 'maps')

    def build(self):
        self.add_line('e0', (22, 40), (22, 36))
        self.add_line('e1', (31, 44), (13, 44))
        self.add_line('e2', (15, 40), (29, 40))
        self.add_arc('e3-top', (8, 19), (36, 19), radius_x=14, radius_y=13)
        self.add_arc('e3-bottom', (36, 19), (8, 19), radius_x=14, radius_y=13)
        self.add_arc('e4-1', (34, 4), (33, 5), radius_x=2, sweep=False)
        self.add_arc('e4-2', (33, 5), (39, 12), radius_x=20)
        self.add_line('e4-3', (39, 12), (40, 18))
        self.add_arc('e4-4', (40, 18), (22, 36), radius_x=18)
        self.add_line('e5-1', (8, 30), (17, 35))
        self.add_line('e5-2', (17, 35), (22, 36))
        self.add_arc('e6', (13, 44), (15, 40), radius_x=3)
        self.add_arc('e7', (29, 40), (31, 44), radius_x=3)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c1', 'e5-1', 'e5-2')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1', 'e6', 'e2', 'e7', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
