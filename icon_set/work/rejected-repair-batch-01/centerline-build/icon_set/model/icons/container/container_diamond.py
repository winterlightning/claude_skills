"""An empty diamond outline enclosing a central field.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide polygon originals and atoms inform a single closed, mirrored perimeter..
Rounded stroke joins retain the intentional polygon corners; no inset detail added.
Hosting measured with compose.py: plus: pass; heart: pass; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class ContainerDiamond(Container64):
    icon_id = "container-diamond"
    keyshape = Keyshape.SQUARE
    aliases = ("geometric-diamond-shape",)
    keywords = ('container', 'diamond')

    def build(self) -> None:
        self.add_polyline('outline', (32, 2), (62, 32), (32, 62), (2, 32), closed=True)
