"""Five small side-facing birds in staggered flight; extremes (2,2)-(46,46). Open swept silhouettes retain raised wings, curved bellies and short heads while dropping closed miniature interiors."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7c1e75f-5c89-447a-8fb6-cc3765f450b1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_b7c1e75f-5c89-447a-8fb6-cc3765f450b1.svg'
AUTHOR = 'gpt-6'


class BirdFlock(Solo48):
    icon_id = 'bird-flock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('birds', 'flock', 'flying', 'group', 'five', 'migration', 'sky', 'flight')

    def build(self) -> None:
        self.add_line('wing-0-1', (2, 2), (6, 8))
        self.add_line('wing-0-2', (6, 8), (2, 8))
        self.add_arc('belly-0', (2, 8), (14, 8), radius_x=6, radius_y=5, sweep=False)
        self.add_line('head-0-1', (14, 8), (11, 5))
        self.add_line('head-0-2', (11, 5), (8, 7))
        self.add_contour('bird-0', 'wing-0-1', 'wing-0-2', 'belly-0', 'head-0-1', 'head-0-2', closed=False)
        self.add_line('wing-1-1', (20, 10), (24, 16))
        self.add_line('wing-1-2', (24, 16), (20, 16))
        self.add_arc('belly-1', (20, 16), (32, 16), radius_x=6, radius_y=5, sweep=False)
        self.add_line('head-1-1', (32, 16), (29, 13))
        self.add_line('head-1-2', (29, 13), (26, 15))
        self.add_contour('bird-1', 'wing-1-1', 'wing-1-2', 'belly-1', 'head-1-1', 'head-1-2', closed=False)
        self.add_line('wing-2-1', (34, 25), (38, 31))
        self.add_line('wing-2-2', (38, 31), (34, 31))
        self.add_arc('belly-2', (34, 31), (46, 31), radius_x=6, radius_y=5, sweep=False)
        self.add_line('head-2-1', (46, 31), (43, 28))
        self.add_line('head-2-2', (43, 28), (40, 30))
        self.add_contour('bird-2', 'wing-2-1', 'wing-2-2', 'belly-2', 'head-2-1', 'head-2-2', closed=False)
        self.add_line('wing-3-1', (20, 35), (24, 41))
        self.add_line('wing-3-2', (24, 41), (20, 41))
        self.add_arc('belly-3', (20, 41), (32, 41), radius_x=6, radius_y=5, sweep=False)
        self.add_line('head-3-1', (32, 41), (29, 38))
        self.add_line('head-3-2', (29, 38), (26, 40))
        self.add_contour('bird-3', 'wing-3-1', 'wing-3-2', 'belly-3', 'head-3-1', 'head-3-2', closed=False)
        self.add_line('wing-4-1', (2, 32), (6, 38))
        self.add_line('wing-4-2', (6, 38), (2, 38))
        self.add_arc('belly-4', (2, 38), (14, 38), radius_x=6, radius_y=5, sweep=False)
        self.add_line('head-4-1', (14, 38), (11, 35))
        self.add_line('head-4-2', (11, 35), (8, 37))
        self.add_contour('bird-4', 'wing-4-1', 'wing-4-2', 'belly-4', 'head-4-1', 'head-4-2', closed=False)
