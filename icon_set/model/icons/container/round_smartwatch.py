"""A circular smartwatch face with rounded upper and lower strap connectors.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide watch informs the circular face and paired strap attachments; the source has no hands.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart passes, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-smartwatch VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundSmartwatch(Container64):
    icon_id = 'round-smartwatch'
    keyshape = Keyshape.VRECT_M
    aliases = ('circular-smartwatch',)
    keywords = ('round', 'smartwatch')

    def build(self) -> None:
        self.add_arc('face-upper', (12, 32), (52, 32), radius_x=20)
        self.add_arc('face-lower', (52, 32), (12, 32), radius_x=20)
        self.add_line('upper-a', (20, 17), (20, 8))
        self.add_arc('upper-b', (20, 8), (24, 4), radius_x=4)
        self.add_line('upper-c', (24, 4), (40, 4))
        self.add_arc('upper-d', (40, 4), (44, 8), radius_x=4)
        self.add_line('upper-e', (44, 8), (44, 17))
        self.add_line('lower-a', (44, 47), (44, 56))
        self.add_arc('lower-b', (44, 56), (40, 60), radius_x=4)
        self.add_line('lower-c', (40, 60), (24, 60))
        self.add_arc('lower-d', (24, 60), (20, 56), radius_x=4)
        self.add_line('lower-e', (20, 56), (20, 47))
        self.add_contour('face', 'face-upper', 'face-lower', closed=True)
        self.add_contour('upper', 'upper-a', 'upper-b', 'upper-c', 'upper-d', 'upper-e')
        self.add_contour('lower', 'lower-a', 'lower-b', 'lower-c', 'lower-d', 'lower-e')
        self.relate('connect', 'upper', 'face')
        self.relate('connect', 'lower', 'face')
