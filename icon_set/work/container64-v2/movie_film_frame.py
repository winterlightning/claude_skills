"""A landscape film cell with four perforation marks on each side.
Centerline extremes (2,10)-(62,54). Lucide film supplies tangent rounded
corners and repeated spacing. Both supplied references inform the side marks;
four marks retained from the second, consolidating the three-mark alternative.
Mirrored on both axes; no tiny oval holes.

Keyshape HRECT_L; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (movie-film-frame HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: perforations back on an 8-unit rhythm.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class MovieFilmFrame(Container64):
    icon_id = 'movie-film-frame'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('movie', 'film', 'frame')

    def build(self) -> None:
        self.add_line('top', (8, 12), (56, 12))
        self.add_arc('ne', (56, 12), (60, 16), radius_x=4)
        self.add_line('right', (60, 16), (60, 48))
        self.add_arc('se', (60, 48), (56, 52), radius_x=4)
        self.add_line('bottom', (56, 52), (8, 52))
        self.add_arc('sw', (8, 52), (4, 48), radius_x=4)
        self.add_line('left', (4, 48), (4, 16))
        self.add_arc('nw', (4, 16), (8, 12), radius_x=4)
        self.add_line('perforation-11-20', (12, 20), (14, 20))
        self.add_line('perforation-11-28', (12, 28), (14, 28))
        self.add_line('perforation-11-36', (12, 36), (14, 36))
        self.add_line('perforation-11-44', (12, 44), (14, 44))
        self.add_line('perforation-53-20', (50, 20), (52, 20))
        self.add_line('perforation-53-28', (50, 28), (52, 28))
        self.add_line('perforation-53-36', (50, 36), (52, 36))
        self.add_line('perforation-53-44', (50, 44), (52, 44))
        self.add_contour('frame', 'top', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
