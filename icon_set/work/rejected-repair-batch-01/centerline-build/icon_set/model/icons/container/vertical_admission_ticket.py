"""An upright admission ticket with two semicircular edge cutouts.

Keyshape VRECT_L, bounds (8, 0, 56, 64): chosen for the reference proportions.
Lucide construction: ticket: circular notches and matching rounded corners. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class VerticalAdmissionTicket(Container64):
    icon_id = 'vertical-admission-ticket'
    keyshape = Keyshape.VRECT_L
    aliases = ('admission-pass', 'admission-stub')
    keywords = ('vertical', 'admission', 'ticket', 'tickets', 'card', 'cards', 'pass', 'passes', 'stub', 'stubs')

    def build(self) -> None:
        self.add_line('outline-0', (14, 2), (25, 2))
        self.add_arc('outline-1', (25, 2), (39, 2), radius_x=7, radius_y=7, sweep=False)
        self.add_line('outline-2', (39, 2), (50, 2))
        self.add_arc('outline-3', (50, 2), (54, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-4', (54, 6), (54, 58))
        self.add_arc('outline-5', (54, 58), (50, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-6', (50, 62), (39, 62))
        self.add_arc('outline-7', (39, 62), (25, 62), radius_x=7, radius_y=7, sweep=False)
        self.add_line('outline-8', (25, 62), (14, 62))
        self.add_arc('outline-9', (14, 62), (10, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('outline-10', (10, 58), (10, 6))
        self.add_arc('outline-11', (10, 6), (14, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', closed=True)
