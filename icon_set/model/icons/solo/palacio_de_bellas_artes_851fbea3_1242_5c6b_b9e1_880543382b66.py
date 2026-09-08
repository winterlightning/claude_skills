"""Palacio de bellas artes: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '851fbea3-1242-5c6b-b9e1-880543382b66'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/bellas artes palace mexico_851fbea3-1242-5c6b-b9e1-880543382b66.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'palacio-de-bellas-artes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('bellas artes', 'palace', 'mexico', 'theatre', 'dome', 'landmark', 'architecture', 'museum')

    def build(self):
        # Centerline extremes: (2,2)-(46,46); stepped wings and dome.
        self.add_polyline("outline", (2,46), (2,30), (12,30), (12,20), (14,20), (24,20), (34,20), (36,20), (36,30), (46,30), (46,46), (30,46), (18,46), closed=True)
        self.add_arc("dome-left", (14,20), (24,10), radius_x=10)
        self.add_arc("dome-right", (24,10), (34,20), radius_x=10)
        self.add_contour("dome", "dome-left", "dome-right")
        self.add_line("finial", (24,2), (24,10))
        self.relate("connect", "finial", "dome")
        self.relate("connect", "dome", "outline")
        self.add_line("door-left", (18, 46), (18, 36))
        self.add_arc("door-top", (18, 36), (30, 36), radius_x=6)
        self.add_line("door-right", (30, 36), (30, 46))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
