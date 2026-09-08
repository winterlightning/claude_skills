"""A blank SIM-card enclosure with a clipped upper-right corner.

HRECT_XL: visible bounds (0, 4, 64, 60); chosen for the source proportions.
Construction reference: Lucide card-sim: clipped corner and rounded remaining corners; asymmetry identifies orientation. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HorizontalSimCard(Container64):
    icon_id = 'horizontal-sim-card'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('horizontal', 'sim', 'card')

    def build(self) -> None:
        self.add_line('outline-0', (6, 6), (48, 6))
        self.add_line('outline-1', (48, 6), (62, 20))
        self.add_line('outline-2', (62, 20), (62, 54))
        self.add_arc('outline-3', (62, 54), (58, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-4', (58, 58), (6, 58))
        self.add_arc('outline-5', (6, 58), (2, 54), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-6', (2, 54), (2, 10))
        self.add_arc('outline-7', (2, 10), (6, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
