"""Medical Cross Symbol: independently authored container.

Construction plan: Single equal-armed cross outline with arm width twenty; mirror both axes.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/cross_a941f1ed-7dc8-4f1e-94e1-4069fcc3c70e.svg. Lucide cross original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (medical-cross-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

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
        self.add_line('cross-1', (23, 6), (41, 6))
        self.add_line('cross-2', (41, 6), (41, 23))
        self.add_line('cross-3', (41, 23), (58, 23))
        self.add_line('cross-4', (58, 23), (58, 41))
        self.add_line('cross-5', (58, 41), (41, 41))
        self.add_line('cross-6', (41, 41), (41, 58))
        self.add_line('cross-7', (41, 58), (23, 58))
        self.add_line('cross-8', (23, 58), (23, 41))
        self.add_line('cross-9', (23, 41), (6, 41))
        self.add_line('cross-10', (6, 41), (6, 23))
        self.add_line('cross-11', (6, 23), (23, 23))
        self.add_line('cross-12', (23, 23), (23, 6))
        self.add_contour('cross', 'cross-1', 'cross-2', 'cross-3', 'cross-4', 'cross-5', 'cross-6', 'cross-7', 'cross-8', 'cross-9', 'cross-10', 'cross-11', 'cross-12', closed=True)
