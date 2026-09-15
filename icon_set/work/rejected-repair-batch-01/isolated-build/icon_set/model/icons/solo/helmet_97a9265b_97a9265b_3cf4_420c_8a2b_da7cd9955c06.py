"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97a9265b-3cf4-420c-8a2b-da7cd9955c06'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.svg'
AUTHOR = 'gpt-6'

class Helmet97a9265b(Solo48):
    icon_id = 'helmet-97a9265b'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_line('sym-e0', (44, 40), (4, 40))
        self.add_line('sym-e3', (24, 8), (24, 29))
        self.add_arc('sym-e5', (40, 40), (38, 26), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (38, 26), (24, 15), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (24, 15), (10, 26), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('sym-e8', (10, 26), (8, 40), radius_x=39, radius_y=39, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e3', closed=False)
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
