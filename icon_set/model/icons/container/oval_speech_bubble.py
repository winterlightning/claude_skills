"""Increase oval height, preserving the wide elliptical bubble and lower-left tail.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (oval-speech-bubble HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class OvalSpeechBubble(Container64):
    icon_id = 'oval-speech-bubble'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # SQUARE (was HRECT_L): a rounder oval, rx 26 ry 24 about (32,30), with the tail to the bottom-left corner;
        # holds a symbol of 26 with a 4 px gap (was 22.5 in the flatter oval).
        self.add_arc('outline-0', (6, 30), (32, 6), radius_x=26, radius_y=24)
        self.add_arc('outline-1', (32, 6), (58, 30), radius_x=26, radius_y=24)
        self.add_arc('outline-2', (58, 30), (32, 54), radius_x=26, radius_y=24)
        self.add_arc('outline-3', (32, 54), (18, 50), radius_x=26, radius_y=24)
        self.add_line('outline-4', (18, 50), (8, 58))
        self.add_line('outline-5', (8, 58), (11, 44))
        self.add_arc('outline-6', (11, 44), (6, 30), radius_x=26, radius_y=24)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)
