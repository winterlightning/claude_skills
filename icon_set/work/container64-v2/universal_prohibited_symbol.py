"""A circular prohibition enclosure crossed by a descending slash.

Keyshape CIRCLE: (0, 0, 64, 64); chosen for the reference silhouette.
Construction reference: Lucide ban: circular outline with a connected diameter. Original and atomic-debug inspected.
Integer on-circle endpoints use a 3:4 direction to preserve exact circle geometry and genuine contact. The diagonal is intentional.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (universal-prohibited-symbol CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: ring on cardinal r28 nodes; slash ends just inside the ring at r27.8.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class UniversalProhibitedSymbol(Container64):
    icon_id = 'universal-prohibited-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('universal', 'prohibited', 'symbol')

    def build(self) -> None:
        self.add_arc('ring-a', (4, 32), (60, 32), radius_x=28)
        self.add_arc('ring-b', (60, 32), (4, 32), radius_x=28)
        self.add_contour('ring', 'ring-a', 'ring-b', closed=True)
        self.add_line('slash', (15, 10), (49, 54))
        self.relate('connect', 'ring', 'slash')
