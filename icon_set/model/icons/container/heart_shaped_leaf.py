"""A heart-shaped leaf outline with a short basal stem.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide heart: mirrored lobes and diagonal taper; lobes meet shoulder arcs with vertical tangents. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heart-shaped-leaf SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-redrawn after review: r17 lobes (r18 below the widest point so the side stays inside the envelope) with V sides tangent within 1.5 degrees at (12,36)-(32,53) and quarter-ellipse dips, so the centerline has no kinks; the symbol area grows from 15.5 to a 22-unit square.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class HeartShapedLeaf(Container64):
    icon_id = 'heart-shaped-leaf'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('heart', 'shaped', 'leaf')

    def build(self) -> None:
        self.add_arc('outline-0', (32, 12), (23, 6), radius_x=9, radius_y=6, sweep=False)
        self.add_arc('outline-1', (23, 6), (6, 23), radius_x=17, sweep=False)
        self.add_arc('outline-2', (6, 23), (12, 36), radius_x=18, sweep=False)
        self.add_line('outline-3', (12, 36), (32, 53))
        self.add_line('outline-4', (32, 53), (52, 36))
        self.add_arc('outline-5', (52, 36), (58, 23), radius_x=18, sweep=False)
        self.add_arc('outline-6', (58, 23), (41, 6), radius_x=17, sweep=False)
        self.add_arc('outline-7', (41, 6), (32, 12), radius_x=9, radius_y=6, sweep=False)
        self.add_line('stem', (32, 53), (32, 58))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.relate('connect', 'outline', 'stem')
