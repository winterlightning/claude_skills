"""An open head-profile enclosure facing right, with forehead, nose, chin and neck.

VRECT_XL: visible bounds (4, 0, 60, 64); chosen for the source proportions.
Construction reference: No useful local head-outline match found; coherent circular skull and elliptical rear contour; intentional right-facing asymmetry. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HumanHeadSideProfile(Container64):
    icon_id = 'human-head-side-profile'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('human', 'head', 'side', 'profile')

    def build(self) -> None:
        self.add_line('outline-0', (14, 62), (14, 44))
        self.add_arc('outline-1', (14, 44), (6, 24), radius_x=8, radius_y=20, sweep=True)
        self.add_arc('outline-2', (6, 24), (50, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_line('outline-3', (50, 24), (58, 36))
        self.add_line('outline-4', (58, 36), (52, 36))
        self.add_line('outline-5', (52, 36), (52, 44))
        self.add_arc('outline-6', (52, 44), (44, 52), radius_x=8, radius_y=8, sweep=True)
        self.add_line('outline-7', (44, 52), (40, 52))
        self.add_line('outline-8', (40, 52), (40, 62))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', closed=False)
