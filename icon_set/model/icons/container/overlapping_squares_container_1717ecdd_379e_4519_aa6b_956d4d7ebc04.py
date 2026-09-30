"""Overlapping Rounded Squares: independently authored container.

Construction plan: Front rounded square occludes the rear outline; retain offset and equal proportions.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/duplicate_1717ecdd-379e-4519-aa6b-956d4d7ebc04.svg. Lucide squares-exclude original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (overlapping-squares-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '1717ecdd-379e-4519-aa6b-956d4d7ebc04'
SOURCE_PATH = 'pictographic-primitives/interface-essential/duplicate_1717ecdd-379e-4519-aa6b-956d4d7ebc04.svg'
AUTHOR = 'claude-opus-5-5'


class OverlappingSquaresContainer(Container64):
    icon_id = 'overlapping-squares-container'
    keyshape = Keyshape.SQUARE
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('overlapping', 'squares', 'container')

    def build(self) -> None:
        self.add_line('front-0', (10, 6), (40, 6))
        self.add_arc('front-1', (40, 6), (44, 10), radius_x=4)
        self.add_line('front-2', (44, 10), (44, 40))
        self.add_arc('front-3', (44, 40), (40, 44), radius_x=4)
        self.add_line('front-4', (40, 44), (10, 44))
        self.add_arc('front-5', (10, 44), (6, 40), radius_x=4)
        self.add_line('front-6', (6, 40), (6, 10))
        self.add_arc('front-7', (6, 10), (10, 6), radius_x=4)
        self.add_line('rear-0', (44, 20), (54, 20))
        self.add_arc('rear-1', (54, 20), (58, 24), radius_x=4)
        self.add_line('rear-2', (58, 24), (58, 54))
        self.add_arc('rear-3', (58, 54), (54, 58), radius_x=4)
        self.add_line('rear-4', (54, 58), (24, 58))
        self.add_arc('rear-5', (24, 58), (20, 54), radius_x=4)
        self.add_line('rear-6', (20, 54), (20, 44))
        self.add_contour('front', 'front-0', 'front-1', 'front-2', 'front-3', 'front-4', 'front-5', 'front-6', 'front-7', closed=True)
        self.add_contour('rear', 'rear-0', 'rear-1', 'rear-2', 'rear-3', 'rear-4', 'rear-5', 'rear-6')
        self.relate('connect', 'front', 'rear')
