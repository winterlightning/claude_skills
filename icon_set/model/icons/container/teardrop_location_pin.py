"""A convex teardrop map-pin enclosure with a pointed base.

VRECT_L: exact centerline extremes recorded in build.
Construction: Lucide map-pin, mirrored round crown and tapered shoulders; distinct from the existing concave-neck pin. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class TeardropLocationPin(Container64):
    icon_id = 'teardrop-location-pin'
    keyshape = Keyshape.VRECT_L
    aliases = ('map-location-pin-marker',)
    keywords = ('teardrop', 'location', 'pin')

    def build(self) -> None:
        # Centerline (10,2)-(54,62).
        self.add_arc('crown-left',(10,26),(32,2),radius_x=22,radius_y=24)
        self.add_arc('crown-right',(32,2),(54,26),radius_x=22,radius_y=24)
        self.add_arc('shoulder-right',(54,26),(46,46),radius_x=29)
        self.add_line('tip-right',(46,46),(32,62))
        self.add_line('tip-left',(32,62),(18,46))
        self.add_arc('shoulder-left',(18,46),(10,26),radius_x=29)
        self.add_contour('outline','crown-left','crown-right','shoulder-right','tip-right','tip-left','shoulder-left',closed=True)
