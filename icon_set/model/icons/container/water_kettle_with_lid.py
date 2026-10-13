"""A lidded kettle with a pouring spout and a loop handle.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: cooking-pot: joined rim, vessel and lid; asymmetric spout and handle retained. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (water-kettle-with-lid SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class WaterKettleWithLid(Container64):
    icon_id = 'water-kettle-with-lid'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('water', 'kettle', 'with', 'lid')

    def build(self) -> None:
        self.add_line('body-0', (6, 18), (35, 18))
        self.add_arc('body-1', (35, 18), (48, 32), radius_x=16, radius_y=37)
        self.add_arc('body-2', (48, 32), (52, 52), radius_x=16, radius_y=37)
        self.add_arc('body-3', (52, 52), (46, 58), radius_x=6)
        self.add_line('body-4', (46, 58), (12, 58))
        self.add_arc('body-5', (12, 58), (6, 52), radius_x=6)
        self.add_line('body-6', (6, 52), (10, 28))
        self.add_line('body-7', (10, 28), (6, 18))
        self.add_arc('lid-0', (15, 18), (25, 8), radius_x=10)
        self.add_arc('lid-1', (25, 8), (35, 18), radius_x=10)
        self.add_line('knob', (25, 6), (25, 8))
        self.add_line('handle-0', (35, 18), (46, 18))
        self.add_arc('handle-1', (46, 18), (58, 24), radius_x=12, radius_y=6)
        self.add_arc('handle-2', (58, 24), (48, 32), radius_x=10, radius_y=8)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('lid', 'lid-0', 'lid-1')
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2')
        self.relate('connect', 'body', 'lid')
        self.relate('connect', 'knob', 'lid')
        self.relate('connect', 'body', 'handle')
        self.relate('connect', 'lid', 'handle')
