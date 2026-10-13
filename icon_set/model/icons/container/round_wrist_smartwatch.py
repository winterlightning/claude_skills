"""A round display enclosure framed by short rounded wristband attachments.
The blank reference face stays blank; no clock hands are introduced.

Keyshape VRECT_L; centerline extremes recorded in build below.
Lucide watch informs the circular face and mirrored straps. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus does not clear, heart passes, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-wrist-smartwatch VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundWristSmartwatch(Container64):
    icon_id = 'round-wrist-smartwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('round', 'wrist', 'smartwatch')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): the face is a rounded square 10..54 x 12..52 with radius-10 corners (a 22-radius
        # circle, the most this frame allows, held only 22.5); straps 20..44 rise from its flat top and bottom.
        # Mirrored on both axes. Holds a symbol of 24+ with a 4 px gap (was 18.5).
        self.add_bezier('face-nw', (10, 22), ((10, 16.5), (14.5, 12), (20, 12)))
        self.add_line('face-top', (20, 12), (44, 12))
        self.add_bezier('face-ne', (44, 12), ((49.5, 12), (54, 16.5), (54, 22)))
        self.add_line('face-right', (54, 22), (54, 42))
        self.add_bezier('face-se', (54, 42), ((54, 47.5), (49.5, 52), (44, 52)))
        self.add_line('face-bottom', (44, 52), (20, 52))
        self.add_bezier('face-sw', (20, 52), ((14.5, 52), (10, 47.5), (10, 42)))
        self.add_line('face-left', (10, 42), (10, 22))
        self.add_line('upper-left', (20, 12), (20, 9))
        self.add_arc('upper-nw', (20, 9), (25, 4), radius_x=5)
        self.add_line('upper-top', (25, 4), (39, 4))
        self.add_arc('upper-ne', (39, 4), (44, 9), radius_x=5)
        self.add_line('upper-right', (44, 9), (44, 12))
        self.add_line('lower-left', (20, 52), (20, 55))
        self.add_arc('lower-nw', (20, 55), (25, 60), radius_x=5, sweep=False)
        self.add_line('lower-top', (25, 60), (39, 60))
        self.add_arc('lower-ne', (39, 60), (44, 55), radius_x=5, sweep=False)
        self.add_line('lower-right', (44, 55), (44, 52))
        self.add_contour('face', 'face-nw', 'face-top', 'face-ne', 'face-right', 'face-se', 'face-bottom', 'face-sw', 'face-left', closed=True)
        self.add_contour('upper', 'upper-left', 'upper-nw', 'upper-top', 'upper-ne', 'upper-right')
        self.add_contour('lower', 'lower-left', 'lower-nw', 'lower-top', 'lower-ne', 'lower-right')
        self.relate('connect', 'face', 'upper')
        self.relate('connect', 'face', 'lower')
