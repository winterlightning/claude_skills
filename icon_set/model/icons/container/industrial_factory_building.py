"""A factory enclosure with a central roof peak and paired chimneys.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide factory: one building contour and distinct chimney silhouette; mirrored here to retain the supplied twin-stack subject. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class IndustrialFactoryBuilding(Container64):
    icon_id = 'industrial-factory-building'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('industrial', 'factory', 'building')

    def build(self) -> None:
        self.add_polyline('building', (2,22), (16,22), (32,12), (48,22), (62,22), (62,62), (2,62), closed=True)
        self.add_polyline('left-stack', (5,22), (7,2), (13,2), (15,22))
        self.add_polyline('right-stack', (49,22), (51,2), (57,2), (59,22))
        self.relate('connect', 'building', 'left-stack')
        self.relate('connect', 'building', 'right-stack')
