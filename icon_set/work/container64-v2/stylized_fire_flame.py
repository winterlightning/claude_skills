"""An asymmetric flame enclosure with two pointed tongues and a rounded base.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide flame: curved bowl and uneven flame tongues; asymmetry preserves upward movement; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (stylized-fire-flame VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class StylizedFireFlame(Container64):
    icon_id = 'stylized-fire-flame'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('stylized', 'fire', 'flame')

    def build(self) -> None:
        self.add_arc('flame-0', (30, 4), (52, 38), radius_x=50)
        self.add_arc('flame-1', (52, 38), (32, 60), radius_x=20, radius_y=22)
        self.add_arc('flame-2', (32, 60), (12, 38), radius_x=20, radius_y=22)
        self.add_arc('flame-3', (12, 38), (19, 26), radius_x=14)
        self.add_arc('flame-4', (19, 26), (21, 12), radius_x=39, sweep=False)
        self.add_arc('flame-5', (21, 12), (28, 18), radius_x=12)
        self.add_arc('flame-6', (28, 18), (30, 4), radius_x=33, sweep=False)
        self.add_contour('flame', 'flame-0', 'flame-1', 'flame-2', 'flame-3', 'flame-4', 'flame-5', 'flame-6', closed=True)
