"""A rounded storage jar with an open flared neck.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide cylinder: vessel outline; rounded corners use tangent quarter arcs; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class StorageJar(Container64):
    icon_id = 'storage-jar'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('storage', 'jar')

    def build(self) -> None:
        self.add_line('body-0', (20, 12), (44, 12))
        self.add_arc('body-1', (44, 12), (54, 22), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-2', (54, 22), (54, 52))
        self.add_arc('body-3', (54, 52), (44, 62), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-4', (44, 62), (20, 62))
        self.add_arc('body-5', (20, 62), (10, 52), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-6', (10, 52), (10, 22))
        self.add_arc('body-7', (10, 22), (20, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_line('neck-0', (20, 12), (14, 2))
        self.add_line('neck-1', (14, 2), (50, 2))
        self.add_line('neck-2', (50, 2), (44, 12))
        self.add_contour('neck', 'neck-0', 'neck-1', 'neck-2', closed=False)
        self.relate("connect", "body", "neck")
