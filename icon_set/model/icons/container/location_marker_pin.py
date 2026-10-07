"""An empty location-pin enclosure with a round crown and a pointed base.

Keyshape VRECT_L: centerline extremes recorded in build below.
Lucide map-pin informs a round crown flowing into paired tapered sides. The supplied reference remains empty; no centre dot is introduced.
Hosting (compose.py): plus invalid, heart invalid, check invalid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (location-marker-pin SQUARE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn as a real map pin. The v2 body was as wide as it was tall with a short point and read as a
shell. Now a round crown r24 centred (32, 28) whose sides leave it vertically and taper as cubics to the point (32, 60),
the Lucide map-pin outline: 48 wide, 56 tall. Symbol room 25 (was 26), still a symbol 24.
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
        self.add_arc('crown-left', (8, 28), (32, 4), radius_x=24)
        self.add_arc('crown-right', (32, 4), (56, 28), radius_x=24)
        self.add_bezier('side-right', (56, 28), ((56, 41.5), (39.4, 55.6), (32, 60)))
        self.add_bezier('side-left', (32, 60), ((24.6, 55.6), (8, 41.5), (8, 28)))
        self.add_contour('outline', 'crown-left', 'crown-right', 'side-right', 'side-left', closed=True)
