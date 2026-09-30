"""A storage box with an overhanging lid.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide archive: separate rounded lid and attached U-shaped body.
All identity features retained.
Hosting (compose.py): plus does not fit, heart does not fit, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (storage-box-with-lid SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class StorageBoxWithLid(Container64):
    icon_id = 'storage-box-with-lid'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('storage', 'box', 'with', 'lid')

    def build(self) -> None:
        self.add_line('lid-0', (9, 6), (55, 6))
        self.add_arc('lid-1', (55, 6), (58, 9), radius_x=3)
        self.add_line('lid-2', (58, 9), (58, 15))
        self.add_arc('lid-3', (58, 15), (55, 18), radius_x=3)
        self.add_line('lid-4', (55, 18), (9, 18))
        self.add_arc('lid-5', (9, 18), (6, 15), radius_x=3)
        self.add_line('lid-6', (6, 15), (6, 9))
        self.add_arc('lid-7', (6, 9), (9, 6), radius_x=3)
        self.add_line('body-0', (10, 18), (10, 48))
        self.add_arc('body-1', (10, 48), (18, 58), radius_x=8, radius_y=10, sweep=False)
        self.add_line('body-2', (18, 58), (46, 58))
        self.add_arc('body-3', (46, 58), (54, 48), radius_x=8, radius_y=10, sweep=False)
        self.add_line('body-4', (54, 48), (54, 18))
        self.add_contour('lid', 'lid-0', 'lid-1', 'lid-2', 'lid-3', 'lid-4', 'lid-5', 'lid-6', 'lid-7', closed=True)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4')
        self.relate('connect', 'body', 'lid')
