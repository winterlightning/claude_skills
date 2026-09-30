"""An empty eight-lobed seal with mirrored circular scallops.
The shallow inward cusps define the scallops; no source features removed.

Keyshape CIRCLE; centerline extremes recorded in build below.
Lucide badge informs eight repeated convex arcs joined at inward scallop cusps. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (scalloped-circular-badge CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class ScallopedCircularBadge(Container64):
    icon_id = 'scalloped-circular-badge'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('scalloped', 'circular', 'badge')

    def build(self) -> None:
        self.add_arc('lobe-0', (24, 13), (40, 13), radius_x=8, radius_y=9)
        self.add_arc('lobe-1', (40, 13), (51, 24), radius_x=8)
        self.add_arc('lobe-2', (51, 24), (51, 40), radius_x=9, radius_y=8)
        self.add_arc('lobe-3', (51, 40), (40, 51), radius_x=8)
        self.add_arc('lobe-4', (40, 51), (24, 51), radius_x=8, radius_y=9)
        self.add_arc('lobe-5', (24, 51), (13, 40), radius_x=8)
        self.add_arc('lobe-6', (13, 40), (13, 24), radius_x=9, radius_y=8)
        self.add_arc('lobe-7', (13, 24), (24, 13), radius_x=8)
        self.add_contour('outline', 'lobe-0', 'lobe-1', 'lobe-2', 'lobe-3', 'lobe-4', 'lobe-5', 'lobe-6', 'lobe-7', closed=True)
