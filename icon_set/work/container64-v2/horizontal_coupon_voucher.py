"""A coupon frame with shallow bowed ends and short corner shoulders.

HRECT_L: visible bounds (0, 8, 64, 56); chosen for the source proportions.
Construction reference: Lucide ticket: continuous side-feature contour; source image takes precedence over erroneous inward-side prose. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (horizontal-coupon-voucher HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class HorizontalCouponVoucher(Container64):
    icon_id = 'horizontal-coupon-voucher'
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('horizontal', 'coupon', 'voucher')

    def build(self) -> None:
        self.add_line('outline-0', (9, 12), (55, 12))
        self.add_line('outline-1', (55, 12), (55, 20))
        self.add_arc('outline-2', (55, 20), (55, 44), radius_x=5, radius_y=12)
        self.add_line('outline-3', (55, 44), (55, 52))
        self.add_line('outline-4', (55, 52), (9, 52))
        self.add_line('outline-5', (9, 52), (9, 44))
        self.add_arc('outline-6', (9, 44), (9, 20), radius_x=5, radius_y=12)
        self.add_line('outline-7', (9, 20), (9, 12))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
