"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c71b55db-b3c3-429a-ae0f-378e045b24c3'
SOURCE_PATH = 'pictographic-primitives/maps/earth_c71b55db-b3c3-429a-ae0f-378e045b24c3.svg'
AUTHOR = 'gpt-6'

class EarthC71b55db(Solo48):
    icon_id = 'earth-c71b55db'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    categories = ('maps', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (24, 4), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (24, 4), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (44, 24), (24, 44), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sym-e3', (24, 44), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('sym-e4', (42, 31), (6, 31))
        self.add_line('sym-e5', (24, 44), (24, 4))
        self.add_line('sym-e7', (42, 18), (6, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c1', 'sym-e4', closed=False)
        self.add_contour('sym-c2', 'sym-e5', closed=False)
        self.add_contour('sym-c3', 'sym-e7', closed=False)
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
