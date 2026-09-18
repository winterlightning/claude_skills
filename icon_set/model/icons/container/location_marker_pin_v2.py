# Variant of location-marker-pin; parent file remains unchanged.
"""An empty location-pin enclosure with a round crown and a pointed base.

Keyshape VRECT_L: centerline extremes recorded in build below.
Lucide map-pin informs a round crown flowing into paired tapered sides. The supplied reference remains empty; no centre dot is introduced.
Hosting (compose.py): plus invalid, heart invalid, check invalid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class LocationMarkerPinVariant2(Container64):
    icon_id = 'location-marker-pin-v2'
    variant_of = 'location-marker-pin'
    variant_label = 'Wider content area'
    keyshape = Keyshape.SQUARE
    aliases = ('map-pin-container',)
    keywords = ('location', 'marker', 'pin')

    def build(self) -> None:
        self.add_arc('crown-left', (2, 32), (32, 2), radius_x=30)
        self.add_arc('crown-right', (32, 2), (62, 32), radius_x=30)
        self.add_arc('shoulder-right', (62, 32), (52, 46), radius_x=22)
        self.add_arc('neck-right', (52, 46), (32, 62), radius_x=37, sweep=False)
        self.add_arc('neck-left', (32, 62), (12, 46), radius_x=37, sweep=False)
        self.add_arc('shoulder-left', (12, 46), (2, 32), radius_x=22)
        self.add_contour('outline', 'crown-left', 'crown-right', 'shoulder-right', 'neck-right', 'neck-left', 'shoulder-left', closed=True)
