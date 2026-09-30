"""An upright tag enclosure with a peaked top and rounded bottom corners.

Keyshape VRECT_L: (8, 0, 56, 64); chosen for the reference silhouette.
Construction reference: Lucide house: axial roof and equal lower quarter-circle corners. Original and atomic-debug inspected.
No door is added: the source is an empty tag. Deliberate roof corners remain.
Hosting measured with compose.py: plus passes, heart passes, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (upward-pointing-tag VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class UpwardPointingTag(Container64):
    icon_id = 'upward-pointing-tag'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('upward', 'pointing', 'tag')

    def build(self) -> None:
        self.add_line('roof-1', (12, 23), (32, 4))
        self.add_line('roof-2', (32, 4), (52, 23))
        self.add_line('roof-3', (52, 23), (52, 56))
        self.add_arc('se', (52, 56), (48, 60), radius_x=4)
        self.add_line('base', (48, 60), (16, 60))
        self.add_arc('sw', (16, 60), (12, 56), radius_x=4)
        self.add_line('left', (12, 56), (12, 23))
        self.add_contour('outline', 'roof-1', 'roof-2', 'roof-3', 'se', 'base', 'sw', 'left', closed=True)
