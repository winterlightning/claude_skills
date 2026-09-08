"""A landscape certificate frame has four inward curved corner holders.

Keyshape HRECT_L: visible bounds (0, 8, 64, 56).
Lucide frame informs the orthogonal boundary; source supplies the quarter-circle
corner holders. Centerline extremes (2,10)-(62,54). All holders are radius 12
and mirrored across both axes; no detail removed.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class FramedAchievementCertificate(Container64):
    icon_id = 'framed-achievement-certificate'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('certificate-frame',)
    keywords = ('certificate', 'achievement', 'frame', 'document')

    def build(self) -> None:
        self.add_polyline('frame', (2, 10), (62, 10), (62, 54), (2, 54), closed=True)
        self.add_arc('holder-nw', (14, 10), (2, 22), radius_x=12, radius_y=12, sweep=True)
        self.relate("connect", 'frame', 'holder-nw')
        self.add_arc('holder-ne', (62, 22), (50, 10), radius_x=12, radius_y=12, sweep=True)
        self.relate("connect", 'frame', 'holder-ne')
        self.add_arc('holder-se', (50, 54), (62, 42), radius_x=12, radius_y=12, sweep=True)
        self.relate("connect", 'frame', 'holder-se')
        self.add_arc('holder-sw', (2, 42), (14, 54), radius_x=12, radius_y=12, sweep=True)
        self.relate("connect", 'frame', 'holder-sw')
