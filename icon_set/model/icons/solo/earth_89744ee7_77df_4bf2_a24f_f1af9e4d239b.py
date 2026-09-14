"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89744ee7-77df-4bf2-a24f-f1af9e4d239b'
SOURCE_PATH = 'icons-json/maps/earth_89744ee7-77df-4bf2-a24f-f1af9e4d239b.json'
AUTHOR = 'json_to_solo'

class Earth89744ee7(Solo48):
    icon_id = 'earth-89744ee7'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_line('e0', (15, 34), (14, 29))
        self.add_line('e1', (27, 23), (27, 27))
        self.add_line('e2', (34, 30), (36, 27))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e4', (24, 44), (15, 34), radius_x=17)
        self.add_arc('e5', (14, 29), (4, 24), radius_x=8, sweep=False)
        self.add_arc('e6-1', (24, 4), (20, 16), radius_x=29, sweep=False)
        self.add_line('e6-2', (20, 16), (26, 20))
        self.add_line('e6-3', (26, 20), (27, 23))
        self.add_arc('e7-1', (27, 27), (29, 32), radius_x=5, sweep=False)
        self.add_arc('e7-2', (29, 32), (34, 30), radius_x=4, sweep=False)
        self.add_arc('e8', (36, 27), (44, 24), radius_x=9)
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e1', 'e7-1', 'e7-2', 'e2', 'e8')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c1', 'e3')
