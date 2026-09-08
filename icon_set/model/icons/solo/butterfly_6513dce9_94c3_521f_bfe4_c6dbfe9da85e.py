"""Mirror-symmetrical butterfly with large upper and smaller lower lobes; circular lobe construction follows Lucide bug simplicity. Wing pattern omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6513dce9-94c3-521f-bfe4-c6dbfe9da85e'
SOURCE_PATH = 'pictographic-primitives/animals/butterfly_6513dce9-94c3-521f-bfe4-c6dbfe9da85e.svg'
AUTHOR = 'gpt-6'


class Butterfly(Solo48):
    icon_id = 'butterfly'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('butterfly', 'insect', 'wings', 'antennae', 'nature', 'spring', 'moth', 'symmetry')

    def build(self) -> None:
        # SQUARE centerline extremes recorded in batch-02-review.md.
        self.add_arc('left-upper-in', (24, 22), (12, 10), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('left-upper-out', (12, 10), (2, 20), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('left-shoulder', (2, 20), (12, 30), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('left-lower-out', (12, 30), (6, 38), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('left-lower-base', (6, 38), (14, 46), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('left-lower-in', (14, 46), (24, 36), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('left-wing', 'left-upper-in', 'left-upper-out', 'left-shoulder', 'left-lower-out', 'left-lower-base', 'left-lower-in', closed=False)
        self.add_arc('left-antenna', (24, 22), (12, 2), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('right-upper-in', (24, 22), (36, 10), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('right-upper-out', (36, 10), (46, 20), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('right-shoulder', (46, 20), (36, 30), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('right-lower-out', (36, 30), (42, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('right-lower-base', (42, 38), (34, 46), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('right-lower-in', (34, 46), (24, 36), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('right-wing', 'right-upper-in', 'right-upper-out', 'right-shoulder', 'right-lower-out', 'right-lower-base', 'right-lower-in', closed=False)
        self.add_arc('right-antenna', (24, 22), (36, 2), radius_x=20, radius_y=20, sweep=True)
        self.add_line('body', (24, 22), (24, 36))
        self.relate("connect", 'left-wing', 'right-wing')
        self.relate("connect", 'body', 'left-wing')
        self.relate("connect", 'body', 'right-wing')
        self.relate("connect", 'left-antenna', 'right-antenna')
        self.relate("connect", 'left-antenna', 'body')
        self.relate("connect", 'left-antenna', 'left-wing')
        self.relate("connect", 'left-antenna', 'right-wing')
        self.relate("connect", 'right-antenna', 'body')
        self.relate("connect", 'right-antenna', 'left-wing')
        self.relate("connect", 'right-antenna', 'right-wing')
