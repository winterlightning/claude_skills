"""An open panoramic enclosure with curved rims and inward-facing side panels.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide cylinder uses elliptical rims and vertical walls.
Mirrored panels preserve the open wraparound view; the detached rear rim remains separate.
Hosting measured with compose.py: plus: does not clear; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class PanoramicCylindricalView(Container64):
    icon_id = 'panoramic-cylindrical-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('panoramic', 'cylindrical', 'view')

    def build(self) -> None:
        self.add_arc('rear-rim', (2, 12), (62, 12), radius_x=30, radius_y=10, sweep=True)
        self.add_line('left-wall', (2, 20), (2, 52))
        self.add_arc('bottom-left', (2, 52), (32, 62), radius_x=30, radius_y=10, sweep=False)
        self.add_arc('bottom-right', (32, 62), (62, 52), radius_x=30, radius_y=10, sweep=False)
        self.add_line('right-wall', (62, 52), (62, 20))
        self.add_contour('outer', 'left-wall', 'bottom-left', 'bottom-right', 'right-wall', closed=False)
        self.add_polyline('left-return', (2, 20), (14, 24), (14, 60), closed=False)
        self.add_polyline('right-return', (62, 20), (50, 24), (50, 60), closed=False)
        self.relate("connect", 'outer', 'left-return')
        self.relate("connect", 'outer', 'right-return')
