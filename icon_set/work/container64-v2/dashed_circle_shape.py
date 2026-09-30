"""A circular enclosure made of eight separated curved dashes.

Keyshape CIRCLE: chosen for the reference silhouette.
Lucide circle-dashed: separated arcs around a shared center; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (dashed-circle-shape CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class DashedCircleShape(Container64):
    icon_id = 'dashed-circle-shape'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('dashed', 'circle', 'shape')

    def build(self) -> None:
        self.add_arc('cardinal-0', (26, 5), (38, 5), radius_x=19)
        self.add_arc('diagonal-0', (47, 9), (55, 17), radius_x=28)
        self.add_arc('cardinal-1', (59, 26), (59, 38), radius_x=19)
        self.add_arc('diagonal-1', (55, 47), (47, 55), radius_x=28)
        self.add_arc('cardinal-2', (38, 59), (26, 59), radius_x=19)
        self.add_arc('diagonal-2', (17, 55), (9, 47), radius_x=28)
        self.add_arc('cardinal-3', (5, 38), (5, 26), radius_x=19)
        self.add_arc('diagonal-3', (9, 17), (17, 9), radius_x=28)
