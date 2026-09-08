"""A circular smartwatch face with rounded upper and lower strap connectors.

Keyshape VRECT_L: (8, 0, 56, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide watch informs the circular face and paired strap attachments; the source has no hands.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus passes, heart passes, check does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class RoundSmartwatch(Container64):
    icon_id = 'round-smartwatch'
    keyshape = Keyshape.VRECT_L
    aliases = ('circular-smartwatch',)
    keywords = ('round', 'smartwatch')

    def build(self) -> None:
        self.add_arc('face-upper', (10, 32), (54, 32), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('face-lower', (54, 32), (10, 32), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('face', 'face-upper', 'face-lower', closed=True)
        self.add_line('upper-a', (18, 15), (18, 6))
        self.add_arc('upper-b', (18, 6), (22, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('upper-c', (22, 2), (42, 2))
        self.add_arc('upper-d', (42, 2), (46, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('upper-e', (46, 6), (46, 15))
        self.add_contour('upper', 'upper-a', 'upper-b', 'upper-c', 'upper-d', 'upper-e', closed=False)
        self.relate("connect", 'upper', 'face')
        self.add_line('lower-a', (46, 49), (46, 58))
        self.add_arc('lower-b', (46, 58), (42, 62), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lower-c', (42, 62), (22, 62))
        self.add_arc('lower-d', (22, 62), (18, 58), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lower-e', (18, 58), (18, 49))
        self.add_contour('lower', 'lower-a', 'lower-b', 'lower-c', 'lower-d', 'lower-e', closed=False)
        self.relate("connect", 'lower', 'face')
