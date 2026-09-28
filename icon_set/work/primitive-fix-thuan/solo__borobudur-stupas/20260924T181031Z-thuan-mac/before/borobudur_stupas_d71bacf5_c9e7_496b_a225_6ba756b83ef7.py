'One dominant stupa above three small matching stupas. Tier bands and enclosed bases omitted to preserve the four-monument arrangement.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd71bacf5-c9e7-496b-a225-6ba756b83ef7'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/chandi borobudur_d71bacf5-c9e7-496b-a225-6ba756b83ef7.svg'
AUTHOR = 'gpt-6'

class BorobudurStupas(Solo48):
    icon_id = 'borobudur-stupas'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('borobudur', 'indonesia', 'stupa', 'temple', 'buddhist', 'landmark', 'monument', 'heritage')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42); centered repeated foreground.
        self.add_line("spire", (24,6), (24,12))
        self.add_arc("dome-left", (16,20), (24,12), radius_x=8)
        self.add_arc("dome-right", (24,12), (32,20), radius_x=8)
        self.add_line("terrace", (32,20), (16,20))
        self.add_contour("dome", "dome-left", "dome-right", "terrace", closed=True)
        self.relate("connect", "spire", "dome")
        for x in (9,24,39):
            self.add_polyline(f"small-{x}", (x-3,42), (x,33), (x+3,42))
            self.add_line(f"finial-{x}", (x,29), (x,33))
            self.relate("connect", f"small-{x}", f"finial-{x}")
