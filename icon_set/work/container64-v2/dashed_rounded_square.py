"""A rounded square selection boundary made of separated strokes.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide square-dashed: corner arcs and paired straight dashes; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (dashed-rounded-square SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class DashedRoundedSquare(Container64):
    icon_id = 'dashed-rounded-square'
    keyshape = Keyshape.SQUARE
    aliases = ('rounded-dashed-selection-box',)
    keywords = ('dashed', 'rounded', 'square')

    def build(self) -> None:
        self.add_arc('corner-0', (6, 13), (13, 6), radius_x=7)
        self.add_line('dash-a-0', (21, 6), (28, 6))
        self.add_line('dash-b-0', (36, 6), (43, 6))
        self.add_arc('corner-1', (51, 6), (58, 13), radius_x=7)
        self.add_line('dash-a-1', (58, 21), (58, 28))
        self.add_line('dash-b-1', (58, 36), (58, 43))
        self.add_arc('corner-2', (58, 51), (51, 58), radius_x=7)
        self.add_line('dash-a-2', (43, 58), (36, 58))
        self.add_line('dash-b-2', (28, 58), (21, 58))
        self.add_arc('corner-3', (13, 58), (6, 51), radius_x=7)
        self.add_line('dash-a-3', (6, 43), (6, 36))
        self.add_line('dash-b-3', (6, 28), (6, 21))
