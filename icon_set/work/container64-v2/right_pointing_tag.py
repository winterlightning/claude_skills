"""A right-pointing label outline with rounded left corners.

Keyshape SQUARE: (0, 0, 64, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide tag informs the continuous outline and deliberate pointed end.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (right-pointing-tag SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RightPointingTag(Container64):
    icon_id = 'right-pointing-tag'
    keyshape = Keyshape.SQUARE
    aliases = ('pointed-tag',)
    keywords = ('right', 'pointing', 'tag')

    def build(self) -> None:
        self.add_line('top', (11, 6), (42, 6))
        self.add_line('tip-upper', (42, 6), (58, 32))
        self.add_line('tip-lower', (58, 32), (42, 58))
        self.add_line('bottom', (42, 58), (11, 58))
        self.add_arc('bottom-left', (11, 58), (6, 53), radius_x=5)
        self.add_line('left', (6, 53), (6, 11))
        self.add_arc('top-left', (6, 11), (11, 6), radius_x=5)
        self.add_contour('outline', 'top', 'tip-upper', 'tip-lower', 'bottom', 'bottom-left', 'left', 'top-left', closed=True)
