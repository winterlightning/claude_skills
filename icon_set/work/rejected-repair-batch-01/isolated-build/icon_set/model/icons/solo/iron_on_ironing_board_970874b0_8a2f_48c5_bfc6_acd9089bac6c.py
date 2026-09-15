'A long ironing board rests on crossed folding legs. A small iron stands upright at the left end of its narrow horizontal top, with its pointed upper profile visible.\n\nConstruction: Small iron resting on a long board supported by crossing legs. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '970874b0-8a2f-48c5-bfc6-acd9089bac6c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/laundry iron board_970874b0-8a2f-48c5-bfc6-acd9089bac6c.svg'
AUTHOR = 'gpt-6'

class IronOnIroningBoard(Solo48):
    icon_id = 'iron-on-ironing-board'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('iron', 'ironing', 'board', 'laundry', 'clothes', 'housework')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('iron-1', (4, 20), (4, 8))
        self.add_line('iron-2', (4, 8), (12, 8))
        self.add_line('iron-3', (12, 8), (18, 20))
        self.add_line('iron-4-joint-1', (18, 20), (12, 20))
        self.add_line('iron-4-joint-2', (12, 20), (4, 20))
        self.add_line('board-1-joint-1', (4, 20), (12, 20))
        self.add_line('board-1-joint-2', (12, 20), (18, 20))
        self.add_line('board-2-joint-1', (18, 20), (36, 20))
        self.add_line('board-2-joint-2', (36, 20), (44, 20))
        self.add_line('left-leg-1', (12, 20), (24, 30))
        self.add_line('left-leg-2', (24, 30), (36, 40))
        self.add_line('right-leg-1', (36, 20), (24, 30))
        self.add_line('right-leg-2', (24, 30), (12, 40))
        self.add_contour('iron', 'iron-1', 'iron-2', 'iron-3', 'iron-4-joint-1', 'iron-4-joint-2', closed=True)
        self.add_contour('board', 'board-1-joint-1', 'board-1-joint-2', 'board-2-joint-1', 'board-2-joint-2', closed=False)
        self.add_contour('left-leg', 'left-leg-1', 'left-leg-2', closed=False)
        self.add_contour('right-leg', 'right-leg-1', 'right-leg-2', closed=False)
        self.relate('connect', 'iron', 'board')
        self.relate('connect', 'left-leg', 'right-leg')
        self.relate('connect', 'left-leg', 'board')
        self.relate('connect', 'right-leg', 'board')
