"""Medical Cross Symbol: independently authored container.

Construction plan: Single equal-armed cross outline with arm width twenty; mirror both axes.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.svg. Lucide cross original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (medical-cross-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): arms widened from 18 to 28 (stubs 12) so a container symbol has room: 19.5-unit square with a 4 px gap, up from 9.5.
Width 34 was tried first and read as a notched square, not a cross; 28 is the widest that still reads as a cross.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e'
SOURCE_PATH = 'pictographic-primitives/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.svg'
AUTHOR = 'claude-opus-5-5'


class MedicalCrossContainer(Container64):
    icon_id = 'medical-cross-container'
    keyshape = Keyshape.SQUARE
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('medical', 'cross', 'container')

    def build(self) -> None:
        # Equal-armed cross, arm width 28 (18..46), arms reaching the keyshape at 6 and 58; mirrored on both axes.
        # The centre holds a symbol square of 19.5 (4 px gap) instead of 9.5 with the old width-18 arms.
        a, b = 18, 46
        ring = [(a, 6), (b, 6), (b, a), (58, a), (58, b), (b, b), (b, 58), (a, 58), (a, b), (6, b), (6, a), (a, a)]
        for n, (p, q) in enumerate(zip(ring, ring[1:] + ring[:1]), 1):
            self.add_line(f'cross-{n}', p, q)
        self.add_contour('cross', *(f'cross-{n}' for n in range(1, 13)), closed=True)
