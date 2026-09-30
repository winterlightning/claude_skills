"""An upright admission ticket with two semicircular edge cutouts.

Keyshape VRECT_L, bounds (8, 0, 56, 64): chosen for the reference proportions.
Lucide construction: ticket: circular notches and matching rounded corners. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (vertical-admission-ticket VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class VerticalAdmissionTicket(Container64):
    icon_id = 'vertical-admission-ticket'
    keyshape = Keyshape.VRECT_M
    aliases = ('admission-pass', 'admission-stub')
    keywords = ('vertical', 'admission', 'ticket', 'tickets', 'card', 'cards', 'pass', 'passes', 'stub', 'stubs')

    def build(self) -> None:
        self.add_line('outline-0', (16, 4), (26, 4))
        self.add_arc('outline-1', (26, 4), (38, 4), radius_x=6, sweep=False)
        self.add_line('outline-2', (38, 4), (48, 4))
        self.add_arc('outline-3', (48, 4), (52, 8), radius_x=4)
        self.add_line('outline-4', (52, 8), (52, 56))
        self.add_arc('outline-5', (52, 56), (48, 60), radius_x=4)
        self.add_line('outline-6', (48, 60), (38, 60))
        self.add_arc('outline-7', (38, 60), (26, 60), radius_x=6, sweep=False)
        self.add_line('outline-8', (26, 60), (16, 60))
        self.add_arc('outline-9', (16, 60), (12, 56), radius_x=4)
        self.add_line('outline-10', (12, 56), (12, 8))
        self.add_arc('outline-11', (12, 8), (16, 4), radius_x=4)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', closed=True)
