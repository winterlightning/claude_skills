"""An empty diamond outline enclosing a central field.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide polygon originals and atoms inform a single closed, mirrored perimeter..
Rounded stroke joins retain the intentional polygon corners; no inset detail added.
Hosting measured with compose.py: plus: pass; heart: pass; check: does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (container-diamond SQUARE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class ContainerDiamond(Container64):
    icon_id = 'container-diamond'
    keyshape = Keyshape.CIRCLE
    aliases = ('geometric-diamond-shape',)
    keywords = ('container', 'diamond')

    def build(self) -> None:
        self.add_line('outline-1', (32, 4), (60, 32))
        self.add_line('outline-2', (60, 32), (32, 60))
        self.add_line('outline-3', (32, 60), (4, 32))
        self.add_line('outline-4', (4, 32), (32, 4))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', closed=True)
