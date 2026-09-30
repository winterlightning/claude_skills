"""A blank upright page with a folded upper-right corner.

Keyshape VRECT_L: chosen for the reference silhouette.
Lucide file: rounded page and inward quarter-circle fold; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus does not fit, heart does not fit, check does not fit.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (document-with-folded-corner VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class DocumentWithFoldedCorner(Container64):
    icon_id = 'document-with-folded-corner'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('document', 'with', 'folded', 'corner')

    def build(self) -> None:
        self.add_line('top', (16, 4), (36, 4))
        self.add_line('diagonal', (36, 4), (52, 21))
        self.add_line('right', (52, 21), (52, 56))
        self.add_arc('se', (52, 56), (48, 60), radius_x=4)
        self.add_line('bottom', (48, 60), (16, 60))
        self.add_arc('sw', (16, 60), (12, 56), radius_x=4)
        self.add_line('left', (12, 56), (12, 8))
        self.add_arc('nw', (12, 8), (16, 4), radius_x=4)
        self.add_line('fold-down', (36, 4), (36, 17))
        self.add_arc('fold-corner', (36, 17), (40, 21), radius_x=4, sweep=False)
        self.add_line('fold-across', (40, 21), (52, 21))
        self.add_contour('page', 'top', 'diagonal', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_contour('fold', 'fold-down', 'fold-corner', 'fold-across')
        self.relate('connect', 'page', 'fold')
