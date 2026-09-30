"""Taller sign panel with a shorter, still distinct centered post.
Independent review variant of rectangular-sign-board. SQUARE CONTAINER64, 4-unit strokes.
Construction follows the inspected Lucide frame/phone/calendar/watch originals and atomic-debug views.
Native SUB32 trial center: [32, 24]. See container-fit-repair report for measured hosting results.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rectangular-sign-board SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class RectangularSignBoard(Container64):
    icon_id = 'rectangular-sign-board'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rectangular', 'sign', 'board')

    def build(self) -> None:
        self.add_line('panel0', (10, 6), (54, 6))
        self.add_arc('panel1', (54, 6), (58, 10), radius_x=4)
        self.add_line('panel2', (58, 10), (58, 40))
        self.add_arc('panel3', (58, 40), (54, 44), radius_x=4)
        self.add_line('panel4', (54, 44), (10, 44))
        self.add_arc('panel5', (10, 44), (6, 40), radius_x=4)
        self.add_line('panel6', (6, 40), (6, 10))
        self.add_arc('panel7', (6, 10), (10, 6), radius_x=4)
        self.add_line('post', (32, 44), (32, 58))
        self.add_contour('panel', 'panel0', 'panel1', 'panel2', 'panel3', 'panel4', 'panel5', 'panel6', 'panel7', closed=True)
        self.relate('connect', 'panel', 'post')
