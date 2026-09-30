"""A folded booklet shows a rectangular front and a sloping rear page above it.

VRECT_M: visible bounds (12, 0, 52, 64), chosen for the subject proportions.
Lucide panels-top-left: shared enclosure edges and attached panel boundaries; original and atomic-debug inspected.
Perspective asymmetry and the triangular rear page retained; no features dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-folded-booklet VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleFoldedBooklet(Container64):
    icon_id = 'simple-folded-booklet'
    keyshape = Keyshape.VRECT_M
    aliases = ('folded-booklet',)
    keywords = ('simple', 'folded', 'booklet')

    def build(self) -> None:
        self.add_line('front-1', (12, 15), (52, 15))
        self.add_line('front-2', (52, 15), (52, 60))
        self.add_line('front-3', (52, 60), (12, 60))
        self.add_line('front-4', (12, 60), (12, 15))
        self.add_line('rear-1', (12, 15), (44, 4))
        self.add_line('rear-2', (44, 4), (44, 15))
        self.add_contour('front', 'front-1', 'front-2', 'front-3', 'front-4', closed=True)
        self.add_contour('rear', 'rear-1', 'rear-2')
        self.relate('connect', 'front', 'rear')
