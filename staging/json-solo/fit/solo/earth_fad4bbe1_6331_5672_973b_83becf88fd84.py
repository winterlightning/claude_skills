"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fad4bbe1-6331-5672-973b-83becf88fd84'
SOURCE_PATH = 'icons-json/maps/earth_fad4bbe1-6331-5672-973b-83becf88fd84.json'
AUTHOR = 'json_to_solo'

class Earth(Solo48):
    icon_id = 'earth'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_line('e0', (16, 34), (15, 30))
        self.add_line('e1', (9, 24), (4, 24))
        self.add_line('e2', (37, 27), (34, 30))
        self.add_line('e3', (27, 27), (27, 23))
        self.add_line('e4', (22, 9), (24, 4))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e6', (24, 44), (16, 34), radius_x=15)
        self.add_arc('e7', (15, 30), (9, 24), radius_x=7, sweep=False)
        self.add_arc('e8', (44, 24), (37, 27), radius_x=9, sweep=False)
        self.add_arc('e9-1', (34, 30), (29, 32), radius_x=4)
        self.add_arc('e9-2', (29, 32), (27, 27), radius_x=5)
        self.add_arc('e10-1', (27, 23), (25, 20), radius_x=4, sweep=False)
        self.add_line('e10-2', (25, 20), (21, 17))
        self.add_arc('e10-3', (21, 17), (22, 9), radius_x=12)
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e8', 'e2', 'e9-1', 'e9-2', 'e3', 'e10-1', 'e10-2', 'e10-3', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c1', 'e5')
