"""Screentone effect action line (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff318c8e-d8a1-4786-accd-7130ff0b0c3e'
SOURCE_PATH = 'pictographic-primitives/video-games/screentone effect action line_ff318c8e-d8a1-4786-accd-7130ff0b0c3e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ScreentoneEffectActionLine(Solo48):
    icon_id = 'screentone-effect-action-line'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('screentone', 'effect', 'action', 'line', 'video-games')

    def build(self):
        self.add_line('e0', (24, 6), (24, 13))
        self.add_line('e1', (31, 17), (41, 7))
        self.add_line('e2', (7, 7), (17, 17))
        self.add_line('e3', (6, 24), (13, 24))
        self.add_line('e4', (35, 24), (42, 24))
        self.add_line('e5', (31, 31), (41, 41))
        self.add_line('e6', (7, 42), (17, 31))
        self.add_line('e7', (24, 35), (24, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
