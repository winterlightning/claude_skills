"""A cell membrane with rounded lobes enclosing an empty interior.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: cloud: coherent circular lobes and deliberate scallop junctions; symmetric membrane outline. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (white-blood-cell SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class WhiteBloodCell(Container64):
    icon_id = 'white-blood-cell'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('white', 'blood', 'cell')

    def build(self) -> None:
        self.add_arc('membrane-0', (21, 16), (43, 16), radius_x=11, radius_y=10)
        self.add_arc('membrane-1', (43, 16), (54, 27), radius_x=11)
        self.add_arc('membrane-2', (54, 27), (58, 35), radius_x=4, radius_y=8)
        self.add_arc('membrane-3', (58, 35), (50, 43), radius_x=8)
        self.add_arc('membrane-4', (50, 43), (36, 52), radius_x=9)
        self.add_arc('membrane-5', (36, 52), (28, 52), radius_x=4, radius_y=6)
        self.add_arc('membrane-6', (28, 52), (14, 43), radius_x=9)
        self.add_arc('membrane-7', (14, 43), (6, 35), radius_x=8)
        self.add_arc('membrane-8', (6, 35), (10, 27), radius_x=4, radius_y=8)
        self.add_arc('membrane-9', (10, 27), (21, 16), radius_x=11)
        self.add_contour('membrane', 'membrane-0', 'membrane-1', 'membrane-2', 'membrane-3', 'membrane-4', 'membrane-5', 'membrane-6', 'membrane-7', 'membrane-8', 'membrane-9', closed=True)
