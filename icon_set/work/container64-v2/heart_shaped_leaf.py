"""A heart-shaped leaf outline with a short basal stem.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide heart: mirrored lobes and diagonal taper; lobes meet shoulder arcs with vertical tangents. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heart-shaped-leaf SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class HeartShapedLeaf(Container64):
    icon_id = 'heart-shaped-leaf'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('heart', 'shaped', 'leaf')

    def build(self) -> None:
        self.add_arc('outline-0', (32, 16), (20, 6), radius_x=12, radius_y=10, sweep=False)
        self.add_arc('outline-1', (20, 6), (6, 21), radius_x=14, radius_y=15, sweep=False)
        self.add_arc('outline-2', (6, 21), (12, 29), radius_x=9, sweep=False)
        self.add_line('outline-3', (12, 29), (32, 50))
        self.add_line('outline-4', (32, 50), (52, 29))
        self.add_arc('outline-5', (52, 29), (58, 21), radius_x=9, sweep=False)
        self.add_arc('outline-6', (58, 21), (44, 6), radius_x=14, radius_y=15, sweep=False)
        self.add_arc('outline-7', (44, 6), (32, 16), radius_x=12, radius_y=10, sweep=False)
        self.add_line('stem', (32, 50), (32, 58))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.relate('connect', 'outline', 'stem')
