"""An empty location-pin enclosure with a round crown and a pointed base.

Keyshape VRECT_L: centerline extremes recorded in build below.
Lucide map-pin informs a round crown flowing into paired tapered sides. The supplied reference remains empty; no centre dot is introduced.
Hosting (compose.py): plus invalid, heart invalid, check invalid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (location-marker-pin SQUARE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class LocationMarkerPin(Container64):
    icon_id = 'location-marker-pin'
    keyshape = Keyshape.CIRCLE
    aliases = ('map-pin-container',)
    keywords = ('location', 'marker', 'pin')

    def build(self) -> None:
        self.add_arc('crown-left', (4, 32), (32, 4), radius_x=28)
        self.add_arc('crown-right', (32, 4), (60, 32), radius_x=28)
        self.add_arc('shoulder-right', (60, 32), (51, 45), radius_x=21)
        self.add_arc('neck-right', (51, 45), (32, 60), radius_x=34, sweep=False)
        self.add_arc('neck-left', (32, 60), (13, 45), radius_x=34, sweep=False)
        self.add_arc('shoulder-left', (13, 45), (4, 32), radius_x=21)
        self.add_contour('outline', 'crown-left', 'crown-right', 'shoulder-right', 'neck-right', 'neck-left', 'shoulder-left', closed=True)
