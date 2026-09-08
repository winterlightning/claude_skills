"""An empty pentagon outline enclosing a central field.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide polygon originals and atoms inform a single closed, mirrored perimeter..
Rounded stroke joins retain the intentional polygon corners; no inset detail added.
Hosting measured with compose.py: plus: pass; heart: pass; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class ContainerPentagon(Container64):
    icon_id = "container-pentagon"
    keyshape = Keyshape.SQUARE
    aliases = ("geometric-pentagon-shape",)
    keywords = ('container', 'pentagon')

    def build(self) -> None:
        self.add_polyline('outline', (32, 2), (62, 25), (50, 62), (14, 62), (2, 25), closed=True)
