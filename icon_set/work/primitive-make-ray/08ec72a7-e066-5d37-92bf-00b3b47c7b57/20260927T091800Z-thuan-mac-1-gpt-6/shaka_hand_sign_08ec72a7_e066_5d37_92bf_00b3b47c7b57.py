# Refinement: Broaden the thumb as well as the little finger.
# Repair: Broaden the little finger while retaining the thumb and folded knuckles.
"""A hand spreads the thumb to the right and the little finger diagonally left. The three middle fingers curl side by side into a broad rounded palm.

Construction: Little finger spreads left and thumb right around three curled middle fingers. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '08ec72a7-e066-5d37-92bf-00b3b47c7b57'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shaka-hand-sign/20260927T091411Z-thuan-mac-1/reference/shaka sign_08ec72a7-e066-5d37-92bf-00b3b47c7b57.svg'
AUTHOR = "gpt-6"

class ShakaHandSign(Solo48):
    icon_id = 'shaka-hand-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('shaka', 'hand', 'gesture', 'thumb', 'fingers', 'greeting')

    # Revision plan: The previous angular fork hid the three curled middle fingers. Shape their three knuckles in the same hand outline; the splayed thumb and little finger remain. Lucide hand informs palm flow.
    # Revision plan: The previous angular fork hid the three curled middle fingers. Shape their three knuckles in the same hand outline; the splayed thumb and little finger remain. Lucide hand informs palm flow.
    # Revision plan: The previous angular fork hid the three curled middle fingers. Shape their three knuckles in the same hand outline; the splayed thumb and little finger remain. Lucide hand informs palm flow.
    # Revision plan: The previous angular fork hid the three curled middle fingers. Shape their three knuckles in the same hand outline; the splayed thumb and little finger remain. Lucide hand informs palm flow.
    # Revision plan: The previous angular fork hid the three curled middle fingers. Shape their three knuckles in the same hand outline; the splayed thumb and little finger remain. Lucide hand informs palm flow.
    def build(self):
        # A single outline follows splayed little finger, three folded knuckles,
        # outward thumb and round palm. Fold valleys are encoded in the contour.
        self.add_line('little-1', (16, 26), (4, 12))
        self.add_line('little-2', (4, 12), (13, 8))
        self.add_line('little-3', (13, 8), (20, 18))
        self.add_arc('fold-one', (20, 18), (24, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('fold-two', (24, 20), (28, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('fold-three', (28, 20), (32, 19), radius_x=3, radius_y=3, sweep=True)
        self.add_line('thumb-1', (32, 19), (35, 8))
        self.add_line('thumb-2', (35, 8), (44, 14))
        self.add_line('thumb-3', (44, 14), (36, 34))
        self.add_arc('palm', (36, 34), (24, 40), radius_x=12, radius_y=6, sweep=True)
        self.add_arc('palm-left', (24, 40), (12, 28), radius_x=12, sweep=True)
        self.add_line('palm-join', (12, 28), (16, 26))
        self.add_contour('hand', 'little-1', 'little-2', 'little-3', 'fold-one', 'fold-two', 'fold-three', 'thumb-1', 'thumb-2', 'thumb-3', 'palm', 'palm-left', 'palm-join', closed=True)
