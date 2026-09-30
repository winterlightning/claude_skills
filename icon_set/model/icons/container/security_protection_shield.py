"""A pointed shield encloses an open protective field.

VRECT_XL: visible bounds (4, 0, 60, 64), chosen for the subject proportions.
Lucide shield: mirrored shoulders flowing into a tapered bowl; original and atomic-debug inspected.
Source crest and pointed base retained; bilateral symmetry, no details dropped.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (security-protection-shield VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SecurityProtectionShield(Container64):
    icon_id = 'security-protection-shield'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('security', 'protection', 'shield')

    def build(self) -> None:
        self.add_line('crest-1', (10, 27), (10, 14))
        self.add_line('crest-2', (10, 14), (32, 4))
        self.add_line('crest-3', (32, 4), (54, 14))
        self.add_line('crest-4', (54, 14), (54, 27))
        self.add_arc('bowl-right', (54, 27), (32, 60), radius_x=36)
        self.add_arc('bowl-left', (32, 60), (10, 27), radius_x=36)
        self.add_contour('crest', 'crest-1', 'crest-2', 'crest-3', 'crest-4')
        self.add_contour('bowl', 'bowl-right', 'bowl-left')
        self.relate('connect', 'crest', 'bowl')
