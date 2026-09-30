"""An empty leaf-like frame with rounded northwest and southeast corners.
The other two corners remain deliberately pointed; no vein or stem is added.

Keyshape SQUARE; centerline extremes recorded in build below.
Lucide square informs tangent corner construction; leaf was inspected but its botanical silhouette is not a useful match. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-leaf-frame SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareLeafFrame(Container64):
    icon_id = 'square-leaf-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('rounded-leaf-shape-icon',)
    keywords = ('square', 'leaf', 'frame')

    def build(self) -> None:
        self.add_line('top', (27, 6), (58, 6))
        self.add_line('right', (58, 6), (58, 37))
        self.add_arc('se', (58, 37), (37, 58), radius_x=21)
        self.add_line('bottom', (37, 58), (6, 58))
        self.add_line('left', (6, 58), (6, 27))
        self.add_arc('nw', (6, 27), (27, 6), radius_x=21)
        self.add_contour('outline', 'top', 'right', 'se', 'bottom', 'left', 'nw', closed=True)
