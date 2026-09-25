"""A circular award medallion with two forked ribbon tails; preserve the inset ring when present.

Live VRECT_L bounds: visible (6,2)-(42,46), centerline (8,4)-(40,44)
for VRECT_L; SQUARE uses visible (4,4)-(44,44), centerline (6,6)-(42,42).
Lucide award informs the circular medallion, notched ribbons and mirrored
construction. The supplied reference sets the tail count and rim detail. Geometry authored independently on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7685ddf5-0d1f-5fc0-acbc-eb672c0d3e0c'
SOURCE_PATH = 'pictographic-primitives/rewards/award badge_7685ddf5-0d1f-5fc0-acbc-eb672c0d3e0c.svg'
AUTHOR = 'gpt-6'

class BroadAwardRibbon(Solo48):
    icon_id = 'broad-award-ribbon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('award', 'prize', 'recognition', 'broad-award-ribbon')

    def build(self) -> None:
        axis = 24
        self.add_arc('disc-top', (11,17), (37,17), radius_x=13)
        self.add_arc('disc-right', (37,17), (36,22), radius_x=13)
        self.add_arc('disc-bottom', (36,22), (12,22), radius_x=13)
        self.add_arc('disc-left', (12,22), (11,17), radius_x=13)
        self.add_contour('disc', 'disc-top', 'disc-right', 'disc-bottom', 'disc-left', closed=True)
        for side, sign in [('left', -1), ('right', 1)]:
            def pt(x, y): return (axis + sign*x, y)
            self.add_polyline(side+'-ribbon', pt(12,22), pt(16,38), pt(9,38), pt(6,44), pt(0,30))
            self.relate('connect', 'disc', side+'-ribbon')
        self.relate('connect', 'left-ribbon', 'right-ribbon')

