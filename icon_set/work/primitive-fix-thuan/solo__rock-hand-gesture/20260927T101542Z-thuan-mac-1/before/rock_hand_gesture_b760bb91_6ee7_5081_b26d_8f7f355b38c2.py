'A hand raises the index and little fingers vertically while folding the middle and ring fingers inward. The thumb crosses the curled fingers above a rounded palm and short wrist.\n\nConstruction: Two upright fingers frame two folded fingers; thumb crosses the lower palm. Bounds (8,4)-(40,44).\nLucide: hand: rounded fingertip caps and broad palm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b760bb91-6ee7-5081-b26d-8f7f355b38c2'
SOURCE_PATH = 'pictographic-primitives/wayfinding/rock hand_b760bb91-6ee7-5081-b26d-8f7f355b38c2.svg'
AUTHOR = 'gpt-6'

class RockHandGesture(Solo48):
    icon_id = 'rock-hand-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('rock', 'hand', 'horns', 'gesture', 'fingers', 'music')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('index', (8, 32), (8, 8))
        self.add_arc('index-tip', (8, 8), (16, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('index-inner', (16, 8), (16, 24))
        self.add_arc('fold-one', (16, 24), (24, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('fold-two', (24, 24), (32, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('little-inner', (32, 24), (32, 8))
        self.add_arc('little-tip', (32, 8), (40, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('little', (40, 8), (40, 32))
        self.add_arc('palm-right', (40, 32), (28, 44), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('wrist', (28, 44), (20, 44))
        self.add_arc('palm-left', (20, 44), (8, 32), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('thumb-1', (8, 32), (16, 32))
        self.add_line('thumb-2', (16, 32), (24, 36))
        self.add_contour('hand', 'index', 'index-tip', 'index-inner', 'fold-one', 'fold-two', 'little-inner', 'little-tip', 'little', 'palm-right', 'wrist', 'palm-left', closed=True)
        self.add_contour('thumb', 'thumb-1', 'thumb-2', closed=False)
        self.relate('connect', 'thumb', 'hand')
