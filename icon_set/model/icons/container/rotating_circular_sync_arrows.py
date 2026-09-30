"""Two curved arrows form an open circular enclosure for synchronization.

Keyshape CIRCLE: radial ink extent 32 around (32,32). The arrowhead ends
reach radius 30 on centerlines; the paired circular arcs use radius 26.
Reference: batch_11 source render; Lucide refresh-cw informs paired arcs with attached arrowheads.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rotating-circular-sync-arrows CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: arcs on r25 (7-24-25 nodes); heads reach r27.8.
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
        self.add_arc('upper', (8, 25), (56, 25), radius_x=25)
        self.add_polyline('upper-head', (46, 23), (56, 25), (56, 18))
        self.relate('connect', 'upper', 'upper-head')
        self.add_arc('lower', (56, 39), (8, 39), radius_x=25)
        self.add_polyline('lower-head', (18, 41), (8, 39), (8, 46))
        self.relate('connect', 'lower', 'lower-head')
