"""Dominant stupa above three smaller spired stupas. Fine stepped collars and plinth outlines omitted."""
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
        # Centerline extremes (2, 2, 46, 46).
        self.add_line("spire", (24,2), (24,8))
        self.add_arc("dome-left", (15,20), (24,8), radius_x=9, radius_y=12)
        self.add_arc("dome-right", (24,8), (33,20), radius_x=9, radius_y=12)
        self.add_contour("dome", "dome-left", "dome-right")
        self.add_line("terrace", (15,20), (33,20))
        self.relate("connect", "dome", "terrace")
        self.relate("connect", "spire", "dome")
        for x in (7,24,41):
            self.add_line(f"left-{x}", (x-5,46), (x-5,40))
            self.add_arc(f"cap-left-{x}", (x-5,40), (x,35), radius_x=5)
            self.add_arc(f"cap-right-{x}", (x,35), (x+5,40), radius_x=5)
            self.add_line(f"right-{x}", (x+5,40), (x+5,46))
            self.add_contour(f"small-{x}", f"left-{x}", f"cap-left-{x}", f"cap-right-{x}", f"right-{x}")
            self.add_line(f"finial-{x}", (x,30), (x,35))
            self.relate("connect", f"small-{x}", f"finial-{x}")
