"""A trapezoidal calibration weight enclosure with an arched handle.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide weight: centered circular handle above sloping body. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HeavyScaleMeasurementWeight(Container64):
    icon_id = 'heavy-scale-measurement-weight'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('heavy', 'scale', 'measurement', 'weight')

    def build(self) -> None:
        self.add_line('outline-0', (14, 18), (50, 18))
        self.add_arc('outline-1', (50, 18), (54, 22), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-2', (54, 22), (62, 58))
        self.add_arc('outline-3', (62, 58), (58, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-4', (58, 62), (6, 62))
        self.add_arc('outline-5', (6, 62), (2, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-6', (2, 58), (10, 22))
        self.add_arc('outline-7', (10, 22), (14, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_arc('handle', (24, 18), (40, 18), radius_x=10, large_arc=True, sweep=True)
        self.relate('connect','outline','handle')
