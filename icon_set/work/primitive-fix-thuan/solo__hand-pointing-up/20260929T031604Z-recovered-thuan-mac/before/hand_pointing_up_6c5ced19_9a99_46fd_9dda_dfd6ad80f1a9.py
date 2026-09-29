# Repair: Give the raised thumb a full-width diagonal outline instead of a pinched wedge.
"""A hand raises one long index finger vertically while the other three fingers curl beside it. The thumb angles outward to the left above the rounded palm and wrist.

Construction: One extended index finger above a closed palm, with a projecting thumb. Bounds (8,4)-(40,44).
Lucide: hand: rounded finger cap and palm contour."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9'
SOURCE_PATH = 'pictographic-primitives/wayfinding/finger point 1_6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9.svg'
AUTHOR = 'gpt-6'

class HandPointingUp(Solo48):
    icon_id = 'hand-pointing-up'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'pointing', 'up', 'index', 'finger', 'gesture')

    def build(self):
        self.add_line('finger-left', (16, 24), (16, 8))
        self.add_arc('tip', (16, 8), (24, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('finger-right-1', (24, 8), (24, 24))
        self.add_line('finger-right-2', (24, 24), (32, 24))
        self.add_arc('knuckles', (32, 24), (40, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('palm-right', (40, 32), (28, 44), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('palm-base', (28, 44), (24, 44))
        self.add_line('thumb-1', (24, 44), (8, 28))
        self.add_line('thumb-2', (8, 28), (8, 16))
        self.add_line('thumb-3', (8, 16), (16, 24))
        self.add_contour('outline', 'finger-left', 'tip', 'finger-right-1', 'finger-right-2', 'knuckles', 'palm-right', 'palm-base', 'thumb-1', 'thumb-2', 'thumb-3', closed=True)
