"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a9265b-3cf4-420c-8a2b-da7cd9955c06'
SOURCE_PATH = 'icons-json/protection/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.json'
AUTHOR = 'json_to_solo'

class Helmet(Solo48):
    icon_id = 'helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_line('sym-e0', (44, 40), (40, 40))
        self.add_line('sym-e1', (40, 40), (8, 40))
        self.add_line('sym-e2', (8, 40), (4, 40))
        self.add_line('sym-e3', (24, 8), (24, 15))
        self.add_line('sym-e4', (24, 15), (24, 29))
        self.add_arc('sym-e5', (40, 40), (38, 26), radius_x=38, sweep=False)
        self.add_arc('sym-e6', (38, 26), (24, 15), radius_x=16, sweep=False)
        self.add_arc('sym-e7', (24, 15), (10, 26), radius_x=16, sweep=False)
        self.add_arc('sym-e8', (10, 26), (8, 40), radius_x=39, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
