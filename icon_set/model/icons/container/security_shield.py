"""A shield with a gently arched top and a rounded taper to its lower point.

VRECT_XL: (4, 0, 60, 64); chosen for the source silhouette.
Lucide shield: mirrored sides and continuous curved lower bowl; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SecurityShield(Container64):
    icon_id = 'security-shield'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('security', 'shield')

    def build(self) -> None:
        self.add_arc('shield-0', (6, 10), (32, 2), radius_x=26, radius_y=8, sweep=True)
        self.add_arc('shield-1', (32, 2), (58, 10), radius_x=26, radius_y=8, sweep=True)
        self.add_line('shield-2', (58, 10), (58, 32))
        self.add_arc('shield-3', (58, 32), (32, 62), radius_x=31, radius_y=31, sweep=True)
        self.add_arc('shield-4', (32, 62), (6, 32), radius_x=31, radius_y=31, sweep=True)
        self.add_line('shield-5', (6, 32), (6, 10))
        self.add_contour('shield', 'shield-0', 'shield-1', 'shield-2', 'shield-3', 'shield-4', 'shield-5', closed=True)
