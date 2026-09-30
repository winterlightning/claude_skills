"""Gift box following user reference: broad bow on lid, empty box face.
SQUARE visible extremes (0,0)-(64,64), native 4-unit stroke.
User clipboard b296dcc9-5ef6-4656-8612-b557f0b5702d is the visual reference.
Lucide gift informs geometric construction. Bow bases share the lid edge
without duplicate strokes. The plain lid is eight units high on centerlines.
Paired symbols measured separately; native 32 does not fit. 24-unit prototypes are measured separately.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (gift-box-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'claude-opus-5-5'


class GiftBoxContainer(Container64):
    icon_id = 'gift-box-container'
    keyshape = Keyshape.SQUARE
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('gift', 'box', 'container')

    def build(self) -> None:
        self.add_line('lid-0', (18, 20), (10, 20))
        self.add_arc('lid-1', (10, 20), (6, 24), radius_x=4, sweep=False)
        self.add_arc('lid-2', (6, 24), (10, 28), radius_x=4, sweep=False)
        self.add_line('lid-3', (10, 28), (54, 28))
        self.add_arc('lid-4', (54, 28), (58, 24), radius_x=4, sweep=False)
        self.add_arc('lid-5', (58, 24), (54, 20), radius_x=4, sweep=False)
        self.add_line('lid-6', (54, 20), (46, 20))
        self.add_line('box-0', (10, 28), (10, 52))
        self.add_arc('box-1', (10, 52), (16, 58), radius_x=6, sweep=False)
        self.add_line('box-2', (16, 58), (48, 58))
        self.add_arc('box-3', (48, 58), (54, 52), radius_x=6, sweep=False)
        self.add_line('box-4', (54, 52), (54, 28))
        self.add_arc('bow--1-0', (32, 20), (18, 6), radius_x=14, sweep=False)
        self.add_arc('bow--1-1', (18, 6), (18, 20), radius_x=9, radius_y=7, sweep=False)
        self.add_line('bow--1-2', (18, 20), (32, 20))
        self.add_arc('bow-1-0', (32, 20), (46, 6), radius_x=14)
        self.add_arc('bow-1-1', (46, 6), (46, 20), radius_x=9, radius_y=7)
        self.add_line('bow-1-2', (46, 20), (32, 20))
        self.add_contour('lid', 'lid-0', 'lid-1', 'lid-2', 'lid-3', 'lid-4', 'lid-5', 'lid-6')
        self.add_contour('box', 'box-0', 'box-1', 'box-2', 'box-3', 'box-4')
        self.add_contour('bow--1', 'bow--1-0', 'bow--1-1', 'bow--1-2', closed=True)
        self.add_contour('bow-1', 'bow-1-0', 'bow-1-1', 'bow-1-2', closed=True)
        self.relate('connect', 'box', 'lid')
        self.relate('connect', 'bow--1', 'lid')
        self.relate('connect', 'bow-1', 'lid')
        self.relate('connect', 'bow--1', 'bow-1')
