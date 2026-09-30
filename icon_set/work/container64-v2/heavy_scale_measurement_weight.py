"""A trapezoidal calibration weight enclosure with an arched handle.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide weight: centered circular handle above sloping body. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heavy-scale-measurement-weight SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class HeavyScaleMeasurementWeight(Container64):
    icon_id = 'heavy-scale-measurement-weight'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('heavy', 'scale', 'measurement', 'weight')

    def build(self) -> None:
        self.add_line('outline-0', (18, 20), (46, 20))
        self.add_arc('outline-1', (46, 20), (50, 24), radius_x=4)
        self.add_line('outline-2', (50, 24), (58, 54))
        self.add_arc('outline-3', (58, 54), (54, 58), radius_x=4)
        self.add_line('outline-4', (54, 58), (10, 58))
        self.add_arc('outline-5', (10, 58), (6, 54), radius_x=4)
        self.add_line('outline-6', (6, 54), (14, 24))
        self.add_arc('outline-7', (14, 24), (18, 20), radius_x=4)
        self.add_arc('handle', (24, 22), (40, 22), radius_x=10, large_arc=True)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.relate('connect', 'outline', 'handle')
