"""Four rounded corner brackets enclose a camera focus area. No central mark added.

Keyshape: SQUARE; centerline extremes recorded in build.
Construction reference: Lucide scan: four matching line-arc-line corner contours.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-camera-focus-viewfinder SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareCameraFocusViewfinder(Container64):
    icon_id = 'square-camera-focus-viewfinder'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'camera', 'focus', 'viewfinder')

    def build(self) -> None:
        self.add_line('nw-vertical', (6, 22), (6, 12))
        self.add_arc('nw-corner', (6, 12), (12, 6), radius_x=6)
        self.add_line('nw-horizontal', (12, 6), (22, 6))
        self.add_line('ne-vertical', (58, 22), (58, 12))
        self.add_arc('ne-corner', (58, 12), (52, 6), radius_x=6, sweep=False)
        self.add_line('ne-horizontal', (52, 6), (42, 6))
        self.add_line('se-vertical', (58, 42), (58, 52))
        self.add_arc('se-corner', (58, 52), (52, 58), radius_x=6)
        self.add_line('se-horizontal', (52, 58), (42, 58))
        self.add_line('sw-vertical', (6, 42), (6, 52))
        self.add_arc('sw-corner', (6, 52), (12, 58), radius_x=6, sweep=False)
        self.add_line('sw-horizontal', (12, 58), (22, 58))
        self.add_contour('nw', 'nw-vertical', 'nw-corner', 'nw-horizontal')
        self.add_contour('ne', 'ne-vertical', 'ne-corner', 'ne-horizontal')
        self.add_contour('se', 'se-vertical', 'se-corner', 'se-horizontal')
        self.add_contour('sw', 'sw-vertical', 'sw-corner', 'sw-horizontal')
