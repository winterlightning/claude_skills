'Two large question marks stand beside one another with opposite orientations. The left mark is inverted with its dot above, while the right mark is upright with its dot below.\n\nConstruction: One upright question mark and a matching inverted mark; reduced to open hooks and dots. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e4b556a-dbe7-4afa-b062-f1b15b9e1b4d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/information desk question help_7e4b556a-dbe7-4afa-b062-f1b15b9e1b4d.svg'
AUTHOR = 'gpt-6'

class PairedQuestionMarks(Solo48):
    icon_id = 'paired-question-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('question', 'help', 'information', 'punctuation', 'query', 'marks')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('right-hook', (26, 14), (42, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('right-turn', (42, 14), (34, 24), radius_x=8, radius_y=10, large_arc=False, sweep=True)
        self.add_line('right-stem', (34, 24), (34, 30))
        self.add_line('right-dot', (34, 42), (34, 42))
        self.add_arc('left-hook', (22, 34), (6, 34), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('left-turn', (6, 34), (14, 24), radius_x=8, radius_y=10, large_arc=False, sweep=True)
        self.add_line('left-stem', (14, 24), (14, 18))
        self.add_line('left-dot', (14, 6), (14, 6))
        self.add_contour('right', 'right-hook', 'right-turn', 'right-stem', closed=False)
        self.add_contour('left', 'left-hook', 'left-turn', 'left-stem', closed=False)
