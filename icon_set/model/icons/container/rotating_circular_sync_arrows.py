"""Two curved arrows form an open circular enclosure for synchronization.

Keyshape CIRCLE: radial ink extent 32 around (32,32). The arrowhead ends
reach radius 30 on centerlines; the paired circular arcs use radius 26.
Reference: batch_11 source render; Lucide refresh-cw informs paired arcs with attached arrowheads.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rotating-circular-sync-arrows CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: arcs on r25 (7-24-25 nodes); heads reach r27.8.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RotatingCircularSyncArrows(Container64):
    icon_id = 'rotating-circular-sync-arrows'
    keyshape = Keyshape.CIRCLE
    aliases = ('circular-sync', 'refresh-enclosure')
    keywords = ('rotating', 'circular', 'sync', 'arrows')

    def build(self) -> None:
        # Arcs on r26 about (32,32) (was r25) with shorter heads (5) that stay inside radius 28, so the middle holds
        # a symbol of 24 with a 4 px gap (was 18.5). Point symmetric about the centre.
        self.add_arc('upper', (7, 25), (57, 25), radius_x=26)
        self.add_polyline('upper-head', (52, 25), (57, 25), (57, 20))
        self.relate('connect', 'upper', 'upper-head')
        self.add_arc('lower', (57, 39), (7, 39), radius_x=26)
        self.add_polyline('lower-head', (12, 39), (7, 39), (7, 44))
        self.relate('connect', 'lower', 'lower-head')
