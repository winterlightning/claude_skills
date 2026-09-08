"""A shield whose top edge forms a three-point crown.

Keyshape VRECT_XL: chosen for the reference silhouette.
Lucide crown: paired crown peaks; the supplied shield sets the body; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class CrownedSecurityShield(Container64):
    icon_id = 'crowned-security-shield'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('crowned', 'security', 'shield')

    def build(self) -> None:
        self.add_polyline("crest", (6,30), (6,8), (16,12), (32,2), (48,12), (58,8), (58,30))
        self.add_arc('shield-right', (58, 30), (32, 62), radius_x=42, radius_y=42, sweep=True)
        self.add_arc('shield-left', (32, 62), (6, 30), radius_x=42, radius_y=42, sweep=True)
        self.add_contour('shield', 'shield-right', 'shield-left', closed=False)
        self.relate("connect", 'crest', 'shield')
        self.add_line('band', (6, 20), (58, 20))
        self.relate("connect", 'band', 'crest')
