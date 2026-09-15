"""A landscape film cell with four perforation marks on each side.
Centerline extremes (2,10)-(62,54). Lucide film supplies tangent rounded
corners and repeated spacing. Both supplied references inform the side marks;
four marks retained from the second, consolidating the three-mark alternative.
Mirrored on both axes; no tiny oval holes.

Keyshape HRECT_L; authored directly on CONTAINER64. Hosting measured with compose.py: plus passes, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class MovieFilmFrame(Container64):
    icon_id = 'movie-film-frame'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('movie', 'film', 'frame')

    def build(self) -> None:
        self.add_line('top', (6,10), (58,10))
        self.add_arc('ne', (58,10), (62,14), radius_x=4)
        self.add_line('right', (62,14), (62,50))
        self.add_arc('se', (62,50), (58,54), radius_x=4)
        self.add_line('bottom', (58,54), (6,54))
        self.add_arc('sw', (6,54), (2,50), radius_x=4)
        self.add_line('left', (2,50), (2,14))
        self.add_arc('nw', (2,14), (6,10), radius_x=4)
        self.add_contour('frame', 'top','ne','right','se','bottom','sw','left','nw', closed=True)
        for x in (11,53):
            for y in (20,28,36,44):
                self.add_line(f'perforation-{x}-{y}', (x-1,y), (x+1,y))
