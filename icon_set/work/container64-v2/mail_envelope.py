"""An envelope enclosure with four short corner folds.

HRECT_L: exact centerline extremes recorded in build.
Construction: Lucide mail, rectangular enclosure and diagonal folds. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (mail-envelope HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class MailEnvelope(Container64):
    icon_id = 'mail-envelope'
    keyshape = Keyshape.HRECT_M
    aliases = ('mail-envelope-icon',)
    keywords = ('mail', 'envelope')

    def build(self) -> None:
        self.add_line('outline-1', (4, 12), (60, 12))
        self.add_line('outline-2', (60, 12), (60, 52))
        self.add_line('outline-3', (60, 52), (4, 52))
        self.add_line('outline-4', (4, 52), (4, 12))
        self.add_line('nw', (4, 12), (16, 20))
        self.add_line('ne', (60, 12), (48, 20))
        self.add_line('sw', (4, 52), (16, 44))
        self.add_line('se', (60, 52), (48, 44))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', closed=True)
        self.relate('connect', 'outline', 'nw')
        self.relate('connect', 'outline', 'ne')
        self.relate('connect', 'outline', 'sw')
        self.relate('connect', 'outline', 'se')
