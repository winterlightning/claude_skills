'Balloon over two unequal temple spires; second balloon and distant temples omitted. Asymmetry retains the scattered landscape.'
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
    category = "landmarks"
    aliases = ()
    keywords = ('bagan', 'myanmar', 'temple', 'pagoda', 'stupa', 'balloon', 'landmark', 'travel', 'skyline')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42).
        self.add_arc("balloon-top", (6,12), (18,12), radius_x=6)
        self.add_arc("balloon-right", (18,12), (12,20), radius_x=6, radius_y=8)
        self.add_arc("balloon-left", (12,20), (6,12), radius_x=6, radius_y=8)
        self.add_contour("balloon", "balloon-top", "balloon-right", "balloon-left", closed=True)
        self.add_polyline("small-temple", (6,42), (6,37), (12,30), (18,37), (18,42))
        self.add_polyline("large-temple", (28,42), (28,32), (35,19), (42,32), (42,42))
