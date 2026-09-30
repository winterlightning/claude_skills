"""An empty octagon outline enclosing a central field.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide polygon originals and atoms inform a single closed, mirrored perimeter..
Rounded stroke joins retain the intentional polygon corners; no inset detail added.
Hosting measured with compose.py: plus: pass; heart: pass; check: pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (container-octagon SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class ContainerOctagon(Container64):
    icon_id = 'container-octagon'
    keyshape = Keyshape.SQUARE
    aliases = ('geometric-octagonal-shape',)
    keywords = ('container', 'octagon')

    def build(self) -> None:
        self.add_line('outline-1', (22, 6), (42, 6))
        self.add_line('outline-2', (42, 6), (58, 22))
        self.add_line('outline-3', (58, 22), (58, 42))
        self.add_line('outline-4', (58, 42), (42, 58))
        self.add_line('outline-5', (42, 58), (22, 58))
        self.add_line('outline-6', (22, 58), (6, 42))
        self.add_line('outline-7', (6, 42), (6, 22))
        self.add_line('outline-8', (6, 22), (22, 6))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', closed=True)
