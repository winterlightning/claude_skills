"""Moved the handle dome and base inward; preserved the tapered bag and split the handle at its true attachment.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: shopping-bag: coherent handle and rounded lower corners.
"""
# Independent repair of shopping-bag-with-loop-handle; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e058f399-32d7-55f0-a75e-23168e8b2b79'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/bag handle_e058f399-32d7-55f0-a75e-23168e8b2b79.svg'
AUTHOR = 'gpt-6'

class ShoppingBagWithLoopHandle(Solo48):
    icon_id = 'shopping-bag-with-loop-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('bag', 'shopping bag', 'paper bag', 'carrier', 'handle', 'retail', 'shopping', 'gift bag')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('top-1', (11, 16), (14, 16))
        self.add_line('top-2', (14, 16), (34, 16))
        self.add_line('top-3', (34, 16), (37, 16))
        self.add_line('right', (37, 16), (40, 40))
        self.add_arc('br', (40, 40), (36, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line('base', (36, 44), (12, 44))
        self.add_arc('bl', (12, 44), (8, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (8, 40), (11, 16))
        self.add_contour('body', 'top-1', 'top-2', 'top-3', 'right', 'br', 'base', 'bl', 'left', closed=True)
        self.add_line('handle-left-lower', (14, 22), (14, 16))
        self.add_line('handle-left-upper', (14, 16), (14, 14))
        self.add_arc('handle-top', (14, 14), (34, 14), radius_x=10, radius_y=10, sweep=True)
        self.add_line('handle-right-upper', (34, 14), (34, 16))
        self.add_line('handle-right-lower', (34, 16), (34, 22))
        self.add_contour('handle', 'handle-left-lower', 'handle-left-upper', 'handle-top', 'handle-right-upper', 'handle-right-lower', closed=False)
        self.relate('connect', 'body', 'handle')
