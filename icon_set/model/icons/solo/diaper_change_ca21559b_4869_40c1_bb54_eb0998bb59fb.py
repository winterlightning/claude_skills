"""An adult bends toward a supine baby on a changing surface; one arm and leg replace the overlapping source limbs. Deliberate side-view asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca21559b-4869-40c1-bb54-eb0998bb59fb'
SOURCE_PATH = 'pictographic-primitives/babies/family baby change diaper_ca21559b-4869-40c1-bb54-eb0998bb59fb.svg'
AUTHOR = 'gpt-6'


class DiaperChange(Solo48):
    icon_id = 'diaper-change'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('diaper', 'change', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('adult-head-top', (21, 7), (31, 7), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('adult-head-bottom', (31, 7), (21, 7), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('adult-head', 'adult-head-top', 'adult-head-bottom', closed=True)
        self.add_polyline('adult-back', (17, 16), (9, 24), (2, 36), (15, 36))
        self.add_line('adult-leg', (10, 36), (10, 46))
        self.relate("connect", 'adult-back', 'adult-leg')
        self.add_polyline('adult-arm', (17, 16), (20, 26), (23, 32))
        self.relate("connect", 'adult-back', 'adult-arm')
        self.add_arc('baby-head-top', (40, 33), (46, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('baby-head-bottom', (46, 33), (40, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('baby-head', 'baby-head-top', 'baby-head-bottom', closed=True)
        self.add_polyline('baby-body', (23, 32), (27, 38), (33, 38), (33, 31))
        self.relate("connect", 'adult-arm', 'baby-body')
        self.add_line('surface', (22, 46), (46, 46))
