"""An empty location-pin enclosure with a round crown and a pointed base.

Keyshape VRECT_L: centerline extremes recorded in build below.
Lucide map-pin informs a round crown flowing into paired tapered sides. The supplied reference remains empty; no centre dot is introduced.
Hosting (compose.py): plus invalid, heart invalid, check invalid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class LocationMarkerPin(Container64):
    icon_id = 'location-marker-pin'
    keyshape = Keyshape.VRECT_L
    aliases = ('map-pin-container',)
    keywords = ('location', 'marker', 'pin')

    def build(self) -> None:
        # VRECT_L centerline extremes: (10,2)-(54,62).
        self.add_arc("crown-left", (10,24), (32,2), radius_x=22)
        self.add_arc("crown-right", (32,2), (54,24), radius_x=22)
        # Circular shoulders leave the crown vertically. Their 3:4:5 end
        # tangents flow into reverse-curved necks (under 0.1 degree mismatch
        # after choosing integer radii), retaining the reference's bulb.
        self.add_arc("shoulder-right", (54,24), (46,40), radius_x=20)
        self.add_arc("neck-right", (46,40), (32,62), radius_x=37, sweep=False)
        self.add_arc("neck-left", (32,62), (18,40), radius_x=37, sweep=False)
        self.add_arc("shoulder-left", (18,40), (10,24), radius_x=20)
        self.add_contour("outline", "crown-left", "crown-right", "shoulder-right", "neck-right", "neck-left", "shoulder-left", closed=True)
