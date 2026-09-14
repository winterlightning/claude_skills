# Variant of stone-bridge; parent file remains unchanged.
"""A compact stone bridge with broad piers and one smooth arch.

Lucide bridge informs the balanced span and paired supports; masonry joints,
railings, and water are omitted to keep a single uninterrupted silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class StoneBridgeVariant2(Solo48):
    icon_id = 'stone-bridge-v2'
    variant_of = 'stone-bridge'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ('masonry bridge',)
    keywords = ('stone', 'bridge', 'arch', 'crossing', 'span')

    def build(self) -> None:
        self.add_line('deck', (6, 8), (42, 8))
        self.add_arc('right-shoulder', (42, 8), (46, 12), radius_x=4)
        self.add_line('right-outside', (46, 12), (46, 40))
        self.add_line('right-foot', (46, 40), (36, 40))
        self.add_line('right-opening', (36, 40), (36, 32))
        self.add_arc('arch', (36, 32), (12, 32), radius_x=12, sweep=False)
        self.add_line('left-opening', (12, 32), (12, 40))
        self.add_line('left-foot', (12, 40), (2, 40))
        self.add_line('left-outside', (2, 40), (2, 12))
        self.add_arc('left-shoulder', (2, 12), (6, 8), radius_x=4)
        self.add_contour('outline', 'deck', 'right-shoulder', 'right-outside', 'right-foot', 'right-opening', 'arch', 'left-opening', 'left-foot', 'left-outside', 'left-shoulder', closed=True)
