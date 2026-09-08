"""A circular prohibition enclosure crossed by a descending slash.

Keyshape CIRCLE: (0, 0, 64, 64); chosen for the reference silhouette.
Construction reference: Lucide ban: circular outline with a connected diameter. Original and atomic-debug inspected.
Integer on-circle endpoints use a 3:4 direction to preserve exact circle geometry and genuine contact. The diagonal is intentional.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class UniversalProhibitedSymbol(Container64):
    icon_id = 'universal-prohibited-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('universal', 'prohibited', 'symbol')

    def build(self) -> None:
        self.add_arc('ring-a', (14, 8), (50, 56), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('ring-b', (50, 56), (14, 8), radius_x=30, radius_y=30, sweep=True)
        self.add_contour('ring', 'ring-a', 'ring-b', closed=True)
        self.add_line('slash', (14, 8), (50, 56))
        self.relate("connect", 'ring', 'slash')
