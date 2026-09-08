"""A heart-shaped leaf outline with a short basal stem.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide heart: mirrored lobes and diagonal taper; lobes meet shoulder arcs with vertical tangents. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HeartShapedLeaf(Container64):
    icon_id = 'heart-shaped-leaf'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('heart', 'shaped', 'leaf')

    def build(self) -> None:
        self.add_arc('outline-0', (32, 12), (17, 2), radius_x=15, radius_y=10, sweep=False)
        self.add_arc('outline-1', (17, 2), (2, 17), radius_x=15, radius_y=15, sweep=False)
        self.add_arc('outline-2', (2, 17), (8, 29), radius_x=15, radius_y=15, sweep=False)
        self.add_line('outline-3', (8, 29), (32, 54))
        self.add_line('outline-4', (32, 54), (56, 29))
        self.add_arc('outline-5', (56, 29), (62, 17), radius_x=15, radius_y=15, sweep=False)
        self.add_arc('outline-6', (62, 17), (47, 2), radius_x=15, radius_y=15, sweep=False)
        self.add_arc('outline-7', (47, 2), (32, 12), radius_x=15, radius_y=10, sweep=False)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_line('stem',(32,54),(32,62))
        self.relate('connect','outline','stem')
