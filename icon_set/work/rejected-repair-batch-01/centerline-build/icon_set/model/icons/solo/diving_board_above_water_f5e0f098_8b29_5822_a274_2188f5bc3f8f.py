'A narrow diving board projects horizontally right from a tall rounded support at the left. Two parallel rows of waves extend beneath the board and around its supporting column.\n\nConstruction: Tall support and projecting diving board above a single row of water waves. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5e0f098-8b29-5822-a274-2188f5bc3f8f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/swimming pool board_f5e0f098-8b29-5822-a274-2188f5bc3f8f.svg'
AUTHOR = 'gpt-6'

class DivingBoardAboveWater(Solo48):
    icon_id = 'diving-board-above-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('diving', 'board', 'pool', 'water', 'swimming', 'sport')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('support-1', (8, 27), (8, 8))
        self.add_line('support-2', (8, 8), (20, 8))
        self.add_line('support-3-joint-1', (20, 8), (20, 12))
        self.add_line('support-3-joint-2', (20, 12), (20, 20))
        self.add_line('support-3-joint-3', (20, 20), (20, 27))
        self.add_line('board-1', (20, 12), (44, 12))
        self.add_line('board-2', (44, 12), (44, 20))
        self.add_line('board-3', (44, 20), (20, 20))
        self.add_arc('water-0', (4, 38), (14, 38), radius_x=5, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-1', (14, 38), (24, 38), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('water-2', (24, 38), (34, 38), radius_x=5, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-3', (34, 38), (44, 38), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('support', 'support-1', 'support-2', 'support-3-joint-1', 'support-3-joint-2', 'support-3-joint-3', closed=False)
        self.add_contour('board', 'board-1', 'board-2', 'board-3', closed=False)
        self.add_contour('water', 'water-0', 'water-1', 'water-2', 'water-3', closed=False)
        self.relate('connect', 'board', 'support')
