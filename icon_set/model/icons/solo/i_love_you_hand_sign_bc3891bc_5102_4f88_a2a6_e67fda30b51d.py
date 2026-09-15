# Repair: Widen the extended thumb while preserving the I-love-you finger arrangement.
"""A hand holds the index and little fingers upright and spreads the thumb to the left. The middle and ring fingers fold down together above a wide rounded palm.

Construction: Index and little fingers stand upright while the thumb spreads left; middle fingers fold inward. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc3891bc-5102-4f88-a2a6-e67fda30b51d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/love you sign_bc3891bc-5102-4f88-a2a6-e67fda30b51d.svg'
AUTHOR = 'gpt-6'

class ILoveYouHandSign(Solo48):
    icon_id = 'i-love-you-hand-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hand', 'love', 'sign', 'language', 'fingers', 'gesture')

    def build(self):
        self.add_line('thumb-1', (14, 34), (6, 28))
        self.add_line('thumb-2', (6, 28), (6, 16))
        self.add_line('thumb-3', (6, 16), (14, 22))
        self.add_line('thumb-4', (14, 22), (14, 10))
        self.add_arc('index-tip', (14, 10), (22, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('index', (22, 10), (22, 26))
        self.add_arc('fold', (22, 26), (34, 26), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('little-inner', (34, 26), (34, 14))
        self.add_arc('little-tip', (34, 14), (42, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('little', (42, 14), (42, 28))
        self.add_arc('palm', (42, 28), (28, 42), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('base', (28, 42), (22, 42))
        self.add_arc('thumb-base', (22, 42), (14, 34), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('hand', 'thumb-1', 'thumb-2', 'thumb-3', 'thumb-4', 'index-tip', 'index', 'fold', 'little-inner', 'little-tip', 'little', 'palm', 'base', 'thumb-base', closed=True)
