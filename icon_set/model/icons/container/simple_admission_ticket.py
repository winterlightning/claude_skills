"""A rectangular admission ticket has inward semicircular side notches.

HRECT_L: visible bounds (0, 8, 64, 56), chosen for the subject proportions.
Lucide ticket: mirrored concave circular cutouts between straight rails; original and atomic-debug inspected.
The plain source has no perforation marks; no features dropped. Both axes mirrored.
Hosting measured with compose.py: plus blocked, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SimpleAdmissionTicket(Container64):
    icon_id = 'simple-admission-ticket'
    keyshape = Keyshape.HRECT_L
    aliases = ('admission-ticket',)
    keywords = ('simple', 'admission', 'ticket')

    def build(self) -> None:
        self.add_line('top', (2, 10), (62, 10))
        self.add_line('right-upper', (62, 10), (62, 22))
        self.add_arc('right-notch', (62, 22), (62, 42), radius_x=10, radius_y=10, sweep=False)
        self.add_line('right-lower', (62, 42), (62, 54))
        self.add_line('bottom', (62, 54), (2, 54))
        self.add_line('left-lower', (2, 54), (2, 42))
        self.add_arc('left-notch', (2, 42), (2, 22), radius_x=10, radius_y=10, sweep=False)
        self.add_line('left-upper', (2, 22), (2, 10))
        self.add_contour('ticket', 'top', 'right-upper', 'right-notch', 'right-lower', 'bottom', 'left-lower', 'left-notch', 'left-upper', closed=True)
