"""Two curved arrows form an open circular enclosure for synchronization.

Keyshape CIRCLE: radial ink extent 32 around (32,32). The arrowhead ends
reach radius 30 on centerlines; the paired circular arcs use radius 26.
Reference: batch_11 source render; Lucide refresh-cw informs paired arcs with attached arrowheads.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart does not clear, check does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class RotatingCircularSyncArrows(Container64):
    icon_id = 'rotating-circular-sync-arrows'
    keyshape = Keyshape.CIRCLE
    aliases = ('circular-sync', 'refresh-enclosure')
    keywords = ('rotating', 'circular', 'sync', 'arrows')

    def build(self) -> None:
        self.add_arc('upper', (8, 22), (56, 22), radius_x=26, radius_y=26, sweep=True, large_arc=False)
        self.add_polyline('upper-head', (46, 20), (56, 22), (56, 14), closed=False)
        self.relate("connect", 'upper', 'upper-head')
        self.add_arc('lower', (56, 42), (8, 42), radius_x=26, radius_y=26, sweep=True, large_arc=False)
        self.add_polyline('lower-head', (18, 44), (8, 42), (8, 50), closed=False)
        self.relate("connect", 'lower', 'lower-head')
