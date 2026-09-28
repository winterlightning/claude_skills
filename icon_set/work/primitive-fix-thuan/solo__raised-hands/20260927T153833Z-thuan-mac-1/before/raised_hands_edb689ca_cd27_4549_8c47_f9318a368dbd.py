'Two hands rise on opposite sides with palms facing inward and thumbs separated from the fingers. Five short radiating strokes form an arc above the open space between them.\n\nConstruction: Two mirrored raised hands with inward thumbs and three detached emphasis rays. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edb689ca-cd27-4549-8c47-f9318a368dbd'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand raise_edb689ca-cd27-4549-8c47-f9318a368dbd.svg'
AUTHOR = 'gpt-6'

class RaisedHands(Solo48):
    icon_id = 'raised-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hands', 'raised', 'palms', 'gesture', 'celebration', 'praise')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('left-1', (6, 42), (6, 32))
        self.add_line('left-2', (6, 32), (10, 24))
        self.add_line('left-3', (10, 24), (14, 24))
        self.add_line('left-4', (14, 24), (18, 34))
        self.add_line('left-5', (18, 34), (20, 28))
        self.add_line('left-6', (20, 28), (20, 38))
        self.add_line('left-7', (20, 38), (16, 42))
        self.add_line('right-1', (42, 42), (42, 32))
        self.add_line('right-2', (42, 32), (38, 24))
        self.add_line('right-3', (38, 24), (34, 24))
        self.add_line('right-4', (34, 24), (30, 34))
        self.add_line('right-5', (30, 34), (28, 28))
        self.add_line('right-6', (28, 28), (28, 38))
        self.add_line('right-7', (28, 38), (32, 42))
        self.add_line('ray-center', (24, 6), (24, 12))
        self.add_line('ray-left', (6, 12), (10, 16))
        self.add_line('ray-right', (42, 12), (38, 16))
        self.add_contour('left', 'left-1', 'left-2', 'left-3', 'left-4', 'left-5', 'left-6', 'left-7', closed=False)
        self.add_contour('right', 'right-1', 'right-2', 'right-3', 'right-4', 'right-5', 'right-6', 'right-7', closed=False)
