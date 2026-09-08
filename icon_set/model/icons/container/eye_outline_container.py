"""An empty almond-shaped eye enclosure.

HRECT_L: exact centerline extremes recorded in build.
Construction: Lucide eye, mirrored upper and lower arcs; pupil omitted because the source is an empty enclosure. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class EyeOutlineContainer(Container64):
    icon_id = 'eye-outline-container'
    keyshape = Keyshape.HRECT_L
    aliases = ('minimalist-human-eye-shape',)
    keywords = ('eye', 'outline', 'container')

    def build(self) -> None:
        # Centerline (2,10)-(62,54). Ellipse centers (32,120)/(32,-56).
        self.add_arc('upper-left',(2,32),(32,10),radius_x=50,radius_y=110)
        self.add_arc('upper-right',(32,10),(62,32),radius_x=50,radius_y=110)
        self.add_arc('lower-right',(62,32),(32,54),radius_x=50,radius_y=110)
        self.add_arc('lower-left',(32,54),(2,32),radius_x=50,radius_y=110)
        self.add_contour('outline','upper-left','upper-right','lower-right','lower-left',closed=True)
