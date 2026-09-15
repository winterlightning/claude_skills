"""A blank rounded sign panel centered on a single supporting post.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide signpost supplies the centered support; rectangle-horizontal supplies tangent rounded corners.
The panel width and height preserve this reference proportion; left and right halves mirror about x=32.
Hosting measured with compose.py: plus: pass; heart: pass; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RectangularSignboardOnAPole(Container64):
    icon_id = 'rectangular-signboard-on-a-pole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('rectangular', 'signboard', 'on', 'a', 'pole')

    def build(self) -> None:
        self.add_line('panel0', (6, 2), (58, 2))
        self.add_arc('panel1', (58, 2), (62, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel2', (62, 6), (62, 40))
        self.add_arc('panel3', (62, 40), (58, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel4', (58, 44), (6, 44))
        self.add_arc('panel5', (6, 44), (2, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel6', (2, 40), (2, 6))
        self.add_arc('panel7', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('panel', 'panel0', 'panel1', 'panel2', 'panel3', 'panel4', 'panel5', 'panel6', 'panel7', closed=True)
        self.add_line('post', (32, 44), (32, 62))
        self.relate("connect", 'panel', 'post')
