"""A cylindrical metal can with an oval rim and curved base.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide cylinder: elliptical rim and straight sides; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (metal-tin-can VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class MetalTinCan(Container64):
    icon_id = 'metal-tin-can'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('metal', 'tin', 'can')

    def build(self) -> None:
        self.add_arc('rim-0', (12, 12), (52, 12), radius_x=20, radius_y=8)
        self.add_arc('rim-1', (52, 12), (12, 12), radius_x=20, radius_y=8)
        self.add_line('body-0', (52, 12), (52, 52))
        self.add_arc('body-1', (52, 52), (12, 52), radius_x=20, radius_y=8)
        self.add_line('body-2', (12, 52), (12, 12))
        self.add_contour('rim', 'rim-0', 'rim-1', closed=True)
        self.add_contour('body', 'body-0', 'body-1', 'body-2')
        self.relate('connect', 'rim', 'body')
