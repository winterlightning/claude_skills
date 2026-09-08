"""A folded booklet shows a rectangular front and a sloping rear page above it.

VRECT_M: visible bounds (12, 0, 52, 64), chosen for the subject proportions.
Lucide panels-top-left: shared enclosure edges and attached panel boundaries; original and atomic-debug inspected.
Perspective asymmetry and the triangular rear page retained; no features dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SimpleFoldedBooklet(Container64):
    icon_id = 'simple-folded-booklet'
    keyshape = Keyshape.VRECT_M
    aliases = ('folded-booklet',)
    keywords = ('simple', 'folded', 'booklet')

    def build(self) -> None:
        self.add_polyline('front', (14, 14), (50, 14), (50, 62), (14, 62), closed=True)
        self.add_polyline('rear', (14, 14), (46, 2), (46, 14), closed=False)
        self.relate("connect", 'front', 'rear')
