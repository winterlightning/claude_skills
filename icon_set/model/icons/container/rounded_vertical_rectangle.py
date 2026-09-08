"""An empty portrait frame with matching soft corners; no source features removed.

Keyshape VRECT_XL; centerline extremes recorded in build below.
Lucide rectangle-vertical informs paired straight runs and consistent corner radii. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class RoundedVerticalRectangle(Container64):
    icon_id = 'rounded-vertical-rectangle'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('rounded', 'vertical', 'rectangle')

    def build(self) -> None:
        # Centerline extremes (6,2)-(58,62); mirrored quarter-circle corners.
        self.add_line("top", (13, 2), (51, 2))
        self.add_arc("ne", (51, 2), (58, 9), radius_x=7)
        self.add_line("right", (58, 9), (58, 55))
        self.add_arc("se", (58, 55), (51, 62), radius_x=7)
        self.add_line("bottom", (51, 62), (13, 62))
        self.add_arc("sw", (13, 62), (6, 55), radius_x=7)
        self.add_line("left", (6, 55), (6, 9))
        self.add_arc("nw", (6, 9), (13, 2), radius_x=7)
        self.add_contour("outline", "top", "ne", "right", "se", "bottom", "sw", "left", "nw", closed=True)
