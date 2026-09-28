'A hand raises two long fingers in a V shape. The thumb folds across the other curled fingers above a rounded palm, with a short angled crease visible inside.\n\nConstruction: Two raised fingers form a V above a compact fist. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b5ca2c2-1fba-56f6-86df-d84f51424abf'
SOURCE_PATH = 'pictographic-primitives/wayfinding/two fingers_1b5ca2c2-1fba-56f6-86df-d84f51424abf.svg'
AUTHOR = 'gpt-6'

class VictoryHandSign(Solo48):
    icon_id = 'victory-hand-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('victory', 'peace', 'hand', 'fingers', 'gesture', 'sign')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('hand-1', (16, 30), (6, 8))
        self.add_line('hand-2', (6, 8), (16, 6))
        self.add_line('hand-3', (16, 6), (24, 24))
        self.add_line('hand-4', (24, 24), (32, 6))
        self.add_line('hand-5', (32, 6), (42, 8))
        self.add_line('hand-6', (42, 8), (32, 30))
        self.add_line('hand-7', (32, 30), (36, 36))
        self.add_line('hand-8', (36, 36), (30, 42))
        self.add_line('hand-9', (30, 42), (16, 42))
        self.add_line('hand-10', (16, 42), (8, 34))
        self.add_line('hand-11', (8, 34), (8, 28))
        self.add_line('hand-12', (8, 28), (16, 30))
        self.add_line('hand-13', (16, 30), (16, 30))
        self.add_line('thumb-fold', (16, 30), (28, 34))
        self.add_contour('hand', 'hand-1', 'hand-2', 'hand-3', 'hand-4', 'hand-5', 'hand-6', 'hand-7', 'hand-8', 'hand-9', 'hand-10', 'hand-11', 'hand-12', 'hand-13', closed=True)
        self.relate('connect', 'thumb-fold', 'hand')
