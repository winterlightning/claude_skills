"""A male-symbol container with a circular enclosure and northeast arrow.

SQUARE: centerline extremes (2,2)-(62,62). The user explicitly confirmed
container classification. Lucide mars original and atomic-debug inform the
circular ring, separate shaft and joined arrowhead. The directional arrow
is deliberately asymmetric; all source-defining parts are retained.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (male-gender-symbol SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
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
        self.add_arc('ring-ne', (41, 19), (50, 36), radius_x=20)
        self.add_arc('ring-se', (50, 36), (28, 58), radius_x=22)
        self.add_arc('ring-sw', (28, 58), (6, 36), radius_x=22)
        self.add_arc('ring-nw', (6, 36), (28, 14), radius_x=22)
        self.add_arc('ring-top', (28, 14), (41, 19), radius_x=19)
        self.add_line('shaft', (41, 19), (58, 6))
        self.add_line('head-1', (43, 6), (58, 6))
        self.add_line('head-2', (58, 6), (58, 22))
        self.add_contour('ring', 'ring-ne', 'ring-se', 'ring-sw', 'ring-nw', 'ring-top', closed=True)
        self.add_contour('head', 'head-1', 'head-2')
        self.relate('connect', 'ring', 'shaft')
        self.relate('connect', 'shaft', 'head')
