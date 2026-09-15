'A hand spreads the thumb to the right and the little finger diagonally left. The three middle fingers curl side by side into a broad rounded palm.\n\nConstruction: Little finger spreads left and thumb right around three curled middle fingers. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08ec72a7-e066-5d37-92bf-00b3b47c7b57'
SOURCE_PATH = 'pictographic-primitives/wayfinding/shaka sign_08ec72a7-e066-5d37-92bf-00b3b47c7b57.svg'
AUTHOR = 'gpt-6'

class ShakaHandSign(Solo48):
    icon_id = 'shaka-hand-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('shaka', 'hand', 'gesture', 'thumb', 'fingers', 'greeting')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('little-1', (16, 26), (4, 12))
        self.add_line('little-2', (4, 12), (8, 8))
        self.add_line('little-3', (8, 8), (20, 20))
        self.add_arc('knuckles', (20, 20), (32, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('thumb-1', (32, 20), (40, 12))
        self.add_line('thumb-2', (40, 12), (44, 16))
        self.add_line('thumb-3', (44, 16), (36, 34))
        self.add_arc('palm', (36, 34), (24, 40), radius_x=12, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('palm-left', (24, 40), (12, 28), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('join', (12, 28), (16, 26))
        self.add_contour('hand', 'little-1', 'little-2', 'little-3', 'knuckles', 'thumb-1', 'thumb-2', 'thumb-3', 'palm', 'palm-left', 'join', closed=True)
