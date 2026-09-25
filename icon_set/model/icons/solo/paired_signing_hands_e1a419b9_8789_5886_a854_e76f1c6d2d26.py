'Two hands face each other with thumb and finger tips forming small enclosed loops near the centre. Their remaining fingers extend upward at different angles above the curved wrists.\n\nConstruction: Two mirrored signing hands curve inward around thumb-index loops. Outer fingers sweep upward. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1a419b9-8789-5886-a854-e76f1c6d2d26'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hands language_e1a419b9-8789-5886-a854-e76f1c6d2d26.svg'
AUTHOR = 'gpt-6'

class PairedSigningHands(Solo48):
    icon_id = 'paired-signing-hands'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('hands', 'signing', 'language', 'gesture', 'fingers', 'communication')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('left-outer-wrist', (4, 40), (4, 24))
        self.add_arc('left-outer-finger', (4, 24), (12, 8), radius_x=8, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('left-fingertip', (12, 8), (16, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('left-fold', (16, 12), (12, 19))
        self.add_arc('left-thumb', (12, 19), (19, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('left-palm', (19, 26), (16, 34), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('left-inner-wrist', (16, 34), (13, 37), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('left-cuff', (13, 37), (13, 40))
        self.add_line('right-outer-wrist', (44, 40), (44, 24))
        self.add_arc('right-outer-finger', (44, 24), (36, 8), radius_x=8, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('right-fingertip', (36, 8), (32, 12), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('right-fold', (32, 12), (36, 19))
        self.add_arc('right-thumb', (36, 19), (29, 26), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('right-palm', (29, 26), (32, 34), radius_x=3, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('right-inner-wrist', (32, 34), (35, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('right-cuff', (35, 37), (35, 40))
        self.add_contour('left', 'left-outer-wrist', 'left-outer-finger', 'left-fingertip', 'left-fold', 'left-thumb', 'left-palm', 'left-inner-wrist', 'left-cuff', closed=False)
        self.add_contour('right', 'right-outer-wrist', 'right-outer-finger', 'right-fingertip', 'right-fold', 'right-thumb', 'right-palm', 'right-inner-wrist', 'right-cuff', closed=False)
