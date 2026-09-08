"""One balloon above an uneven pagoda skyline. Second balloon and extra temples omitted; asymmetry preserves the scattered landscape."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0527e64-26b6-5f5c-bdf2-bed6763e0653'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/bagan_e0527e64-26b6-5f5c-bdf2-bed6763e0653.svg'
AUTHOR = 'gpt-6'

class BaganTemplePlain(Solo48):
    icon_id = 'bagan-temple-plain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('bagan', 'myanmar', 'temple', 'pagoda', 'stupa', 'balloon', 'landmark', 'travel', 'skyline')

    def build(self) -> None:
        # Centerline extremes (2, 2, 46, 46).
        self.add_arc("balloon-top", (2,9), (16,9), radius_x=7)
        self.add_arc("balloon-bottom", (16,9), (9,20), radius_x=7, radius_y=11)
        self.add_arc("balloon-return", (9,20), (2,9), radius_x=7, radius_y=11)
        self.add_contour("balloon", "balloon-top", "balloon-bottom", "balloon-return", closed=True)
        self.add_polyline("temple-left", (2,46), (2,39), (10,29), (18,39), (18,46))
        self.add_polyline("temple-middle", (28,46), (28,33), (37,18), (46,33), (46,46))
