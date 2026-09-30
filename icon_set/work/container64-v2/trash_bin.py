"""A trash bin with a wide flat lid, arched grip, and rounded lower corners.

SQUARE: (0, 0, 64, 64); chosen for the source silhouette.
Lucide trash: lid overhang, rounded base, and attached handle; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (trash-bin SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class TrashBin(Container64):
    icon_id = 'trash-bin'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('trash', 'bin')

    def build(self) -> None:
        self.add_line('body-0', (12, 18), (12, 52))
        self.add_arc('body-1', (12, 52), (18, 58), radius_x=6, sweep=False)
        self.add_line('body-2', (18, 58), (46, 58))
        self.add_arc('body-3', (46, 58), (52, 52), radius_x=6, sweep=False)
        self.add_line('body-4', (52, 52), (52, 18))
        self.add_line('lid-0', (6, 18), (58, 18))
        self.add_line('grip-0', (24, 18), (24, 10))
        self.add_arc('grip-1', (24, 10), (28, 6), radius_x=4)
        self.add_line('grip-2', (28, 6), (36, 6))
        self.add_arc('grip-3', (36, 6), (40, 10), radius_x=4)
        self.add_line('grip-4', (40, 10), (40, 18))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4')
        self.add_contour('lid', 'lid-0')
        self.add_contour('grip', 'grip-0', 'grip-1', 'grip-2', 'grip-3', 'grip-4')
        self.relate('connect', 'body', 'lid')
        self.relate('connect', 'grip', 'lid')
