"""A convex teardrop map-pin enclosure with a pointed base.

VRECT_L: exact centerline extremes recorded in build.
Construction: Lucide map-pin, mirrored round crown and tapered shoulders; distinct from the existing concave-neck pin. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (teardrop-location-pin SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn as one smooth teardrop (Bezier sides, no kinks at the shoulders); same frame and symbol room.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class TeardropLocationPin(Container64):
    icon_id = 'teardrop-location-pin'
    keyshape = Keyshape.SQUARE
    aliases = ('map-location-pin-marker',)
    keywords = ('teardrop', 'location', 'pin')

    def build(self) -> None:
        # One smooth teardrop: each side is a Bezier run from the tip (32,58) to the widest point (6,28) with a
        # vertical tangent, then round over the top (32,6) with a horizontal tangent; the right side mirrors the
        # left about x = 32. Replaces the flattened-ellipse crown and 35-radius shoulders that kinked at their joins.
        self.add_bezier('left', (32, 58), ((26, 52), (6, 42), (6, 28)), ((6, 15), (18, 6), (32, 6)))
        self.add_bezier('right', (32, 6), ((46, 6), (58, 15), (58, 28)), ((58, 42), (38, 52), (32, 58)))
        self.add_contour('outline', 'left', 'right', closed=True)
