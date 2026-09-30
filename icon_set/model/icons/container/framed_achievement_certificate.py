"""A landscape certificate frame has four inward curved corner holders.

Keyshape HRECT_L: visible bounds (0, 8, 64, 56).
Lucide frame informs the orthogonal boundary; source supplies the quarter-circle
corner holders. Centerline extremes (2,10)-(62,54). All holders are radius 12
and mirrored across both axes; no detail removed.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (framed-achievement-certificate HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class FramedAchievementCertificate(Container64):
    icon_id = 'framed-achievement-certificate'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('certificate-frame',)
    keywords = ('certificate', 'achievement', 'frame', 'document')

    def build(self) -> None:
        self.add_line('frame-1', (4, 12), (60, 12))
        self.add_line('frame-2', (60, 12), (60, 52))
        self.add_line('frame-3', (60, 52), (4, 52))
        self.add_line('frame-4', (4, 52), (4, 12))
        self.add_arc('holder-nw', (15, 12), (4, 23), radius_x=11)
        self.add_arc('holder-ne', (60, 23), (49, 12), radius_x=11)
        self.add_arc('holder-se', (49, 52), (60, 41), radius_x=11)
        self.add_arc('holder-sw', (4, 41), (15, 52), radius_x=11)
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', 'frame-4', closed=True)
        self.relate('connect', 'frame', 'holder-nw')
        self.relate('connect', 'frame', 'holder-ne')
        self.relate('connect', 'frame', 'holder-se')
        self.relate('connect', 'frame', 'holder-sw')
