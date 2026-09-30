"""A cloud outline with a broad central dome and two rounded side lobes.

HRECT_L: (0, 8, 64, 56); chosen for the source silhouette.
Lucide cloud: continuous lobed outline and flat base; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rounded-cloud-container HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundedCloudContainer(Container64):
    icon_id = 'rounded-cloud-container'
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('rounded', 'cloud', 'container')

    def build(self) -> None:
        self.add_arc('cloud-0-a', (15, 27), (4, 40), radius_x=11, radius_y=13, sweep=False)
        self.add_arc('cloud-0-b', (4, 40), (15, 52), radius_x=12, radius_y=14, sweep=False)
        self.add_line('cloud-1', (15, 52), (49, 52))
        self.add_arc('cloud-2-a', (49, 52), (60, 40), radius_x=12, radius_y=14, sweep=False)
        self.add_arc('cloud-2-b', (60, 40), (49, 27), radius_x=11, radius_y=13, sweep=False)
        self.add_arc('cloud-3', (49, 27), (32, 12), radius_x=17, radius_y=15, sweep=False)
        self.add_arc('cloud-4', (32, 12), (15, 27), radius_x=17, radius_y=15, sweep=False)
        self.add_contour('cloud', 'cloud-0-a', 'cloud-0-b', 'cloud-1', 'cloud-2-a', 'cloud-2-b', 'cloud-3', 'cloud-4', closed=True)
