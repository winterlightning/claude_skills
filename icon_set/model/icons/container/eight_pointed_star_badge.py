"""An eight-pointed badge alternates cardinal tips and square shoulders.

Keyshape SQUARE: visible bounds (0, 0, 64, 64).
Lucide badge informs the balanced closed perimeter; the source determines the
geometric eight-point silhouette instead of Lucide scallops. Centerline
extremes (2,2)-(62,62). Tips retain deliberate corners softened by round joins.
Equivalent square shoulders use radius 3 quarter circles.
Hosting measured with compose.py: plus passes, heart passes, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (eight-pointed-star-badge SQUARE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class EightPointedStarBadge(Container64):
    icon_id = 'eight-pointed-star-badge'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('eight-point-badge',)
    keywords = ('badge', 'star', 'emblem', 'outline')

    def build(self) -> None:
        self.add_line('n-rise', (23, 13), (32, 4))
        self.add_line('n-fall', (32, 4), (41, 13))
        self.add_line('ne-top', (41, 13), (48, 13))
        self.add_arc('ne-corner', (48, 13), (51, 16), radius_x=3)
        self.add_line('ne-side', (51, 16), (51, 23))
        self.add_line('e-rise', (51, 23), (60, 32))
        self.add_line('e-fall', (60, 32), (51, 41))
        self.add_line('se-side', (51, 41), (51, 48))
        self.add_arc('se-corner', (51, 48), (48, 51), radius_x=3)
        self.add_line('se-bottom', (48, 51), (41, 51))
        self.add_line('s-rise', (41, 51), (32, 60))
        self.add_line('s-fall', (32, 60), (23, 51))
        self.add_line('sw-bottom', (23, 51), (16, 51))
        self.add_arc('sw-corner', (16, 51), (13, 48), radius_x=3)
        self.add_line('sw-side', (13, 48), (13, 41))
        self.add_line('w-rise', (13, 41), (4, 32))
        self.add_line('w-fall', (4, 32), (13, 23))
        self.add_line('nw-side', (13, 23), (13, 16))
        self.add_arc('nw-corner', (13, 16), (16, 13), radius_x=3)
        self.add_line('nw-top', (16, 13), (23, 13))
        self.add_contour('outline', 'n-rise', 'n-fall', 'ne-top', 'ne-corner', 'ne-side', 'e-rise', 'e-fall', 'se-side', 'se-corner', 'se-bottom', 's-rise', 's-fall', 'sw-bottom', 'sw-corner', 'sw-side', 'w-rise', 'w-fall', 'nw-side', 'nw-corner', 'nw-top', closed=True)
