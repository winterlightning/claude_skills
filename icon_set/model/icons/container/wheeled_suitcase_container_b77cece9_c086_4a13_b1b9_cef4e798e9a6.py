"""Travel Suitcase with Wheels: independently authored container.

Construction plan: Rounded suitcase, centered handle and two matching short wheels.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg. Lucide luggage original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (wheeled-suitcase-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'b77cece9-c086-4a13-b1b9-cef4e798e9a6'
SOURCE_PATH = 'pictographic-primitives/travel/baggage_b77cece9-c086-4a13-b1b9-cef4e798e9a6.svg'
AUTHOR = 'claude-opus-5-5'


class WheeledSuitcaseContainer(Container64):
    icon_id = 'wheeled-suitcase-container'
    keyshape = Keyshape.SQUARE
    category = 'travel'
    categories = ('travel', 'state')
    aliases = ()
    keywords = ('wheeled', 'suitcase', 'container')

    def build(self) -> None:
        self.add_line('case-0', (12, 18), (52, 18))
        self.add_arc('case-1', (52, 18), (58, 24), radius_x=6)
        self.add_line('case-2', (58, 24), (58, 44))
        self.add_arc('case-3', (58, 44), (52, 50), radius_x=6)
        self.add_line('case-4', (52, 50), (12, 50))
        self.add_arc('case-5', (12, 50), (6, 44), radius_x=6)
        self.add_line('case-6', (6, 44), (6, 24))
        self.add_arc('case-7', (6, 24), (12, 18), radius_x=6)
        self.add_line('handle-0', (24, 18), (24, 10))
        self.add_arc('handle-1', (24, 10), (28, 6), radius_x=4)
        self.add_line('handle-2', (28, 6), (36, 6))
        self.add_arc('handle-3', (36, 6), (40, 10), radius_x=4)
        self.add_line('handle-4', (40, 10), (40, 18))
        self.add_line('wheel-16', (18, 50), (18, 58))
        self.add_line('wheel-48', (46, 50), (46, 58))
        self.add_contour('case', 'case-0', 'case-1', 'case-2', 'case-3', 'case-4', 'case-5', 'case-6', 'case-7', closed=True)
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2', 'handle-3', 'handle-4')
        self.relate('connect', 'handle', 'case')
        self.relate('connect', 'case', 'wheel-16')
        self.relate('connect', 'case', 'wheel-48')
