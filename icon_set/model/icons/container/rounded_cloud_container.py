"""A cloud outline with a broad central dome and two rounded side lobes.

HRECT_L: (0, 8, 64, 56); chosen for the source silhouette.
Lucide cloud: continuous lobed outline and flat base; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RoundedCloudContainer(Container64):
    icon_id = 'rounded-cloud-container'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('rounded', 'cloud', 'container')

    def build(self) -> None:
        self.add_arc('cloud-0', (14, 26), (14, 54), radius_x=12, radius_y=14, sweep=False)
        self.add_line('cloud-1', (14, 54), (50, 54))
        self.add_arc('cloud-2', (50, 54), (50, 26), radius_x=12, radius_y=14, sweep=False)
        self.add_arc('cloud-3', (50, 26), (32, 10), radius_x=18, radius_y=16, sweep=False)
        self.add_arc('cloud-4', (32, 10), (14, 26), radius_x=18, radius_y=16, sweep=False)
        self.add_contour('cloud', 'cloud-0', 'cloud-1', 'cloud-2', 'cloud-3', 'cloud-4', closed=True)
