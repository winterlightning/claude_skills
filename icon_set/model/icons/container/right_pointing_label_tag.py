"""A right-pointing label outline with rounded left corners.

Keyshape HRECT_M: (0, 12, 64, 52); preserves the reference proportions.
Reference: batch_11 source render; Lucide tag informs the continuous outline and deliberate pointed end.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart does not clear, check does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RightPointingLabelTag(Container64):
    icon_id = 'right-pointing-label-tag'
    keyshape = Keyshape.HRECT_M
    aliases = ('wide-label-tag',)
    keywords = ('right', 'pointing', 'label', 'tag')

    def build(self) -> None:
        self.add_line('top', (7, 14), (44, 14))
        self.add_line('tip-upper', (44, 14), (62, 32))
        self.add_line('tip-lower', (62, 32), (44, 50))
        self.add_line('bottom', (44, 50), (7, 50))
        self.add_arc('bottom-left', (7, 50), (2, 45), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('left', (2, 45), (2, 19))
        self.add_arc('top-left', (2, 19), (7, 14), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('outline', 'top', 'tip-upper', 'tip-lower', 'bottom', 'bottom-left', 'left', 'top-left', closed=True)
