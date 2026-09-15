"""An empty leaf-like frame with rounded northwest and southeast corners.
The other two corners remain deliberately pointed; no vein or stem is added.

Keyshape HRECT_XL; centerline extremes recorded in build below.
Lucide square informs tangent corner construction; leaf was inspected but its botanical silhouette is not a useful match. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class HorizontalLeafFrame(Container64):
    icon_id = 'horizontal-leaf-frame'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('rounded-leaf-shape',)
    keywords = ('horizontal', 'leaf', 'frame')

    def build(self) -> None:
        # Centerline extremes (2,6)-(62,58); opposing matching arcs.
        self.add_line("top", (24, 6), (62, 6))
        self.add_line("right", (62, 6), (62, 36))
        self.add_arc("se", (62, 36), (40, 58), radius_x=22)
        self.add_line("bottom", (40, 58), (2, 58))
        self.add_line("left", (2, 58), (2, 28))
        self.add_arc("nw", (2, 28), (24, 6), radius_x=22)
        self.add_contour("outline", "top", "right", "se", "bottom", "left", "nw", closed=True)
