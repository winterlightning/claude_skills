"""A blank rounded sign panel centered on a single supporting post.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide signpost supplies the centered support; rectangle-horizontal supplies tangent rounded corners.
The panel width and height preserve this reference proportion; left and right halves mirror about x=32.
Hosting measured with compose.py: plus: pass; heart: pass; check: does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rectangular-signboard-on-a-pole SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RectangularSignboardOnAPole(Container64):
    icon_id = 'rectangular-signboard-on-a-pole'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rectangular', 'signboard', 'on', 'a', 'pole')

    def build(self) -> None:
        self.add_line('panel0', (10, 6), (54, 6))
        self.add_arc('panel1', (54, 6), (58, 10), radius_x=4)
        self.add_line('panel2', (58, 10), (58, 38))
        self.add_arc('panel3', (58, 38), (54, 42), radius_x=4)
        self.add_line('panel4', (54, 42), (10, 42))
        self.add_arc('panel5', (10, 42), (6, 38), radius_x=4)
        self.add_line('panel6', (6, 38), (6, 10))
        self.add_arc('panel7', (6, 10), (10, 6), radius_x=4)
        self.add_line('post', (32, 42), (32, 58))
        self.add_contour('panel', 'panel0', 'panel1', 'panel2', 'panel3', 'panel4', 'panel5', 'panel6', 'panel7', closed=True)
        self.relate('connect', 'panel', 'post')
