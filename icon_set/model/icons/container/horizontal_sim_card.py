"""A blank SIM-card enclosure with a clipped upper-right corner.

HRECT_XL: visible bounds (0, 4, 64, 60); chosen for the source proportions.
Construction reference: Lucide card-sim: clipped corner and rounded remaining corners; asymmetry identifies orientation. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (horizontal-sim-card HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class HorizontalSimCard(Container64):
    icon_id = 'horizontal-sim-card'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('horizontal', 'sim', 'card')

    def build(self) -> None:
        self.add_line('outline-0', (8, 10), (47, 10))
        self.add_line('outline-1', (47, 10), (60, 22))
        self.add_line('outline-2', (60, 22), (60, 50))
        self.add_arc('outline-3', (60, 50), (56, 54), radius_x=4)
        self.add_line('outline-4', (56, 54), (8, 54))
        self.add_arc('outline-5', (8, 54), (4, 50), radius_x=4)
        self.add_line('outline-6', (4, 50), (4, 14))
        self.add_arc('outline-7', (4, 14), (8, 10), radius_x=4)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
