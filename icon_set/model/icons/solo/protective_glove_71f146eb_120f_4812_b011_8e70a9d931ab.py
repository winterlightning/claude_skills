'An upright glove has four rounded fingers of different heights and a thumb spreading diagonally right. The sides widen above a straight open cuff, with short divisions between the fingers.\n\nConstruction: Four rounded fingertips with shared eight-unit spacing and an outward thumb. Finger creases reduced to three straight seams; clapping reference reduced to its dominant raised hand. Bounds (6,6)-(42,42).\nLucide: hand: rounded fingertip arches and broad palm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71f146eb-120f-4812-b011-8e70a9d931ab'
SOURCE_PATH = 'pictographic-primitives/wayfinding/gloves_71f146eb-120f-4812-b011-8e70a9d931ab.svg'
AUTHOR = 'gpt-6'

class ProtectiveGlove(Solo48):
    icon_id = 'protective-glove'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('glove', 'hand', 'protection', 'cleaning', 'fingers', 'cuff')

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
        self.add_line('palm-right-1', (34, 35), (34, 42))
        self.add_line('palm-right-2', (34, 42), (10, 42))
        self.add_line('palm-left-1', (10, 42), (10, 32))
        self.add_line('palm-left-2', (10, 32), (6, 26))
        self.add_line('finger-seam-14', (14, 20), (14, 26))
        self.add_line('finger-seam-22', (22, 14), (22, 26))
        self.add_line('finger-seam-30', (30, 14), (30, 26))
        self.add_contour('palm', 'little-side', 'little-tip', 'ring-side', 'ring-tip', 'middle-side', 'middle-tip', 'index-side', 'index-tip', 'thumb-side-1', 'thumb-side-2', 'thumb-side-3', 'palm-right-1', 'palm-right-2', 'palm-left-1', 'palm-left-2', closed=True)
        self.relate('connect', 'finger-seam-14', 'palm')
        self.relate('connect', 'finger-seam-22', 'palm')
        self.relate('connect', 'finger-seam-30', 'palm')
