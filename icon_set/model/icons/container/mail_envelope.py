"""An envelope enclosure with four short corner folds.

HRECT_L: exact centerline extremes recorded in build.
Construction: Lucide mail, rectangular enclosure and diagonal folds. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (mail-envelope HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class MailEnvelope(Container64):
    icon_id = 'mail-envelope'
    keyshape = Keyshape.HRECT_L
    aliases = ('mail-envelope-icon',)
    keywords = ('mail', 'envelope')

    def build(self) -> None:
        # HRECT_L (was HRECT_M): envelope 4..60 x 10..54 with shorter corner folds, so it holds a symbol of 28+
        # with a 4 px gap (was 20.5). Mirrored on both axes.
        self.add_line('outline-1', (4, 10), (60, 10))
        self.add_line('outline-2', (60, 10), (60, 54))
        self.add_line('outline-3', (60, 54), (4, 54))
        self.add_line('outline-4', (4, 54), (4, 10))
        self.add_line('nw', (4, 10), (12, 15))
        self.add_line('ne', (60, 10), (52, 15))
        self.add_line('sw', (4, 54), (12, 49))
        self.add_line('se', (60, 54), (52, 49))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', closed=True)
        self.relate('connect', 'outline', 'nw')
        self.relate('connect', 'outline', 'ne')
        self.relate('connect', 'outline', 'sw')
        self.relate('connect', 'outline', 'se')
