"""A pointed shield encloses an open protective field.

VRECT_XL: visible bounds (4, 0, 60, 64), chosen for the subject proportions.
Lucide shield: mirrored shoulders flowing into a tapered bowl; original and atomic-debug inspected.
Source crest and pointed base retained; bilateral symmetry, no details dropped.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SecurityProtectionShield(Container64):
    icon_id = 'security-protection-shield'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('security', 'protection', 'shield')

    def build(self) -> None:
        self.add_polyline('crest', (6, 26), (6, 12), (32, 2), (58, 12), (58, 26), closed=False)
        self.add_arc('bowl-right', (58, 26), (32, 62), radius_x=38, radius_y=38, sweep=True)
        self.add_arc('bowl-left', (32, 62), (6, 26), radius_x=38, radius_y=38, sweep=True)
        self.add_contour('bowl', 'bowl-right', 'bowl-left', closed=False)
        self.relate("connect", 'crest', 'bowl')
