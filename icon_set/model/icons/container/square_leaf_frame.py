"""An empty leaf-like frame with rounded northwest and southeast corners.
The other two corners remain deliberately pointed; no vein or stem is added.

Keyshape SQUARE; centerline extremes recorded in build below.
Lucide square informs tangent corner construction; leaf was inspected but its botanical silhouette is not a useful match. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SquareLeafFrame(Container64):
    icon_id = 'square-leaf-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('rounded-leaf-shape-icon',)
    keywords = ('square', 'leaf', 'frame')

    def build(self) -> None:
        # Centerline extremes (2,2)-(62,62); opposing matching arcs.
        self.add_line("top", (26, 2), (62, 2))
        self.add_line("right", (62, 2), (62, 38))
        self.add_arc("se", (62, 38), (38, 62), radius_x=24)
        self.add_line("bottom", (38, 62), (2, 62))
        self.add_line("left", (2, 62), (2, 26))
        self.add_arc("nw", (2, 26), (26, 2), radius_x=24)
        self.add_contour("outline", "top", "right", "se", "bottom", "left", "nw", closed=True)
