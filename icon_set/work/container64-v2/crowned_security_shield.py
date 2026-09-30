"""A shield whose top edge forms a three-point crown.

Keyshape VRECT_XL: chosen for the reference silhouette.
Lucide crown: paired crown peaks; the supplied shield sets the body; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (crowned-security-shield VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class CrownedSecurityShield(Container64):
    icon_id = 'crowned-security-shield'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('crowned', 'security', 'shield')

    def build(self) -> None:
        self.add_line('crest-1', (10, 30), (10, 10))
        self.add_line('crest-2', (10, 10), (18, 14))
        self.add_line('crest-3', (18, 14), (32, 4))
        self.add_line('crest-4', (32, 4), (46, 14))
        self.add_line('crest-5', (46, 14), (54, 10))
        self.add_line('crest-6', (54, 10), (54, 30))
        self.add_arc('shield-right', (54, 30), (32, 60), radius_x=37)
        self.add_arc('shield-left', (32, 60), (10, 30), radius_x=37)
        self.add_line('band', (10, 22), (54, 22))
        self.add_contour('crest', 'crest-1', 'crest-2', 'crest-3', 'crest-4', 'crest-5', 'crest-6')
        self.add_contour('shield', 'shield-right', 'shield-left')
        self.relate('connect', 'crest', 'shield')
        self.relate('connect', 'band', 'crest')
