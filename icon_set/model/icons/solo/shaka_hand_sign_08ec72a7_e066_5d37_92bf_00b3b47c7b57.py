# Refinement: Broaden the thumb as well as the little finger.
# Repair: Broaden the little finger while retaining the thumb and folded knuckles.
"""A hand spreads the thumb to the right and the little finger diagonally left. The three middle fingers curl side by side into a broad rounded palm.

Construction: Little finger spreads left and thumb right around three curled middle fingers. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08ec72a7-e066-5d37-92bf-00b3b47c7b57'
SOURCE_PATH = 'pictographic-primitives/wayfinding/shaka sign_08ec72a7-e066-5d37-92bf-00b3b47c7b57.svg'
AUTHOR = 'gpt-6'

class ShakaHandSign(Solo48):
    icon_id = 'shaka-hand-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('shaka', 'hand', 'gesture', 'thumb', 'fingers', 'greeting')

    def build(self):
        self.add_line('little-1', (16, 26), (4, 12))
        self.add_line('little-2', (4, 12), (13, 8))
        self.add_line('little-3', (13, 8), (23, 20))
        self.add_arc('knuckles', (23, 20), (31, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('thumb-1', (31, 20), (34, 8))
        self.add_line('thumb-2', (34, 8), (44, 14))
        self.add_line('thumb-3', (44, 14), (36, 34))
        self.add_arc('palm', (36, 34), (24, 40), radius_x=12, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('palm-left', (24, 40), (12, 28), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('join', (12, 28), (16, 26))
        self.add_contour('hand', 'little-1', 'little-2', 'little-3', 'knuckles', 'thumb-1', 'thumb-2', 'thumb-3', 'palm', 'palm-left', 'join', closed=True)
