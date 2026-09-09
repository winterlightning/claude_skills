# Variant of necklace-with-three-beads; parent file remains unchanged.
'Necklace variant with the two small side beads removed and the cord reconnected to the central bead. SQUARE preserves the open curling cord. No useful Lucide subject match.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd456324-64d7-46c8-a153-b39382cfb4fa'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/diy jewelry_bd456324-64d7-46c8-a153-b39382cfb4fa.svg'
AUTHOR = 'gpt-6'

class NecklaceWithThreeBeadsVariant2(Solo48):
    icon_id = 'necklace-with-three-beads-v2'
    variant_of = 'necklace-with-three-beads'
    variant_label = 'Single central bead'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('necklace', 'bead', 'beaded', 'jewellery', 'jewelry', 'diy', 'craft', 'cord', 'accessory')

    def build(self) -> None:
        self.add_arc('left-curl', (10, 2), (2, 10), radius_x=8, radius_y=8, sweep=False)
        self.add_line('left-run', (2, 10), (2, 12))
        self.add_arc('left-cord', (2, 12), (8, 25), radius_x=6, radius_y=13, sweep=False)
        self.add_contour('left-string', 'left-curl', 'left-run', 'left-cord', closed=False)
        self.add_arc('right-curl', (38, 2), (46, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_line('right-run', (46, 10), (46, 12))
        self.add_arc('right-cord', (46, 12), (40, 25), radius_x=6, radius_y=13, sweep=True)
        self.add_contour('right-string', 'right-curl', 'right-run', 'right-cord', closed=False)
        self.add_arc('main-bead-a', (24, 30), (24, 46), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('main-bead-b', (24, 46), (24, 30), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('main-bead', 'main-bead-a', 'main-bead-b', closed=True)
        self.add_line('thread-left', (8, 25), (24, 30))
        self.add_line('thread-right', (24, 30), (40, 25))
        self.relate('connect', 'thread-left', 'main-bead')
        self.relate('connect', 'thread-right', 'main-bead')
        self.relate('connect', 'thread-left', 'thread-right')
        self.relate('connect','thread-left','left-string')
        self.relate('connect','thread-right','right-string')
