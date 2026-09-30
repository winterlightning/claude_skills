"""A factory enclosure with a central roof peak and paired chimneys.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide factory: one building contour and distinct chimney silhouette; mirrored here to retain the supplied twin-stack subject. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (industrial-factory-building SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class IndustrialFactoryBuilding(Container64):
    icon_id = 'industrial-factory-building'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('industrial', 'factory', 'building')

    def build(self) -> None:
        self.add_line('building-1', (6, 24), (20, 24))
        self.add_line('building-2', (20, 24), (32, 15))
        self.add_line('building-3', (32, 15), (44, 24))
        self.add_line('building-4', (44, 24), (58, 24))
        self.add_line('building-5', (58, 24), (58, 58))
        self.add_line('building-6', (58, 58), (6, 58))
        self.add_line('building-7', (6, 58), (6, 24))
        self.add_line('left-stack-1', (9, 24), (11, 6))
        self.add_line('left-stack-2', (11, 6), (17, 6))
        self.add_line('left-stack-3', (17, 6), (19, 24))
        self.add_line('right-stack-1', (45, 24), (47, 6))
        self.add_line('right-stack-2', (47, 6), (53, 6))
        self.add_line('right-stack-3', (53, 6), (55, 24))
        self.add_contour('building', 'building-1', 'building-2', 'building-3', 'building-4', 'building-5', 'building-6', 'building-7', closed=True)
        self.add_contour('left-stack', 'left-stack-1', 'left-stack-2', 'left-stack-3')
        self.add_contour('right-stack', 'right-stack-1', 'right-stack-2', 'right-stack-3')
        self.relate('connect', 'building', 'left-stack')
        self.relate('connect', 'building', 'right-stack')
