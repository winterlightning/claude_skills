"""A house-shaped enclosure has a pitched roof and rounded lower corners.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide house: mirrored pitched roof and rounded wall junctions; original and atomic-debug inspected.
The empty source silhouette is retained; no doorway added. Bilateral symmetry.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-house-icon SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleHouseIcon(Container64):
    icon_id = 'simple-house-icon'
    keyshape = Keyshape.SQUARE
    aliases = ('house-container',)
    keywords = ('simple', 'house', 'icon')

    def build(self) -> None:
        self.add_line('roof-right', (32, 6), (52, 22))
        self.add_arc('shoulder-right', (52, 22), (58, 32), radius_x=12)
        self.add_line('wall-right', (58, 32), (58, 54))
        self.add_arc('base-se', (58, 54), (54, 58), radius_x=4)
        self.add_line('base', (54, 58), (10, 58))
        self.add_arc('base-sw', (10, 58), (6, 54), radius_x=4)
        self.add_line('wall-left', (6, 54), (6, 32))
        self.add_arc('shoulder-left', (6, 32), (12, 22), radius_x=12)
        self.add_line('roof-left', (12, 22), (32, 6))
        self.add_contour('house', 'roof-right', 'shoulder-right', 'wall-right', 'base-se', 'base', 'base-sw', 'wall-left', 'shoulder-left', 'roof-left', closed=True)
