"""An empty almond-shaped eye enclosure.

HRECT_L: exact centerline extremes recorded in build.
Construction: Lucide eye, mirrored upper and lower arcs; pupil omitted because the source is an empty enclosure. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (eye-outline-container HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class EyeOutlineContainer(Container64):
    icon_id = 'eye-outline-container'
    keyshape = Keyshape.HRECT_M
    aliases = ('minimalist-human-eye-shape',)
    keywords = ('eye', 'outline', 'container')

    def build(self) -> None:
        self.add_arc('upper-left', (4, 32), (32, 12), radius_x=47, radius_y=101)
        self.add_arc('upper-right', (32, 12), (60, 32), radius_x=47, radius_y=101)
        self.add_arc('lower-right', (60, 32), (32, 52), radius_x=47, radius_y=101)
        self.add_arc('lower-left', (32, 52), (4, 32), radius_x=47, radius_y=101)
        self.add_contour('outline', 'upper-left', 'upper-right', 'lower-right', 'lower-left', closed=True)
