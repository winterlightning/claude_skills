"""A trash bin with a wide flat lid, arched grip, and rounded lower corners.

SQUARE: (0, 0, 64, 64); chosen for the source silhouette.
Lucide trash: lid overhang, rounded base, and attached handle; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class TrashBin(Container64):
    icon_id = 'trash-bin'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('trash', 'bin')

    def build(self) -> None:
        self.add_line('body-0', (10, 14), (10, 56))
        self.add_arc('body-1', (10, 56), (16, 62), radius_x=6, radius_y=6, sweep=False)
        self.add_line('body-2', (16, 62), (48, 62))
        self.add_arc('body-3', (48, 62), (54, 56), radius_x=6, radius_y=6, sweep=False)
        self.add_line('body-4', (54, 56), (54, 14))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', closed=False)
        self.add_line('lid-0', (2, 14), (62, 14))
        self.add_contour('lid', 'lid-0', closed=False)
        self.add_line('grip-0', (22, 14), (22, 6))
        self.add_arc('grip-1', (22, 6), (26, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_line('grip-2', (26, 2), (38, 2))
        self.add_arc('grip-3', (38, 2), (42, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('grip-4', (42, 6), (42, 14))
        self.add_contour('grip', 'grip-0', 'grip-1', 'grip-2', 'grip-3', 'grip-4', closed=False)
        self.relate("connect", "body", "lid")
        self.relate("connect", "grip", "lid")
