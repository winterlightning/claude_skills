"""An empty portrait frame with matching soft corners; no source features removed.

Keyshape VRECT_XL; centerline extremes recorded in build below.
Lucide rectangle-vertical informs paired straight runs and consistent corner radii. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rounded-vertical-rectangle VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundedVerticalRectangle(Container64):
    icon_id = 'rounded-vertical-rectangle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rounded', 'vertical', 'rectangle')

    def build(self) -> None:
        self.add_line('top', (17, 4), (47, 4))
        self.add_arc('ne', (47, 4), (54, 11), radius_x=7)
        self.add_line('right', (54, 11), (54, 53))
        self.add_arc('se', (54, 53), (47, 60), radius_x=7)
        self.add_line('bottom', (47, 60), (17, 60))
        self.add_arc('sw', (17, 60), (10, 53), radius_x=7)
        self.add_line('left', (10, 53), (10, 11))
        self.add_arc('nw', (10, 11), (17, 4), radius_x=7)
        self.add_contour('outline', 'top', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
