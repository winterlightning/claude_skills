"""Three dots (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12eb4663-24d4-4740-956a-57124928664f'
SOURCE_PATH = 'icons-json/state/three dots_12eb4663-24d4-4740-956a-57124928664f.json'
AUTHOR = 'json_to_solo'

class ThreeDotsState(Solo48):
    icon_id = 'three-dots-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'dots', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_line('sym-e1', (8, 24), (8, 40))
        self.add_line('sym-e2', (8, 40), (8, 41))
        self.add_arc('sym-e3-1', (8, 41), (9, 43), radius_x=3, sweep=False)
        self.add_line('sym-e3-2', (9, 43), (12, 44))
        self.add_line('sym-e4', (12, 44), (36, 44))
        self.add_arc('sym-e5', (36, 44), (40, 43), radius_x=7)
        self.add_line('sym-e6', (40, 43), (40, 42))
        self.add_line('sym-e7', (40, 42), (40, 24))
        self.add_line('sym-e8', (40, 24), (40, 6))
        self.add_arc('sym-e9', (40, 6), (40, 5), radius_x=1)
        self.add_arc('sym-e10', (40, 5), (36, 4), radius_x=7)
        self.add_line('sym-e11', (36, 4), (12, 4))
        self.add_line('sym-e12-1', (12, 4), (9, 5))
        self.add_arc('sym-e12-2', (9, 5), (8, 7), radius_x=3, sweep=False)
        self.add_line('sym-e13', (8, 7), (8, 8))
        self.add_line('sym-e14', (8, 8), (8, 24))
        self.add_line('sym-e15', (24, 35), (24, 35))
        self.add_line('sym-e16', (24, 13), (24, 13))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e14', closed=True)
        self.add_contour('sym-c2', 'sym-e15')
        self.add_contour('sym-c3', 'sym-e16')
