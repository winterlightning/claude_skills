"""Hexagon Geometric Shape: independently authored container.

Construction plan: One point-top hexagonal enclosure with mirror-derived vertices; keep source orientation.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/design/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg. Lucide container original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (point-top-hexagon-container VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '392ff95c-1214-470d-870f-2dc6d3f7f1c3'
SOURCE_PATH = 'pictographic-primitives/design/hexagon shape_392ff95c-1214-470d-870f-2dc6d3f7f1c3.svg'
AUTHOR = 'claude-opus-5-5'


class PointTopHexagonContainer(Container64):
    icon_id = 'point-top-hexagon-container'
    keyshape = Keyshape.VRECT_L
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('point', 'top', 'hexagon', 'container')

    def build(self) -> None:
        self.add_line('hexagon-1', (32, 4), (54, 18))
        self.add_line('hexagon-2', (54, 18), (54, 46))
        self.add_line('hexagon-3', (54, 46), (32, 60))
        self.add_line('hexagon-4', (32, 60), (10, 46))
        self.add_line('hexagon-5', (10, 46), (10, 18))
        self.add_line('hexagon-6', (10, 18), (32, 4))
        self.add_contour('hexagon', 'hexagon-1', 'hexagon-2', 'hexagon-3', 'hexagon-4', 'hexagon-5', 'hexagon-6', closed=True)
