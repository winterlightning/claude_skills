"""Five Pointed Star Symbol: independently authored container.

Construction plan: One five-point outline, mirrored about the vertical axis; no inner symbol.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.svg. Lucide star original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (five-point-star-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): fuller star (inner corners pushed out 1.5x) so a container symbol has room: 21-unit square with a 4 px gap, up from 11.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'c5b95603-1163-4ea7-85f6-90c9f169e889'
SOURCE_PATH = 'pictographic-primitives/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.svg'
AUTHOR = 'claude-opus-5-5'


class FivePointStarContainer(Container64):
    icon_id = 'five-point-star-container'
    keyshape = Keyshape.SQUARE
    category = 'holidays'
    categories = ('holidays', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('five', 'point', 'star', 'container')

    def build(self) -> None:
        # Tips fixed on the keyshape; the inner corners sit 1.5x further from (32,35) than a classic star so the
        # body holds a symbol square of 21 (4 px gap) instead of 11. Mirrored about x = 32.
        tips = [(32, 6), (58, 25), (50, 58), (14, 58), (6, 25)]
        inner = [(44, 20), (50, 38), (32, 53), (14, 38), (20, 20)]
        ring = [p for pair in zip(tips, inner) for p in pair]
        for n, (a, b) in enumerate(zip(ring, ring[1:] + ring[:1]), 1):
            self.add_line(f'star-{n}', a, b)
        self.add_contour('star', *(f'star-{n}' for n in range(1, 11)), closed=True)
