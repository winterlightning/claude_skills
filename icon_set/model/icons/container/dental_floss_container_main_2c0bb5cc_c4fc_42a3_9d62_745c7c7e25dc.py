"""Dental Floss Container: independently authored container.

Construction plan: Rounded floss case plus a continuous trailing thread on the right; folder informs rounded casing only.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/dental floss_2c0bb5cc-c4fc-42a3-9d62-745c7c7e25dc.svg. Lucide folder original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (dental-floss-container-main HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '2c0bb5cc-c4fc-42a3-9d62-745c7c7e25dc'
SOURCE_PATH = 'pictographic-primitives/health/dental floss_2c0bb5cc-c4fc-42a3-9d62-745c7c7e25dc.svg'
AUTHOR = 'claude-opus-5-5'


class DentalFlossContainerMain(Container64):
    icon_id = 'dental-floss-container-main'
    keyshape = Keyshape.HRECT_L
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('dental', 'floss', 'container', 'main')

    def build(self) -> None:
        self.add_line('case-0', (11, 10), (36, 10))
        self.add_arc('case-1', (36, 10), (43, 18), radius_x=7, radius_y=8)
        self.add_line('case-2', (43, 18), (43, 46))
        self.add_arc('case-3', (43, 46), (36, 54), radius_x=7, radius_y=8)
        self.add_line('case-4', (36, 54), (11, 54))
        self.add_arc('case-5', (11, 54), (4, 46), radius_x=7, radius_y=8)
        self.add_line('case-6', (4, 46), (4, 18))
        self.add_arc('case-7', (4, 18), (11, 10), radius_x=7, radius_y=8)
        self.add_line('thread-0', (43, 24), (47, 24))
        self.add_arc('thread-1', (47, 24), (53, 29), radius_x=6, radius_y=5)
        self.add_line('thread-2', (53, 29), (52, 50))
        self.add_arc('thread-3', (52, 50), (60, 50), radius_x=4, sweep=False)
        self.add_contour('case', 'case-0', 'case-1', 'case-2', 'case-3', 'case-4', 'case-5', 'case-6', 'case-7', closed=True)
        self.add_contour('thread', 'thread-0', 'thread-1', 'thread-2', 'thread-3')
        self.relate('connect', 'case', 'thread')
