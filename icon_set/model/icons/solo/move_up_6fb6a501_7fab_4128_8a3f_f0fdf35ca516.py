"""Move up (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fb6a501-7fab-4128-8a3f-f0fdf35ca516'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move up_6fb6a501-7fab-4128-8a3f-f0fdf35ca516.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MoveUp(Solo48):
    icon_id = 'move-up'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'up', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (18, 10), (24, 4))
        self.add_line('e1', (24, 24), (24, 4))
        self.add_line('e2', (30, 10), (24, 4))
        self.add_line('e3', (8, 32), (8, 44))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_line('e5', (40, 44), (40, 32))
        self.add_line('e6', (40, 32), (8, 32))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
