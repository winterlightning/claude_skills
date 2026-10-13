"""A heart-shaped leaf outline with a short basal stem.

SQUARE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide heart: mirrored lobes and diagonal taper; lobes meet shoulder arcs with vertical tangents. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heart-shaped-leaf SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-redrawn after review: r17 lobes (r18 below the widest point so the side stays inside the envelope) with V sides tangent within 1.5 degrees at (12,36)-(32,53) and quarter-ellipse dips, so the centerline has no kinks; the symbol area grows from 15.5 to a 22-unit square.

v3 (2026-10-07): redrawn as a full cordate leaf with Bezier sides so a container symbol has room: 22-unit square with a 4 px gap, up from 10 at the old placement.
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
        # Cordate leaf: notch (32,12), lobe top (19,6) with a horizontal tangent, widest point (6,26) with a vertical
        # tangent, tip (32,53) and a short stem to 58; the right half mirrors the left about x = 32. The full lower
        # body leaves a symbol square of 22 (4 px gap) around (32,29); the old V heart left 10 to 18.
        self.add_bezier('outline-left', (32, 12),
                        ((31, 8), (25, 6), (19, 6)),
                        ((11.8, 6), (6, 14.5), (6, 26)),
                        ((6, 42), (20, 47), (32, 53)))
        self.add_bezier('outline-right', (32, 53),
                        ((44, 47), (58, 42), (58, 26)),
                        ((58, 14.5), (52.2, 6), (45, 6)),
                        ((39, 6), (33, 8), (32, 12)))
        self.add_line('stem', (32, 53), (32, 58))
        self.add_contour('outline', 'outline-left', 'outline-right', closed=True)
        self.relate('connect', 'outline', 'stem')
