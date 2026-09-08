"""A round speech enclosure with a lower-left pointed tail. Deliberately asymmetric tail.

Keyshape SQUARE; visible bounds (0, 0, 64, 64); centerline extremes (2, 2)-(62, 62).
Construction reference: Lucide message-circle: broad circular outline and integrated tail, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus does not clear, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class CircularSpeechBubble(Container64):
    icon_id = 'circular-speech-bubble'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('circular', 'speech', 'bubble')

    def build(self) -> None:
        self.add_arc('upper-left', (2, 27), (32, 2), radius_x=30, radius_y=25, sweep=True, large_arc=False)
        self.add_arc('upper-right', (32, 2), (62, 27), radius_x=30, radius_y=25, sweep=True, large_arc=False)
        self.add_arc('lower-right', (62, 27), (32, 52), radius_x=30, radius_y=25, sweep=True, large_arc=False)
        self.add_arc('lower-shoulder', (32, 52), (14, 47), radius_x=30, radius_y=25, sweep=True, large_arc=False)
        self.add_line('tail-out', (14, 47), (6, 62))
        self.add_line('tail-in', (6, 62), (8, 42))
        self.add_arc('lower-left', (8, 42), (2, 27), radius_x=30, radius_y=25, sweep=True, large_arc=False)
        self.add_contour('outline', 'upper-left', 'upper-right', 'lower-right', 'lower-shoulder', 'tail-out', 'tail-in', 'lower-left', closed=True)
