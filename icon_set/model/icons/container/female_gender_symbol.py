"""A female gender symbol has a circular enclosure and a cross below it.

Authored as a container at the user's explicit request. VRECT_L preserves
its upright proportions: visible (8,0)-(56,64), centerline (10,2)-(54,62).
Lucide venus original and atomic-debug inform the circular outline and
centered connected cross. The supplied reference establishes the subject;
no identity-bearing detail is removed. The circle is centered at (32,24)
with radius 22; the cross is mirrored about x=32.
Hosting measured with compose.py: plus passes, heart does not pass, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (female-gender-symbol VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class FemaleGenderSymbol(Container64):
    icon_id = 'female-gender-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('venus-container', 'female-symbol-container')
    keywords = ('female', 'gender', 'venus', 'woman', 'circle')

    def build(self) -> None:
        self.add_arc('ring-left', (32, 44), (32, 4), radius_x=20)
        self.add_arc('ring-right', (32, 4), (32, 44), radius_x=20)
        self.add_line('stem', (32, 44), (32, 60))
        self.add_line('crossbar', (24, 54), (40, 54))
        self.add_contour('ring', 'ring-left', 'ring-right', closed=True)
        self.relate('connect', 'ring', 'stem')
        self.relate('connect', 'stem', 'crossbar')
