"""House entrance (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8ff6223-9707-5e5b-9f2e-83b33b38b733'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house entrance_a8ff6223-9707-5e5b-9f2e-83b33b38b733.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class HouseEntrance(Solo48):
    icon_id = 'house-entrance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'entrance', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('sym-e1', (4, 40), (18, 40))
        self.add_line('sym-e4', (18, 40), (18, 31))
        self.add_arc('sym-e5', (18, 31), (24, 25), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e6', (24, 25), (30, 31), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e7', (30, 31), (30, 40))
        self.add_line('sym-e10', (30, 40), (44, 40))
        self.add_line('sym-e12', (44, 40), (44, 22))
        self.add_line('sym-e13', (44, 22), (27, 10))
        self.add_line('sym-e14', (27, 10), (24, 8))
        self.add_arc('sym-e15', (24, 8), (21, 10), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e16', (21, 10), (4, 22))
        self.add_line('sym-e17', (4, 22), (4, 40))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
