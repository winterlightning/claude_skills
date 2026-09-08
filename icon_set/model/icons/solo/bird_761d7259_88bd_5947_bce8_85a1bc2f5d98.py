"""Right-facing plump songbird with a long tail and two legs; Lucide bird informs circular head and breast. Directional asymmetry preserves the pose."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '761d7259-88bd-5947-bce8-85a1bc2f5d98'
SOURCE_PATH = 'pictographic-primitives/animals/bird_761d7259-88bd-5947-bce8-85a1bc2f5d98.svg'
AUTHOR = 'gpt-6'


class PerchedSongbird(Solo48):
    icon_id = 'perched-songbird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('bird', 'songbird', 'sparrow', 'robin', 'perched', 'wildlife', 'wing', 'garden')

    def build(self) -> None:
        # SQUARE centerline extremes recorded in batch-02-review.md.
        self.add_arc('head-left', (24, 14), (34, 2), radius_x=10, radius_y=12, sweep=True)
        self.add_arc('head-right', (34, 2), (44, 14), radius_x=10, radius_y=12, sweep=True)
        self.add_line('beak-1', (44, 14), (46, 18))
        self.add_line('beak-2', (46, 18), (40, 22))
        self.add_line('breast-neck', (40, 22), (40, 24))
        self.add_arc('breast', (40, 24), (26, 38), radius_x=14, radius_y=14, sweep=True)
        self.add_line('belly', (26, 38), (18, 38))
        self.add_line('tail-1', (18, 38), (2, 34))
        self.add_line('tail-2', (2, 34), (24, 14))
        self.add_contour('outline', 'head-left', 'head-right', 'beak-1', 'beak-2', 'breast-neck', 'breast', 'belly', 'tail-1', 'tail-2', closed=True)
        self.add_arc('wing', (28, 22), (16, 30), radius_x=10, radius_y=10, sweep=True)
        self.add_line('leg-left-1', (18, 38), (18, 46))
        self.add_line('leg-left-2', (18, 46), (14, 46))
        self.add_contour('leg-left', 'leg-left-1', 'leg-left-2', closed=False)
        self.add_line('leg-right-1', (26, 38), (30, 46))
        self.add_line('leg-right-2', (30, 46), (34, 46))
        self.add_contour('leg-right', 'leg-right-1', 'leg-right-2', closed=False)
        self.relate("connect", 'outline', 'leg-left')
        self.relate("connect", 'outline', 'leg-right')
