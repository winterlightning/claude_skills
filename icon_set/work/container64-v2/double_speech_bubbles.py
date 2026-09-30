"""Deepen the front message while preserving both speech tails and the rear bubble.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (double-speech-bubbles SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class DoubleSpeechBubbles(Container64):
    icon_id = 'double-speech-bubbles'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('front-0', (9, 6), (44, 6))
        self.add_arc('front-1', (44, 6), (48, 9), radius_x=4, radius_y=3)
        self.add_line('front-2', (48, 9), (48, 40))
        self.add_arc('front-3', (48, 40), (44, 44), radius_x=4)
        self.add_line('front-4', (44, 44), (24, 44))
        self.add_line('front-5', (24, 44), (12, 52))
        self.add_line('front-6', (12, 52), (12, 44))
        self.add_line('front-7', (12, 44), (9, 44))
        self.add_arc('front-8', (9, 44), (6, 40), radius_x=3, radius_y=4)
        self.add_line('front-9', (6, 40), (6, 9))
        self.add_arc('front-10', (6, 9), (9, 6), radius_x=3)
        self.add_line('rear-0', (48, 30), (55, 30))
        self.add_arc('rear-1', (55, 30), (58, 34), radius_x=3, radius_y=4)
        self.add_line('rear-2', (58, 34), (58, 50))
        self.add_line('rear-3', (58, 50), (55, 50))
        self.add_line('rear-4', (55, 50), (55, 58))
        self.add_line('rear-5', (55, 58), (42, 52))
        self.add_line('rear-6', (42, 52), (34, 52))
        self.add_arc('rear-7', (34, 52), (30, 48), radius_x=4)
        self.add_line('rear-8', (30, 48), (30, 44))
        self.add_contour('front', 'front-0', 'front-1', 'front-2', 'front-3', 'front-4', 'front-5', 'front-6', 'front-7', 'front-8', 'front-9', 'front-10', closed=True)
        self.add_contour('rear', 'rear-0', 'rear-1', 'rear-2', 'rear-3', 'rear-4', 'rear-5', 'rear-6', 'rear-7', 'rear-8')
        self.relate('connect', 'front', 'rear')
