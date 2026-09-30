"""A round display enclosure framed by short rounded wristband attachments.
The blank reference face stays blank; no clock hands are introduced.

Keyshape VRECT_L; centerline extremes recorded in build below.
Lucide watch informs the circular face and mirrored straps. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus does not clear, heart passes, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (round-wrist-smartwatch VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundWristSmartwatch(Container64):
    icon_id = 'round-wrist-smartwatch'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('round', 'wrist', 'smartwatch')

    def build(self) -> None:
        self.add_arc('face-nw', (12, 32), (19, 18), radius_x=18)
        self.add_arc('face-nw-top', (19, 18), (30, 14), radius_x=17)
        self.add_line('face-top', (30, 14), (34, 14))
        self.add_arc('face-ne-top', (34, 14), (45, 18), radius_x=17)
        self.add_arc('face-ne', (45, 18), (52, 32), radius_x=18)
        self.add_arc('face-se', (52, 32), (45, 46), radius_x=18)
        self.add_arc('face-se-bottom', (45, 46), (34, 50), radius_x=17)
        self.add_line('face-bottom', (34, 50), (30, 50))
        self.add_arc('face-sw-bottom', (30, 50), (19, 46), radius_x=17)
        self.add_arc('face-sw', (19, 46), (12, 32), radius_x=18)
        self.add_line('upper-left', (19, 18), (19, 9))
        self.add_arc('upper-nw', (19, 9), (24, 4), radius_x=5)
        self.add_line('upper-top', (24, 4), (40, 4))
        self.add_arc('upper-ne', (40, 4), (45, 9), radius_x=5)
        self.add_line('upper-right', (45, 9), (45, 18))
        self.add_line('lower-left', (19, 46), (19, 55))
        self.add_arc('lower-nw', (19, 55), (24, 60), radius_x=5, sweep=False)
        self.add_line('lower-top', (24, 60), (40, 60))
        self.add_arc('lower-ne', (40, 60), (45, 55), radius_x=5, sweep=False)
        self.add_line('lower-right', (45, 55), (45, 46))
        self.add_contour('face', 'face-nw', 'face-nw-top', 'face-top', 'face-ne-top', 'face-ne', 'face-se', 'face-se-bottom', 'face-bottom', 'face-sw-bottom', 'face-sw', closed=True)
        self.add_contour('upper', 'upper-left', 'upper-nw', 'upper-top', 'upper-ne', 'upper-right')
        self.add_contour('lower', 'lower-left', 'lower-nw', 'lower-top', 'lower-ne', 'lower-right')
        self.relate('connect', 'face', 'upper')
        self.relate('connect', 'face', 'lower')
