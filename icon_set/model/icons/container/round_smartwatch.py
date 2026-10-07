"""A circular smartwatch face with rounded upper and lower strap connectors.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide watch informs the circular face and paired strap attachments; the source has no hands.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart passes, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-smartwatch VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundSmartwatch(Container64):
    icon_id = 'round-smartwatch'
    keyshape = Keyshape.VRECT_L
    aliases = ('circular-smartwatch',)
    keywords = ('round', 'smartwatch')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): rounded-square face 10..54 x 12..52 with radius-10 corners (a round face of the
        # widest radius this frame allows held only 22.5); straps 20..44. Mirrored on both axes. Holds a symbol
        # of 24+ with a 4 px gap (was 19).
        self.add_bezier('face-nw', (10, 22), ((10, 16.5), (14.5, 12), (20, 12)))
        self.add_line('face-top', (20, 12), (44, 12))
        self.add_bezier('face-ne', (44, 12), ((49.5, 12), (54, 16.5), (54, 22)))
        self.add_line('face-right', (54, 22), (54, 42))
        self.add_bezier('face-se', (54, 42), ((54, 47.5), (49.5, 52), (44, 52)))
        self.add_line('face-bottom', (44, 52), (20, 52))
        self.add_bezier('face-sw', (20, 52), ((14.5, 52), (10, 47.5), (10, 42)))
        self.add_line('face-left', (10, 42), (10, 22))
        self.add_line('upper-a', (20, 12), (20, 8))
        self.add_arc('upper-b', (20, 8), (24, 4), radius_x=4)
        self.add_line('upper-c', (24, 4), (40, 4))
        self.add_arc('upper-d', (40, 4), (44, 8), radius_x=4)
        self.add_line('upper-e', (44, 8), (44, 12))
        self.add_line('lower-a', (44, 52), (44, 56))
        self.add_arc('lower-b', (44, 56), (40, 60), radius_x=4)
        self.add_line('lower-c', (40, 60), (24, 60))
        self.add_arc('lower-d', (24, 60), (20, 56), radius_x=4)
        self.add_line('lower-e', (20, 56), (20, 52))
        self.add_contour('face', 'face-nw', 'face-top', 'face-ne', 'face-right', 'face-se', 'face-bottom', 'face-sw', 'face-left', closed=True)
        self.add_contour('upper', 'upper-a', 'upper-b', 'upper-c', 'upper-d', 'upper-e')
        self.add_contour('lower', 'lower-a', 'lower-b', 'lower-c', 'lower-d', 'lower-e')
        self.relate('connect', 'face', 'upper')
        self.relate('connect', 'face', 'lower')
