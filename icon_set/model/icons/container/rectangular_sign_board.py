"""A blank rounded sign panel centered on a single supporting post.

Keyshape HRECT_L: (0, 8, 64, 56); authored from its exact extremes.
Reference: batch_10 source render. Lucide signpost supplies the centered support; rectangle-horizontal supplies tangent rounded corners.
The panel width and height preserve this reference proportion; left and right halves mirror about x=32.
Hosting measured with compose.py: plus: pass; heart: pass; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class RectangularSignBoard(Container64):
    icon_id = 'rectangular-sign-board'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('rectangular', 'sign', 'board')

    def build(self) -> None:
        self.add_line('panel0', (6, 10), (58, 10))
        self.add_arc('panel1', (58, 10), (62, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel2', (62, 14), (62, 32))
        self.add_arc('panel3', (62, 32), (58, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel4', (58, 36), (6, 36))
        self.add_arc('panel5', (6, 36), (2, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel6', (2, 32), (2, 14))
        self.add_arc('panel7', (2, 14), (6, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('panel', 'panel0', 'panel1', 'panel2', 'panel3', 'panel4', 'panel5', 'panel6', 'panel7', closed=True)
        self.add_line('post', (32, 36), (32, 54))
        self.relate("connect", 'panel', 'post')
