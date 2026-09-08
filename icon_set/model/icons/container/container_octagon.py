"""An empty octagon outline enclosing a central field.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide polygon originals and atoms inform a single closed, mirrored perimeter..
Rounded stroke joins retain the intentional polygon corners; no inset detail added.
Hosting measured with compose.py: plus: pass; heart: pass; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class ContainerOctagon(Container64):
    icon_id = "container-octagon"
    keyshape = Keyshape.SQUARE
    aliases = ("geometric-octagonal-shape",)
    keywords = ('container', 'octagon')

    def build(self) -> None:
        self.add_polyline('outline', (20, 2), (44, 2), (62, 20), (62, 44), (44, 62), (20, 62), (2, 44), (2, 20), closed=True)
