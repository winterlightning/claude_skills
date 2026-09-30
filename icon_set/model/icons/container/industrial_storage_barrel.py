"""An industrial barrel with projecting rims and two pairs of short reinforcing ribs.

Keyshape SQUARE: centerline extremes recorded in build below.
The supplied front-view barrel sets the construction. Lucide cylinder was inspected but its perspective ellipses are inappropriate here.
Hosting (compose.py): plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (industrial-storage-barrel SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class IndustrialStorageBarrel(Container64):
    icon_id = 'industrial-storage-barrel'
    keyshape = Keyshape.SQUARE
    aliases = ('storage-drum',)
    keywords = ('industrial', 'storage', 'barrel')

    def build(self) -> None:
        self.add_line('body-1', (12, 6), (52, 6))
        self.add_line('body-2', (52, 6), (52, 58))
        self.add_line('body-3', (52, 58), (12, 58))
        self.add_line('body-4', (12, 58), (12, 6))
        self.add_line('rim-top-left', (6, 6), (12, 6))
        self.add_line('rim-top-right', (52, 6), (58, 6))
        self.add_line('rib-upper-left', (6, 23), (12, 23))
        self.add_line('rib-upper-right', (52, 23), (58, 23))
        self.add_line('rib-lower-left', (6, 41), (12, 41))
        self.add_line('rib-lower-right', (52, 41), (58, 41))
        self.add_line('rim-bottom-left', (6, 58), (12, 58))
        self.add_line('rim-bottom-right', (52, 58), (58, 58))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', closed=True)
        self.relate('connect', 'body', 'rim-top-left')
        self.relate('connect', 'body', 'rim-top-right')
        self.relate('connect', 'body', 'rib-upper-left')
        self.relate('connect', 'body', 'rib-upper-right')
        self.relate('connect', 'body', 'rib-lower-left')
        self.relate('connect', 'body', 'rib-lower-right')
        self.relate('connect', 'body', 'rim-bottom-left')
        self.relate('connect', 'body', 'rim-bottom-right')
