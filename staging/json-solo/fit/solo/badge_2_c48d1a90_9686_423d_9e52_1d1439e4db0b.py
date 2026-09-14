"""Badge 2 (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c48d1a90-9686-423d-9e52-1d1439e4db0b'
SOURCE_PATH = 'icons-json/other/badge 2_c48d1a90-9686-423d-9e52-1d1439e4db0b.json'
AUTHOR = 'json_to_solo'

class Badge2Other(Solo48):
    icon_id = 'badge-2-other'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('badge', 'other')

    def build(self):
        self.add_arc('sym-e0', (38, 30), (39, 29), radius_x=9)
        self.add_arc('sym-e1', (39, 29), (42, 24), radius_x=7, sweep=False)
        self.add_arc('sym-e4', (42, 24), (39, 19), radius_x=7, sweep=False)
        self.add_line('sym-e5', (39, 19), (38, 18))
        self.add_arc('sym-e6', (38, 18), (30, 10), radius_x=6, sweep=False)
        self.add_arc('sym-e7', (30, 10), (24, 6), radius_x=7, sweep=False)
        self.add_arc('sym-e8', (24, 6), (18, 10), radius_x=7, sweep=False)
        self.add_arc('sym-e9', (18, 10), (10, 18), radius_x=6, sweep=False)
        self.add_line('sym-e10', (10, 18), (9, 19))
        self.add_arc('sym-e11', (9, 19), (6, 24), radius_x=7, sweep=False)
        self.add_arc('sym-e14', (6, 24), (9, 29), radius_x=7, sweep=False)
        self.add_line('sym-e15', (9, 29), (10, 30))
        self.add_arc('sym-e16', (10, 30), (18, 38), radius_x=6, sweep=False)
        self.add_arc('sym-e17', (18, 38), (24, 42), radius_x=7, sweep=False)
        self.add_arc('sym-e18', (24, 42), (30, 38), radius_x=7, sweep=False)
        self.add_arc('sym-e19', (30, 38), (38, 30), radius_x=6, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
