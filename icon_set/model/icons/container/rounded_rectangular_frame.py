"""An empty landscape frame with gently rounded corners; no source features removed.

Keyshape HRECT_M; centerline extremes recorded in build below.
Lucide rectangle-horizontal informs tangent quarter-circle corners. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class RoundedRectangularFrame(Container64):
    icon_id = 'rounded-rectangular-frame'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('rounded', 'rectangular', 'frame')

    def build(self) -> None:
        # Centerline extremes (2,14)-(62,50); mirrored quarter-circle corners.
        self.add_line("top", (6, 14), (58, 14))
        self.add_arc("ne", (58, 14), (62, 18), radius_x=4)
        self.add_line("right", (62, 18), (62, 46))
        self.add_arc("se", (62, 46), (58, 50), radius_x=4)
        self.add_line("bottom", (58, 50), (6, 50))
        self.add_arc("sw", (6, 50), (2, 46), radius_x=4)
        self.add_line("left", (2, 46), (2, 18))
        self.add_arc("nw", (2, 18), (6, 14), radius_x=4)
        self.add_contour("outline", "top", "ne", "right", "se", "bottom", "sw", "left", "nw", closed=True)
