"""An empty eight-lobed seal with mirrored circular scallops.
The shallow inward cusps define the scallops; no source features removed.

Keyshape CIRCLE; centerline extremes recorded in build below.
Lucide badge informs eight repeated convex arcs joined at inward scallop cusps. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class ScallopedCircularBadge(Container64):
    icon_id = 'scalloped-circular-badge'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('scalloped', 'circular', 'badge')

    def build(self) -> None:
        # Radial keyshape: radius 30 about (32,32); extremes 2 and 62.
        points = [(23, 11), (41, 11), (53, 23), (53, 41),
                  (41, 53), (23, 53), (11, 41), (11, 23)]
        names = []
        for i, start in enumerate(points):
            name = f"lobe-{i}"
            self.add_arc(name, start, points[(i + 1) % 8], radius_x=9)
            names.append(name)
        self.add_contour("outline", *names, closed=True)
