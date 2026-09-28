"""Increased frame height one keyshape step, preserving width and corner radii.
Independent review variant of rounded-rectangular-frame. HRECT_L CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 32]. See container-fit-repair report for measured hosting results."""
SOURCE_PATH = None
SOURCE_ICON_ID = None
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class RoundedRectangularFrame(Container64):
    icon_id = 'rounded-rectangular-frame'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rounded', 'rectangular', 'frame')

    def build(self) -> None:
        self.add_line('top', (6, 10), (58, 10))
        self.add_arc('ne', (58, 10), (62, 14), radius_x=4)
        self.add_line('right', (62, 14), (62, 50))
        self.add_arc('se', (62, 50), (58, 54), radius_x=4)
        self.add_line('bottom', (58, 54), (6, 54))
        self.add_arc('sw', (6, 54), (2, 50), radius_x=4)
        self.add_line('left', (2, 50), (2, 14))
        self.add_arc('nw', (2, 14), (6, 10), radius_x=4)
        self.add_contour('outline', 'top', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
