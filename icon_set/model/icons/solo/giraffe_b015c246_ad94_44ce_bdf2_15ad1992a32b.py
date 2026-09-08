"""Right-facing giraffe head with long diagonal neck, large leaf ear and upright ossicone; eye omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b015c246-ad94-44ce-bdf2-15ad1992a32b'
SOURCE_PATH = 'pictographic-primitives/animals/giraffe_b015c246-ad94-44ce-bdf2-15ad1992a32b.svg'
AUTHOR = 'gpt-6'


class GiraffeHead(Solo48):
    icon_id = 'giraffe-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('giraffe', 'head', 'neck', 'ossicone', 'ear', 'profile', 'animal', 'safari')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 0, 48, 48); centerlines inset by stroke radius 2.
        self.add_line('outline-1', (2, 46), (15, 18))
        self.add_arc('outline-2', (15, 18), (2, 5), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('outline-3', (2, 5), (17, 17), radius_x=15, radius_y=15, sweep=True)
        self.add_line('outline-4', (17, 17), (20, 10))
        self.add_line('outline-5', (20, 10), (19, 2))
        self.add_line('outline-6', (19, 2), (25, 2))
        self.add_line('outline-7', (25, 2), (26, 10))
        self.add_line('outline-8', (26, 10), (29, 10))
        self.add_line('outline-9', (29, 10), (46, 27))
        self.add_line('outline-10', (46, 27), (46, 29))
        self.add_arc('outline-11', (46, 29), (41, 34), radius_x=5, radius_y=5, sweep=True)
        self.add_line('outline-12', (41, 34), (23, 29))
        self.add_line('outline-13', (23, 29), (17, 46))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', 'outline-12', 'outline-13', closed=False)
