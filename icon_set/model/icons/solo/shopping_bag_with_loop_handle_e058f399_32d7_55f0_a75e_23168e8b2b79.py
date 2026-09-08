"""A tapered shopping bag with an arched loop handle; omit paper seams.

Lucide construction: shopping-bag: rounded lower corners and coherent handle arc.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e058f399-32d7-55f0-a75e-23168e8b2b79'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/bag handle_e058f399-32d7-55f0-a75e-23168e8b2b79.svg'
AUTHOR = 'astra-chatgpt'


class ShoppingBagWithLoopHandle(Solo48):
    icon_id = 'shopping-bag-with-loop-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bag', 'shopping bag', 'paper bag', 'carrier', 'handle', 'retail', 'shopping', 'gift bag')

    def build(self) -> None:
        # Exact keyshape envelope: (6, 0, 42, 48).
        self.add_line('top-1', (11, 16), (14, 16))
        self.add_line('top-2', (14, 16), (34, 16))
        self.add_line('top-3', (34, 16), (37, 16))
        self.add_line('right', (37, 16), (40, 42))
        self.add_arc('br', (40, 42), (36, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_line('base', (36, 46), (12, 46))
        self.add_arc('bl', (12, 46), (8, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (8, 42), (11, 16))
        self.add_contour('body', 'top-1', 'top-2', 'top-3', 'right', 'br', 'base', 'bl', 'left', closed=True)
        self.add_line('handle-left', (14, 22), (14, 12))
        self.add_arc('handle-top', (14, 12), (34, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_line('handle-right', (34, 12), (34, 22))
        self.add_contour('handle', 'handle-left', 'handle-top', 'handle-right', closed=False)
        self.relate("connect", 'body', 'handle')
