"""A rounded storage jar with an open flared neck.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide cylinder: vessel outline; rounded corners use tangent quarter arcs; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (storage-jar VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class StorageJar(Container64):
    icon_id = 'storage-jar'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('storage', 'jar')

    def build(self) -> None:
        self.add_line('body-0', (22, 13), (42, 13))
        self.add_arc('body-1', (42, 13), (52, 23), radius_x=10)
        self.add_line('body-2', (52, 23), (52, 51))
        self.add_arc('body-3', (52, 51), (42, 60), radius_x=10, radius_y=9)
        self.add_line('body-4', (42, 60), (22, 60))
        self.add_arc('body-5', (22, 60), (12, 51), radius_x=10, radius_y=9)
        self.add_line('body-6', (12, 51), (12, 23))
        self.add_arc('body-7', (12, 23), (22, 13), radius_x=10)
        self.add_line('neck-0', (22, 13), (16, 4))
        self.add_line('neck-1', (16, 4), (48, 4))
        self.add_line('neck-2', (48, 4), (42, 13))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('neck', 'neck-0', 'neck-1', 'neck-2')
        self.relate('connect', 'body', 'neck')
