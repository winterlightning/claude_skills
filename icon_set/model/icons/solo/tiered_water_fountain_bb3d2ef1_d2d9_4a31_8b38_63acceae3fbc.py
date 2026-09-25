'Two open bowls and mirrored water jets; bowl rims removed to avoid narrow enclosed slivers, pedestal reduced to a stem.'
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
    category = "landmarks"
    aliases = ()
    keywords = ('fountain', 'water', 'park', 'plaza', 'jet', 'basin', 'garden', 'landmark')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42), common axis 24.
        self.add_arc("jet-left", (12,12), (24,12), radius_x=6)
        self.add_arc("jet-right", (24,12), (36,12), radius_x=6)
        self.add_line("water", (24,12), (24,27))
        for part in ("jet-left","jet-right"):
            self.relate("connect", part, "water")
        self.relate("connect", "jet-left", "jet-right")
        self.add_arc("upper-left", (12,21), (24,27), radius_x=12, radius_y=6, sweep=False)
        self.add_arc("upper-right", (24,27), (36,21), radius_x=12, radius_y=6, sweep=False)
        self.add_contour("upper", "upper-left", "upper-right")
        self.relate("connect", "water", "upper")
        self.add_line("stem", (24,27), (24,39))
        self.relate("connect", "stem", "upper")
        self.relate("connect", "stem", "water")
        self.add_arc("lower-left", (6,33), (24,39), radius_x=18, radius_y=6, sweep=False)
        self.add_arc("lower-right", (24,39), (42,33), radius_x=18, radius_y=6, sweep=False)
        self.add_contour("lower", "lower-left", "lower-right")
        self.relate("connect", "stem", "lower")
        self.add_line("foot", (24,39), (24,42))
        self.relate("connect", "foot", "lower")
        self.relate("connect", "foot", "stem")
