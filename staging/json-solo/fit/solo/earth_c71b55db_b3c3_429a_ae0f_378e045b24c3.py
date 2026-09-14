"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c71b55db-b3c3-429a-ae0f-378e045b24c3'
SOURCE_PATH = 'icons-json/maps/earth_c71b55db-b3c3-429a-ae0f-378e045b24c3.json'
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
        self.add_arc('sym-e0', (4, 24), (24, 4), radius_x=20)
        self.add_arc('sym-e1', (24, 4), (44, 24), radius_x=20)
        self.add_arc('sym-e2', (44, 24), (24, 44), radius_x=20)
        self.add_arc('sym-e3', (24, 44), (4, 24), radius_x=20)
        self.add_line('sym-e4', (42, 31), (6, 31))
        self.add_line('sym-e5', (24, 44), (24, 18))
        self.add_line('sym-e6', (24, 18), (24, 4))
        self.add_line('sym-e7', (42, 18), (24, 18))
        self.add_line('sym-e8', (24, 18), (6, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c1', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
