"""Container shapes.

Four open enclosures. Each is a single outline with an empty interior, so each
hosts anything the CONTAINER_COMBINE template will place in it -- not because a
rule reserves the middle of the canvas (the protected slot was withdrawn on
2026-09-07) but because these particular subjects have nothing inside them. A
container with real interior furniture, such as `browser-window`, is drawn the
same way and simply clears fewer children; `compose.py` reports which.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class CircleContainer(Container64):
    icon_id = "container-circle"
    keyshape = Keyshape.CIRCLE
    aliases = ("ring-container", "badge-circle")
    keywords = ("circle", "ring", "badge", "avatar", "bubble")

    def build(self) -> None:
        self.add_arc("half-top", (2, 32), (62, 32), radius_x=30)
        self.add_arc("half-bottom", (62, 32), (2, 32), radius_x=30)
        self.add_contour("outline", "half-top", "half-bottom", closed=True)


class SquareContainer(Container64):
    icon_id = "container-square"
    keyshape = Keyshape.SQUARE
    aliases = ("box-container", "frame")
    keywords = ("square", "box", "frame", "card", "window")

    def build(self) -> None:
        self.add_polyline("outline", (2, 2), (62, 2), (62, 62), (2, 62), closed=True)


class RoundedSquareContainer(Container64):
    icon_id = "container-rounded-square"
    keyshape = Keyshape.SQUARE
    aliases = ("squircle", "app-tile", "rounded-corner-square-frame")
    keywords = ("rounded", "square", "tile", "app", "card")

    def build(self) -> None:
        # Corner radius 8: the straight runs stay long enough to read as a
        # square, and each corner arc is a clean quarter circle on the grid.
        self.add_line("edge-top", (11, 2), (53, 2))
        self.add_arc("corner-ne", (53, 2), (62, 11), radius_x=9)
        self.add_line("edge-right", (62, 11), (62, 53))
        self.add_arc("corner-se", (62, 53), (53, 62), radius_x=9)
        self.add_line("edge-bottom", (53, 62), (11, 62))
        self.add_arc("corner-sw", (11, 62), (2, 53), radius_x=9)
        self.add_line("edge-left", (2, 53), (2, 11))
        self.add_arc("corner-nw", (2, 11), (11, 2), radius_x=9)
        self.add_contour(
            "outline",
            "edge-top", "corner-ne", "edge-right", "corner-se",
            "edge-bottom", "corner-sw", "edge-left", "corner-nw",
            closed=True,
        )


class HexagonContainer(Container64):
    icon_id = "container-hexagon"
    keyshape = Keyshape.SQUARE
    aliases = ("hex-badge",)
    keywords = ("hexagon", "badge", "cell", "token")

    def build(self) -> None:
        # The top corners sit at x 14, not 22. A hexagon's diagonals cut across
        # the square slot's corners, and pulling them in to 22 leaves only 0.13
        # units of centerline clearance there -- the ink crosses well inside the
        # slot. At 14 the diagonal clears the corner by 4.85 centerline units.
        self.add_polyline(
            "outline",
            (11, 2), (53, 2), (62, 32), (53, 62), (11, 62), (2, 32),
            closed=True,
        )
