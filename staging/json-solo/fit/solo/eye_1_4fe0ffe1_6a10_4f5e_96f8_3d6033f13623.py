"""Eye 1 (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fe0ffe1-6a10-4f5e-96f8-3d6033f13623'
SOURCE_PATH = 'icons-json/state/eye 1_4fe0ffe1-6a10-4f5e-96f8-3d6033f13623.json'
AUTHOR = 'json_to_solo'

class Eye14fe0ffe1(Solo48):
    icon_id = 'eye-1-4fe0ffe1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('eye', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_arc('sym-e2', (44, 24), (41, 30), radius_x=46)
        self.add_arc('sym-e3', (41, 30), (24, 40), radius_x=22)
        self.add_arc('sym-e5', (24, 40), (23, 40), radius_x=26, sweep=False)
        self.add_arc('sym-e6', (23, 40), (8, 30), radius_x=21)
        self.add_arc('sym-e7', (8, 30), (4, 24), radius_x=54)
        self.add_arc('sym-e8', (4, 24), (8, 18), radius_x=54)
        self.add_arc('sym-e9', (8, 18), (23, 8), radius_x=21)
        self.add_arc('sym-e10', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_arc('sym-e12', (24, 8), (41, 18), radius_x=22)
        self.add_arc('sym-e13', (41, 18), (44, 24), radius_x=46)
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', closed=True)
