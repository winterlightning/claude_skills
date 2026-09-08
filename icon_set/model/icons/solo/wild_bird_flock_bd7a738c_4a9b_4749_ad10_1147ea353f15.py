"""Three flying birds with broad raised wings; extremes (2,2)-(46,46). Directional silhouettes; small feather teeth omitted to preserve distinct birds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd7a738c-4a9b-4749-ad10-1147ea353f15'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_bd7a738c-4a9b-4749-ad10-1147ea353f15.svg'
AUTHOR = 'gpt-6'


class ThreeFlyingBirds(Solo48):
    icon_id = 'three-flying-birds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('birds', 'three', 'flying', 'flock', 'doves', 'sky', 'flight', 'group')

    def build(self) -> None:
        self.add_line('upper-0-1', (2, 12), (8, 12))
        self.add_line('upper-0-2', (8, 12), (2, 2))
        self.add_arc('wing-front-0', (2, 2), (14, 9), radius_x=18, radius_y=14, sweep=True)
        self.add_line('wing-tip-0', (14, 9), (15, 3))
        self.add_arc('wing-small-0', (15, 3), (19, 11), radius_x=6, radius_y=8, sweep=True)
        self.add_line('beak-0', (19, 11), (22, 12))
        self.add_arc('belly-0', (22, 12), (2, 12), radius_x=10, radius_y=6, sweep=True)
        self.add_contour('bird-0', 'upper-0-1', 'upper-0-2', 'wing-front-0', 'wing-tip-0', 'wing-small-0', 'beak-0', 'belly-0', closed=True)
        self.add_line('upper-1-1', (26, 29), (32, 29))
        self.add_line('upper-1-2', (32, 29), (26, 19))
        self.add_arc('wing-front-1', (26, 19), (38, 26), radius_x=18, radius_y=14, sweep=True)
        self.add_line('wing-tip-1', (38, 26), (39, 20))
        self.add_arc('wing-small-1', (39, 20), (43, 28), radius_x=6, radius_y=8, sweep=True)
        self.add_line('beak-1', (43, 28), (46, 29))
        self.add_arc('belly-1', (46, 29), (26, 29), radius_x=10, radius_y=6, sweep=True)
        self.add_contour('bird-1', 'upper-1-1', 'upper-1-2', 'wing-front-1', 'wing-tip-1', 'wing-small-1', 'beak-1', 'belly-1', closed=True)
        self.add_line('upper-2-1', (4, 40), (10, 40))
        self.add_line('upper-2-2', (10, 40), (4, 30))
        self.add_arc('wing-front-2', (4, 30), (16, 37), radius_x=18, radius_y=14, sweep=True)
        self.add_line('wing-tip-2', (16, 37), (17, 31))
        self.add_arc('wing-small-2', (17, 31), (21, 39), radius_x=6, radius_y=8, sweep=True)
        self.add_line('beak-2', (21, 39), (24, 40))
        self.add_arc('belly-2', (24, 40), (4, 40), radius_x=10, radius_y=6, sweep=True)
        self.add_contour('bird-2', 'upper-2-1', 'upper-2-2', 'wing-front-2', 'wing-tip-2', 'wing-small-2', 'beak-2', 'belly-2', closed=True)
