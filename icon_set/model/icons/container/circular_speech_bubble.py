"""A round speech enclosure with a lower-left pointed tail. Deliberately asymmetric tail.

Keyshape SQUARE; visible bounds (0, 0, 64, 64); centerline extremes (2, 2)-(62, 62).
Construction reference: Lucide message-circle: broad circular outline and integrated tail, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus does not clear, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (circular-speech-bubble SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class CircularSpeechBubble(Container64):
    icon_id = 'circular-speech-bubble'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('circular', 'speech', 'bubble')

    def build(self) -> None:
        self.add_arc('upper-left', (6, 28), (32, 6), radius_x=26, radius_y=22)
        self.add_arc('upper-right', (32, 6), (58, 28), radius_x=26, radius_y=22)
        self.add_arc('lower-right', (58, 28), (32, 51), radius_x=26, radius_y=23)
        self.add_arc('lower-shoulder', (32, 51), (18, 46), radius_x=18, radius_y=14)
        self.add_line('tail-out', (18, 46), (10, 58))
        self.add_line('tail-in', (10, 58), (12, 41))
        self.add_arc('lower-left', (12, 41), (6, 28), radius_x=24, radius_y=20)
        self.add_contour('outline', 'upper-left', 'upper-right', 'lower-right', 'lower-shoulder', 'tail-out', 'tail-in', 'lower-left', closed=True)
