"""A blank upright page with a folded upper-right corner.

Keyshape VRECT_L: chosen for the reference silhouette.
Lucide file: rounded page and inward quarter-circle fold; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus does not fit, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class DocumentWithFoldedCorner(Container64):
    icon_id = 'document-with-folded-corner'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('document', 'with', 'folded', 'corner')

    def build(self) -> None:
        self.add_line('top', (14, 2), (36, 2))
        self.add_line('diagonal', (36, 2), (54, 20))
        self.add_line('right', (54, 20), (54, 58))
        self.add_arc('se', (54, 58), (50, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (50, 62), (14, 62))
        self.add_arc('sw', (14, 62), (10, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (10, 58), (10, 6))
        self.add_arc('nw', (10, 6), (14, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('page', 'top', 'diagonal', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_line('fold-down', (36, 2), (36, 16))
        self.add_arc('fold-corner', (36, 16), (40, 20), radius_x=4, radius_y=4, sweep=False)
        self.add_line('fold-across', (40, 20), (54, 20))
        self.add_contour('fold', 'fold-down', 'fold-corner', 'fold-across', closed=False)
        self.relate("connect", 'page', 'fold')
