"""A wide ticket enclosure with semicircular tabs on both ends.

HRECT_S: visible bounds (0, 16, 64, 48); chosen for the source proportions.
Construction reference: Lucide ticket: joined straight rails and circular side features; source specifies outward tabs. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class HorizontalTicketVoucher(Container64):
    icon_id = 'horizontal-ticket-voucher'
    keyshape = Keyshape.HRECT_S
    aliases = ()
    keywords = ('horizontal', 'ticket', 'voucher')

    def build(self) -> None:
        self.add_line('outline-0', (12, 18), (52, 18))
        self.add_line('outline-1', (52, 18), (52, 22))
        self.add_arc('outline-2', (52, 22), (52, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_line('outline-3', (52, 42), (52, 46))
        self.add_line('outline-4', (52, 46), (12, 46))
        self.add_line('outline-5', (12, 46), (12, 42))
        self.add_arc('outline-6', (12, 42), (12, 22), radius_x=10, radius_y=10, sweep=True)
        self.add_line('outline-7', (12, 22), (12, 18))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
