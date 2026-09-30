"""A shield with a gently arched top and a rounded taper to its lower point.

VRECT_XL: (4, 0, 60, 64); chosen for the source silhouette.
Lucide shield: mirrored sides and continuous curved lower bowl; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (security-shield VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class SecurityShield(Container64):
    icon_id = 'security-shield'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('security', 'shield')

    def build(self) -> None:
        self.add_arc('shield-0', (10, 12), (32, 4), radius_x=22, radius_y=8)
        self.add_arc('shield-1', (32, 4), (54, 12), radius_x=22, radius_y=8)
        self.add_line('shield-2', (54, 12), (54, 32))
        self.add_arc('shield-3', (54, 32), (32, 60), radius_x=29)
        self.add_arc('shield-4', (32, 60), (10, 32), radius_x=29)
        self.add_line('shield-5', (10, 32), (10, 12))
        self.add_contour('shield', 'shield-0', 'shield-1', 'shield-2', 'shield-3', 'shield-4', 'shield-5', closed=True)
