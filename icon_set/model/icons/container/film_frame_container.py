"""A cinema frame with top and bottom perforation rails.

SQUARE: centerline extremes (2,2)-(62,62), visible (0,0)-(64,64).
Lucide film informs the rounded frame and connected rails; the source
sets the horizontal orientation and three short perforations per rail.
All six marks retained; export defects omitted. Mirrored on both axes.
Batch 01 hosting measured with compose.py: plus pass. heart, check do not pass (including uncertified review).
"""

from ...keyshapes import Keyshape
from ._base import Container64


class FilmFrameContainer(Container64):
    icon_id = 'film-frame-container'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('cinema-movie-film-frame',)
    keywords = ('film', 'frame', 'container')

    def build(self) -> None:
        self.add_line("top", (8, 2), (56, 2))
        self.add_arc("ne", (56, 2), (62, 8), radius_x=6)
        self.add_line("right", (62, 8), (62, 56))
        self.add_arc("se", (62, 56), (56, 62), radius_x=6)
        self.add_line("bottom", (56, 62), (8, 62))
        self.add_arc("sw", (8, 62), (2, 56), radius_x=6)
        self.add_line("left", (2, 56), (2, 8))
        self.add_arc("nw", (2, 8), (8, 2), radius_x=6)
        self.add_contour("frame", "top", "ne", "right", "se", "bottom", "sw", "left", "nw", closed=True)
        for y in (18, 46):
            self.add_line(f"rail-{y}", (2, y), (62, y))
            self.relate("connect", "frame", f"rail-{y}")
        for y in (10, 54):
            for x in (14, 30, 46):
                self.add_line(f"perforation-{x}-{y}", (x, y), (x + 4, y))
