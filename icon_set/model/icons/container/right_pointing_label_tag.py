"""A right-pointing label outline with rounded left corners.

Keyshape HRECT_M: (0, 12, 64, 52); preserves the reference proportions.
Reference: batch_11 source render; Lucide tag informs the continuous outline and deliberate pointed end.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (right-pointing-label-tag HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RightPointingLabelTag(Container64):
    icon_id = 'right-pointing-label-tag'
    keyshape = Keyshape.HRECT_M
    aliases = ('wide-label-tag',)
    keywords = ('right', 'pointing', 'label', 'tag')

    def build(self) -> None:
        self.add_line('top', (9, 12), (43, 12))
        self.add_line('tip-upper', (43, 12), (60, 32))
        self.add_line('tip-lower', (60, 32), (43, 52))
        self.add_line('bottom', (43, 52), (9, 52))
        self.add_arc('bottom-left', (9, 52), (4, 47), radius_x=5)
        self.add_line('left', (4, 47), (4, 17))
        self.add_arc('top-left', (4, 17), (9, 12), radius_x=5)
        self.add_contour('outline', 'top', 'tip-upper', 'tip-lower', 'bottom', 'bottom-left', 'left', 'top-left', closed=True)
