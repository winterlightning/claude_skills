"""Increased frame height one keyshape step, preserving width and corner radii.
Independent review variant of rounded-rectangular-frame. HRECT_L CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 32]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rounded-rectangular-frame HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class RoundedRectangularFrame(Container64):
    icon_id = 'rounded-rectangular-frame'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rounded', 'rectangular', 'frame')

    def build(self) -> None:
        self.add_line('top', (8, 12), (56, 12))
        self.add_arc('ne', (56, 12), (60, 16), radius_x=4)
        self.add_line('right', (60, 16), (60, 48))
        self.add_arc('se', (60, 48), (56, 52), radius_x=4)
        self.add_line('bottom', (56, 52), (8, 52))
        self.add_arc('sw', (8, 52), (4, 48), radius_x=4)
        self.add_line('left', (4, 48), (4, 16))
        self.add_arc('nw', (4, 16), (8, 12), radius_x=4)
        self.add_contour('outline', 'top', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
