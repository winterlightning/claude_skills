"""A coupon frame with shallow bowed ends and short corner shoulders.

HRECT_L: visible bounds (0, 8, 64, 56); chosen for the source proportions.
Construction reference: Lucide ticket: continuous side-feature contour; source image takes precedence over erroneous inward-side prose. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HorizontalCouponVoucher(Container64):
    icon_id = 'horizontal-coupon-voucher'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('horizontal', 'coupon', 'voucher')

    def build(self) -> None:
        self.add_line('outline-0', (7, 10), (57, 10))
        self.add_line('outline-1', (57, 10), (57, 18))
        self.add_arc('outline-2', (57, 18), (57, 46), radius_x=5, radius_y=14, sweep=True)
        self.add_line('outline-3', (57, 46), (57, 54))
        self.add_line('outline-4', (57, 54), (7, 54))
        self.add_line('outline-5', (7, 54), (7, 46))
        self.add_arc('outline-6', (7, 46), (7, 18), radius_x=5, radius_y=14, sweep=True)
        self.add_line('outline-7', (7, 18), (7, 10))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
