"""A landscape phone enclosure with a left bezel divider.

HRECT_M: visible bounds (0, 12, 64, 52); chosen for the source proportions.
Construction reference: Lucide smartphone: consistent quarter-circle corners. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus blocked, heart blocked, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class HorizontalMobilePhone(Container64):
    icon_id = 'horizontal-mobile-phone'
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('horizontal', 'mobile', 'phone')

    def build(self) -> None:
        self.add_line('outline-0', (8, 14), (56, 14))
        self.add_arc('outline-1', (56, 14), (62, 20), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-2', (62, 20), (62, 44))
        self.add_arc('outline-3', (62, 44), (56, 50), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-4', (56, 50), (8, 50))
        self.add_arc('outline-5', (8, 50), (2, 44), radius_x=6, radius_y=6, sweep=True)
        self.add_line('outline-6', (2, 44), (2, 20))
        self.add_arc('outline-7', (2, 20), (8, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_line('bezel', (12,14), (12,50))
        self.relate('connect', 'outline', 'bezel')
