"""Container shapes.

Four open enclosures. Each is a single outline with an empty interior, so each
hosts anything the CONTAINER_COMBINE template will place in it -- not because a
rule reserves the middle of the canvas (the protected slot was withdrawn on
2026-09-07) but because these particular subjects have nothing inside them. A
container with real interior furniture, such as `browser-window`, is drawn the
same way and simply clears fewer children; `compose.py` reports which.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (container-circle CIRCLE -> CIRCLE; container-hexagon SQUARE -> SQUARE; container-rounded-square SQUARE -> SQUARE; container-square SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class CircleContainer(Container64):
    icon_id = 'container-circle'
    keyshape = Keyshape.CIRCLE
    aliases = ('ring-container', 'badge-circle')
    keywords = ('circle', 'ring', 'badge', 'avatar', 'bubble')

    def build(self) -> None:
        self.add_arc('half-top', (4, 32), (60, 32), radius_x=28)
        self.add_arc('half-bottom', (60, 32), (4, 32), radius_x=28)
        self.add_contour('outline', 'half-top', 'half-bottom', closed=True)


class HexagonContainer(Container64):
    icon_id = 'container-hexagon'
    keyshape = Keyshape.SQUARE
    aliases = ('hex-badge',)
    keywords = ('hexagon', 'badge', 'cell', 'token')

    def build(self) -> None:
        self.add_line('outline-1', (14, 6), (50, 6))
        self.add_line('outline-2', (50, 6), (58, 32))
        self.add_line('outline-3', (58, 32), (50, 58))
        self.add_line('outline-4', (50, 58), (14, 58))
        self.add_line('outline-5', (14, 58), (6, 32))
        self.add_line('outline-6', (6, 32), (14, 6))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)


class RoundedSquareContainer(Container64):
    icon_id = 'container-rounded-square'
    keyshape = Keyshape.SQUARE
    aliases = ('squircle', 'app-tile', 'rounded-corner-square-frame')
    keywords = ('rounded', 'square', 'tile', 'app', 'card')

    def build(self) -> None:
        self.add_line('edge-top', (14, 6), (50, 6))
        self.add_arc('corner-ne', (50, 6), (58, 14), radius_x=8)
        self.add_line('edge-right', (58, 14), (58, 50))
        self.add_arc('corner-se', (58, 50), (50, 58), radius_x=8)
        self.add_line('edge-bottom', (50, 58), (14, 58))
        self.add_arc('corner-sw', (14, 58), (6, 50), radius_x=8)
        self.add_line('edge-left', (6, 50), (6, 14))
        self.add_arc('corner-nw', (6, 14), (14, 6), radius_x=8)
        self.add_contour('outline', 'edge-top', 'corner-ne', 'edge-right', 'corner-se', 'edge-bottom', 'corner-sw', 'edge-left', 'corner-nw', closed=True)


class SquareContainer(Container64):
    icon_id = 'container-square'
    keyshape = Keyshape.SQUARE
    aliases = ('box-container', 'frame')
    keywords = ('square', 'box', 'frame', 'card', 'window')

    def build(self) -> None:
        self.add_line('outline-1', (6, 6), (58, 6))
        self.add_line('outline-2', (58, 6), (58, 58))
        self.add_line('outline-3', (58, 58), (6, 58))
        self.add_line('outline-4', (6, 58), (6, 6))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', closed=True)
