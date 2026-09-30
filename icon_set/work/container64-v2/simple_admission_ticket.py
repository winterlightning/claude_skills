"""A rectangular admission ticket has inward semicircular side notches.

HRECT_L: visible bounds (0, 8, 64, 56), chosen for the subject proportions.
Lucide ticket: mirrored concave circular cutouts between straight rails; original and atomic-debug inspected.
The plain source has no perforation marks; no features dropped. Both axes mirrored.
Hosting measured with compose.py: plus blocked, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-admission-ticket HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleAdmissionTicket(Container64):
    icon_id = 'simple-admission-ticket'
    keyshape = Keyshape.HRECT_M
    aliases = ('admission-ticket',)
    keywords = ('simple', 'admission', 'ticket')

    def build(self) -> None:
        self.add_line('top', (4, 12), (60, 12))
        self.add_line('right-upper', (60, 12), (60, 23))
        self.add_arc('right-notch', (60, 23), (60, 41), radius_x=9, sweep=False)
        self.add_line('right-lower', (60, 41), (60, 52))
        self.add_line('bottom', (60, 52), (4, 52))
        self.add_line('left-lower', (4, 52), (4, 41))
        self.add_arc('left-notch', (4, 41), (4, 23), radius_x=9, sweep=False)
        self.add_line('left-upper', (4, 23), (4, 12))
        self.add_contour('ticket', 'top', 'right-upper', 'right-notch', 'right-lower', 'bottom', 'left-lower', 'left-notch', 'left-upper', closed=True)
