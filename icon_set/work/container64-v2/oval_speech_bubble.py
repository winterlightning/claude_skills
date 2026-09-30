"""Increase oval height, preserving the wide elliptical bubble and lower-left tail.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (oval-speech-bubble HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class OvalSpeechBubble(Container64):
    icon_id = 'oval-speech-bubble'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_arc('outline-0', (4, 30), (32, 10), radius_x=28, radius_y=20)
        self.add_arc('outline-1', (32, 10), (60, 30), radius_x=28, radius_y=20)
        self.add_arc('outline-2', (60, 30), (32, 50), radius_x=28, radius_y=20)
        self.add_arc('outline-3', (32, 50), (16, 45), radius_x=28, radius_y=20)
        self.add_line('outline-4', (16, 45), (8, 54))
        self.add_line('outline-5', (8, 54), (10, 40))
        self.add_arc('outline-6', (10, 40), (4, 30), radius_x=28, radius_y=20)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)
