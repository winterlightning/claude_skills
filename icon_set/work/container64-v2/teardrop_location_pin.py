"""A convex teardrop map-pin enclosure with a pointed base.

VRECT_L: exact centerline extremes recorded in build.
Construction: Lucide map-pin, mirrored round crown and tapered shoulders; distinct from the existing concave-neck pin. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (teardrop-location-pin SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class TeardropLocationPin(Container64):
    icon_id = 'teardrop-location-pin'
    keyshape = Keyshape.SQUARE
    aliases = ('map-location-pin-marker',)
    keywords = ('teardrop', 'location', 'pin')

    def build(self) -> None:
        self.add_arc('crown-left', (6, 27), (32, 6), radius_x=26, radius_y=21)
        self.add_arc('crown-right', (32, 6), (58, 27), radius_x=26, radius_y=21)
        self.add_arc('shoulder-right', (58, 27), (49, 45), radius_x=35)
        self.add_line('tip-right', (49, 45), (32, 58))
        self.add_line('tip-left', (32, 58), (15, 45))
        self.add_arc('shoulder-left', (15, 45), (6, 27), radius_x=35)
        self.add_contour('outline', 'crown-left', 'crown-right', 'shoulder-right', 'tip-right', 'tip-left', 'shoulder-left', closed=True)
