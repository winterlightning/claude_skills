"""An empty leaf-like frame with rounded northwest and southeast corners.
The other two corners remain deliberately pointed; no vein or stem is added.

Keyshape HRECT_XL; centerline extremes recorded in build below.
Lucide square informs tangent corner construction; leaf was inspected but its botanical silhouette is not a useful match. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (horizontal-leaf-frame HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class HorizontalLeafFrame(Container64):
    icon_id = 'horizontal-leaf-frame'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('rounded-leaf-shape',)
    keywords = ('horizontal', 'leaf', 'frame')

    def build(self) -> None:
        self.add_line('top', (25, 10), (60, 10))
        self.add_line('right', (60, 10), (60, 36))
        self.add_arc('se', (60, 36), (39, 54), radius_x=21, radius_y=18)
        self.add_line('bottom', (39, 54), (4, 54))
        self.add_line('left', (4, 54), (4, 28))
        self.add_arc('nw', (4, 28), (25, 10), radius_x=21, radius_y=18)
        self.add_contour('outline', 'top', 'right', 'se', 'bottom', 'left', 'nw', closed=True)
