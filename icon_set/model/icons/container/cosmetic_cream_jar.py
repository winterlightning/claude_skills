"""A rounded cosmetic jar with a narrower screw lid.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide square-dashed: tangent quarter-circle corners; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (cosmetic-cream-jar SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class CosmeticCreamJar(Container64):
    icon_id = 'cosmetic-cream-jar'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('cosmetic', 'cream', 'jar')

    def build(self) -> None:
        self.add_line('jar-0', (14, 22), (50, 22))
        self.add_arc('jar-1', (50, 22), (58, 29), radius_x=8, radius_y=7)
        self.add_line('jar-2', (58, 29), (58, 48))
        self.add_arc('jar-3', (58, 48), (50, 58), radius_x=8, radius_y=10)
        self.add_line('jar-4', (50, 58), (14, 58))
        self.add_arc('jar-5', (14, 58), (6, 48), radius_x=8, radius_y=10)
        self.add_line('jar-6', (6, 48), (6, 29))
        self.add_arc('jar-7', (6, 29), (14, 22), radius_x=8, radius_y=7)
        self.add_line('lid-left', (14, 22), (14, 10))
        self.add_arc('lid-nw', (14, 10), (18, 6), radius_x=4)
        self.add_line('lid-top', (18, 6), (46, 6))
        self.add_arc('lid-ne', (46, 6), (50, 10), radius_x=4)
        self.add_line('lid-right', (50, 10), (50, 22))
        self.add_contour('jar', 'jar-0', 'jar-1', 'jar-2', 'jar-3', 'jar-4', 'jar-5', 'jar-6', 'jar-7', closed=True)
        self.add_contour('lid', 'lid-left', 'lid-nw', 'lid-top', 'lid-ne', 'lid-right')
        self.relate('connect', 'lid', 'jar')
