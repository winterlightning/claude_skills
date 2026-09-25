"""Taller sign panel with a shorter, still distinct centered post.
Independent review variant of rectangular-sign-board. SQUARE CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 24]. See container-fit-repair report for measured hosting results."""
SOURCE_PATH = None
SOURCE_ICON_ID = None
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class RectangularSignBoard(Container64):
    icon_id = 'rectangular-sign-board'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('rectangular', 'sign', 'board')

    def build(self) -> None:
        self.add_line('panel0', (6, 2), (58, 2))
        self.add_arc('panel1', (58, 2), (62, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel2', (62, 6), (62, 42))
        self.add_arc('panel3', (62, 42), (58, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel4', (58, 46), (6, 46))
        self.add_arc('panel5', (6, 46), (2, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('panel6', (2, 42), (2, 6))
        self.add_arc('panel7', (2, 6), (6, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('panel', 'panel0', 'panel1', 'panel2', 'panel3', 'panel4', 'panel5', 'panel6', 'panel7', closed=True)
        self.add_line('post', (32, 46), (32, 62))
        self.relate('connect', 'panel', 'post')
