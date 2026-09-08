"""Two bowls and mirrored water arcs; narrow pedestal outline reduced to a stem."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb3d2ef1-d2d9-4a31-8b38-63acceae3fbc'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/park fonutain_bb3d2ef1-d2d9-4a31-8b38-63acceae3fbc.svg'
AUTHOR = 'gpt-6'

class TieredWaterFountain(Solo48):
    icon_id = 'tiered-water-fountain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('fountain', 'water', 'park', 'plaza', 'jet', 'basin', 'garden', 'landmark')

    def build(self) -> None:
        # Centerline extremes (2, 2, 46, 46).
        self.add_arc("jet-left", (8,10), (24,10), radius_x=8)
        self.add_arc("jet-right", (24,10), (40,10), radius_x=8)
        self.add_line("water", (24,10), (24,18))
        self.relate("connect", "jet-left", "jet-right")
        self.relate("connect", "jet-left", "water")
        self.relate("connect", "jet-right", "water")
        self.add_arc("upper-left", (12,18), (24,24), radius_x=12, radius_y=6, sweep=False)
        self.add_arc("upper-right", (24,24), (36,18), radius_x=12, radius_y=6, sweep=False)
        self.add_line("upper-rim-1", (36, 18), (24, 18))
        self.add_line("upper-rim-2", (24, 18), (12, 18))
        self.add_contour("upper", "upper-left", "upper-right", "upper-rim-1", "upper-rim-2", closed=True)
        self.relate("connect", "water", "upper")
        self.add_line("stem", (24,24), (24,32))
        self.relate("connect", "stem", "upper")
        self.add_arc("lower-left", (2,32), (24,40), radius_x=22, radius_y=8, sweep=False)
        self.add_arc("lower-right", (24,40), (46,32), radius_x=22, radius_y=8, sweep=False)
        self.add_line("lower-rim-1", (46, 32), (24, 32))
        self.add_line("lower-rim-2", (24, 32), (2, 32))
        self.add_contour("lower", "lower-left", "lower-right", "lower-rim-1", "lower-rim-2", closed=True)
        self.relate("connect", "stem", "lower")
        self.add_line("foot", (24,40), (24,46))
        self.relate("connect", "foot", "lower")
