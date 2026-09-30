"""A circular progress enclosure with a continuous arc and three separated dashes.

CIRCLE: visible bounds (0, 0, 64, 64); chosen for the source proportions.
Construction reference: Lucide loader-circle: long circular arc with open end; source retains dashed remainder. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (incomplete-circular-progress-indicator CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class IncompleteCircularProgressIndicator(Container64):
    icon_id = 'incomplete-circular-progress-indicator'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('incomplete', 'circular', 'progress', 'indicator')

    def build(self) -> None:
        self.add_arc('solid-right', (32, 4), (32, 60), radius_x=28)
        self.add_arc('solid-bottom-left', (32, 60), (4, 32), radius_x=28)
        self.add_arc('dash-upper-left', (10, 16), (16, 10), radius_x=27)
        self.add_arc('dash-top', (23, 6), (26, 5), radius_x=28)
        self.add_arc('dash-left', (5, 26), (6, 23), radius_x=28)
        self.add_contour('solid', 'solid-right', 'solid-bottom-left')
