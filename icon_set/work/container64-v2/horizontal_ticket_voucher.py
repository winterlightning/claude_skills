"""A wide ticket enclosure with semicircular tabs on both ends.

HRECT_S: visible bounds (0, 16, 64, 48); chosen for the source proportions.
Construction reference: Lucide ticket: joined straight rails and circular side features; source specifies outward tabs. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (horizontal-ticket-voucher HRECT_S -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: redrawn for HRECT_M: 28x40 body with r14 end caps that reach the sides.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class HorizontalTicketVoucher(Container64):
    icon_id = 'horizontal-ticket-voucher'
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('horizontal', 'ticket', 'voucher')

    def build(self) -> None:
        self.add_line('outline-0', (18, 12), (46, 12))
        self.add_line('outline-1', (46, 12), (46, 18))
        self.add_arc('outline-2', (46, 18), (46, 46), radius_x=14)
        self.add_line('outline-3', (46, 46), (46, 52))
        self.add_line('outline-4', (46, 52), (18, 52))
        self.add_line('outline-5', (18, 52), (18, 46))
        self.add_arc('outline-6', (18, 46), (18, 18), radius_x=14)
        self.add_line('outline-7', (18, 18), (18, 12))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
