"""A right-pointing label outline with rounded left corners.

Keyshape SQUARE: (0, 0, 64, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide tag informs the continuous outline and deliberate pointed end.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart passes, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class RightPointingTag(Container64):
    icon_id = 'right-pointing-tag'
    keyshape = Keyshape.SQUARE
    aliases = ('pointed-tag',)
    keywords = ('right', 'pointing', 'tag')

    def build(self) -> None:
        self.add_line('top', (7, 2), (44, 2))
        self.add_line('tip-upper', (44, 2), (62, 32))
        self.add_line('tip-lower', (62, 32), (44, 62))
        self.add_line('bottom', (44, 62), (7, 62))
        self.add_arc('bottom-left', (7, 62), (2, 57), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('left', (2, 57), (2, 7))
        self.add_arc('top-left', (2, 7), (7, 2), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('outline', 'top', 'tip-upper', 'tip-lower', 'bottom', 'bottom-left', 'left', 'top-left', closed=True)
