"""A male-symbol container with a circular enclosure and northeast arrow.

SQUARE: centerline extremes (2,2)-(62,62). The user explicitly confirmed
container classification. Lucide mars original and atomic-debug inform the
circular ring, separate shaft and joined arrowhead. The directional arrow
is deliberately asymmetric; all source-defining parts are retained.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (male-gender-symbol SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class MaleGenderSymbol(Container64):
    icon_id = 'male-gender-symbol'
    keyshape = Keyshape.SQUARE
    aliases = ('mars-symbol-container',)
    keywords = ('male', 'gender', 'mars', 'circle', 'arrow')

    def build(self) -> None:
        # Ring r24 about (30,34) (was r22 about (28,36)) touching the keyshape left and bottom; the arrow leaves it
        # at 45 degrees to the top-right corner. The ring holds a symbol of 25 with a 4 px gap (was 22).
        self.add_arc('ring-ne', (47, 17), (54, 34), radius_x=24)
        self.add_arc('ring-se', (54, 34), (30, 58), radius_x=24)
        self.add_arc('ring-sw', (30, 58), (6, 34), radius_x=24)
        self.add_arc('ring-nw', (6, 34), (30, 10), radius_x=24)
        self.add_arc('ring-top', (30, 10), (47, 17), radius_x=24)
        self.add_line('shaft', (47, 17), (58, 6))
        self.add_line('head-1', (46, 6), (58, 6))
        self.add_line('head-2', (58, 6), (58, 18))
        self.add_contour('ring', 'ring-ne', 'ring-se', 'ring-sw', 'ring-nw', 'ring-top', closed=True)
        self.add_contour('head', 'head-1', 'head-2')
        self.relate('connect', 'ring', 'shaft')
        self.relate('connect', 'shaft', 'head')
