'An angled open hand has four rounded fingers gathered toward the upper-left and a thumb raised at the right. A short curved motion stroke sits beyond the fingertips.\n\nConstruction: Four rounded fingertips with shared eight-unit spacing and an outward thumb. Finger creases reduced to three straight seams; clapping reference reduced to its dominant raised hand. Bounds (6,6)-(42,42).\nLucide: hand: rounded fingertip arches and broad palm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cdbf5cfc-c77a-43ac-925c-d8a3a7e49753'
SOURCE_PATH = 'pictographic-primitives/wayfinding/clap_cdbf5cfc-c77a-43ac-925c-d8a3a7e49753.svg'
AUTHOR = 'gpt-6'

class ClappingHand(Solo48):
    icon_id = 'clapping-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'clap', 'applause', 'palm', 'fingers', 'gesture')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('little-side', (6, 26), (6, 20))
        self.add_arc('little-tip', (6, 20), (14, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('ring-side', (14, 20), (14, 14))
        self.add_arc('ring-tip', (14, 14), (22, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('middle-side', (22, 14), (22, 10))
        self.add_arc('middle-tip', (22, 10), (30, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('index-side', (30, 10), (30, 14))
        self.add_arc('index-tip', (30, 14), (38, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('thumb-side-1', (38, 14), (38, 23))
        self.add_line('thumb-side-2', (38, 23), (42, 27))
        self.add_line('thumb-side-3', (42, 27), (34, 35))
        self.add_arc('palm-right', (34, 35), (24, 42), radius_x=10, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('palm-left', (24, 42), (6, 26), radius_x=18, radius_y=16, large_arc=False, sweep=True)
        self.add_line('finger-seam-14', (14, 20), (14, 26))
        self.add_line('finger-seam-22', (22, 14), (22, 26))
        self.add_line('finger-seam-30', (30, 14), (30, 26))
        self.add_arc('clap-motion', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('palm', 'little-side', 'little-tip', 'ring-side', 'ring-tip', 'middle-side', 'middle-tip', 'index-side', 'index-tip', 'thumb-side-1', 'thumb-side-2', 'thumb-side-3', 'palm-right', 'palm-left', closed=True)
        self.relate('connect', 'finger-seam-14', 'palm')
        self.relate('connect', 'finger-seam-22', 'palm')
        self.relate('connect', 'finger-seam-30', 'palm')
