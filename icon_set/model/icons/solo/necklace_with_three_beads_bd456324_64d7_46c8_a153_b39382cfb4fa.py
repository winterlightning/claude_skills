"""An open necklace with two curling cords, two small beads and a larger central bead."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd456324-64d7-46c8-a153-b39382cfb4fa'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/diy jewelry_bd456324-64d7-46c8-a153-b39382cfb4fa.svg'
AUTHOR = 'astra-chatgpt'


class NecklaceWithThreeBeads(Solo48):
    icon_id = 'necklace-with-three-beads'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necklace', 'bead', 'beaded', 'jewellery', 'jewelry', 'diy', 'craft', 'cord', 'accessory')

    def build(self) -> None:
        # SQUARE: authored directly to its SOLO48 centerline extremes.
        self.add_arc('left-curl', (10, 2), (2, 10), radius_x=8, radius_y=8, sweep=False)
        self.add_line('left-run', (2, 10), (2, 12))
        self.add_arc('left-cord', (2, 12), (8, 25), radius_x=6, radius_y=13, sweep=False)
        self.add_contour('left-string', 'left-curl', 'left-run', 'left-cord', closed=False)
        self.add_arc('left-bead-a', (8, 25), (8, 31), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left-bead-b', (8, 31), (8, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left-bead', 'left-bead-a', 'left-bead-b', closed=True)
        self.relate("connect", 'left-string', 'left-bead')
        self.add_arc('right-curl', (38, 2), (46, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_line('right-run', (46, 10), (46, 12))
        self.add_arc('right-cord', (46, 12), (40, 25), radius_x=6, radius_y=13, sweep=True)
        self.add_contour('right-string', 'right-curl', 'right-run', 'right-cord', closed=False)
        self.add_arc('right-bead-a', (40, 25), (40, 31), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right-bead-b', (40, 31), (40, 25), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right-bead', 'right-bead-a', 'right-bead-b', closed=True)
        self.relate("connect", 'right-string', 'right-bead')
        self.add_arc('main-bead-a', (24, 30), (24, 46), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('main-bead-b', (24, 46), (24, 30), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('main-bead', 'main-bead-a', 'main-bead-b', closed=True)
        self.add_line('thread-left', (11, 28), (24, 30))
        self.add_line('thread-right', (24, 30), (37, 28))
        self.relate("connect", 'thread-left', 'left-bead')
        self.relate("connect", 'thread-left', 'main-bead')
        self.relate("connect", 'thread-right', 'right-bead')
        self.relate("connect", 'thread-right', 'main-bead')
        self.relate("connect", 'thread-left', 'thread-right')
