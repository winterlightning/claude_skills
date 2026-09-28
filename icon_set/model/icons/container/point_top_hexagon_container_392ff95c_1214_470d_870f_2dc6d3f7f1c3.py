"""Hexagon Geometric Shape: independently authored container.

Construction plan: One point-top hexagonal enclosure with mirror-derived vertices; keep source orientation.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/design/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg. Lucide container original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '392ff95c-1214-470d-870f-2dc6d3f7f1c3'
SOURCE_PATH = 'pictographic-primitives/design/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg'
AUTHOR = 'gpt-6'


class PointTopHexagonContainer(Container64):
    icon_id = 'point-top-hexagon-container'
    category = 'design'
    categories = ('design', 'primitives')
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('point', 'top', 'hexagon', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('hexagon',(32,2),(58,17),(58,47),(32,62),(6,47),(6,17),closed=True)
