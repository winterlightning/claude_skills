"""Move right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a1ed44e-1143-59a7-813e-101fa7a6d148'
SOURCE_PATH = 'icons-json/interface-essential/move right_9a1ed44e-1143-59a7-813e-101fa7a6d148.json'
AUTHOR = 'gpt-6'

class MoveRight(Solo48):
    icon_id = 'move-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'right', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (44, 24), (24, 24))
        self.add_line('sym-e1', (37, 16), (44, 24))
        self.add_line('sym-e2', (44, 24), (37, 32))
        self.add_line('sym-e3', (7, 8), (13, 8))
        self.add_arc('sym-e5', (13, 8), (16, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e6', (16, 11), (16, 37))
        self.add_arc('sym-e8', (16, 37), (13, 40), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e9', (13, 40), (7, 40))
        self.add_arc('sym-e11', (7, 40), (4, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e12', (4, 37), (4, 11))
        self.add_arc('sym-e14', (4, 11), (7, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', closed=False)
        self.add_contour('sym-c2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
