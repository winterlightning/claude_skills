"""A circular badge above one broad notched ribbon.

Live VRECT_L bounds: visible (6,2)-(42,46), centerline (8,4)-(40,44)
for VRECT_L; SQUARE uses visible (4,4)-(44,44), centerline (6,6)-(42,42).
Lucide award informs the circular medallion, notched ribbons and mirrored
construction. The supplied reference sets the tail count and rim detail. Geometry authored independently on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e2ed51b-8309-4e10-861b-a51459770e84'
SOURCE_PATH = 'pictographic-primitives/rewards/badge_4e2ed51b-8309-4e10-861b-a51459770e84.svg'
AUTHOR = 'gpt-6'

class SingleTailAwardBadge(Solo48):
    icon_id = 'single-tail-award-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'state')
    aliases = ()
    keywords = ('award', 'prize', 'recognition', 'single-tail-award-badge')

    def build(self) -> None:
        self.add_arc('upper', (8,16), (40,16), radius_x=16, radius_y=12)
        self.add_arc('lower-right', (40,16), (36,24), radius_x=16, radius_y=13)
        self.add_arc('lower', (36,24), (12,24), radius_x=16, radius_y=12)
        self.add_arc('lower-left', (12,24), (8,16), radius_x=16, radius_y=13)
        self.add_contour('disc', 'upper', 'lower-right', 'lower', 'lower-left', closed=True)
        self.add_polyline('ribbon', (12,24), (12,44), (24,36), (36,44), (36,24))
        self.relate('connect','disc','ribbon')
