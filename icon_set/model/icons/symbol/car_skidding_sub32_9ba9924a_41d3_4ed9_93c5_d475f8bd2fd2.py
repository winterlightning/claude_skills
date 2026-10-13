"""Independent 32px profile of car-skidding.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2'
SOURCE_PATH = 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2', 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-skidding',)
SOLO_SOURCE_ICON_IDS = ('car-skidding',)
REFERENCE_EXPORT_SHA256 = '9c7d067718aebcceaa356212e3ce9f66c57820044d15f484cfef56e28b575b4d'

class Drawing(Sub32):
    icon_id = 'car-skidding-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Car (front view, one outline) above two curving skid marks.
        self.add_line('p1-r1-1', (10, 2), (22, 2))
        self.add_line('p1-r1-2', (22, 2), (26, 8))
        self.add_line('p1-r1-3', (26, 8), (28, 8))
        self.add_line('p1-r1-4', (28, 8), (28, 16))
        self.add_line('p1-r1-5', (28, 16), (4, 16))
        self.add_line('p1-r1-6', (4, 16), (4, 8))
        self.add_line('p1-r1-7', (4, 8), (6, 8))
        self.add_line('p1-r1-8', (6, 8), (10, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_bezier('p2-r1-1', (8, 24), ((4, 26), (12, 28), (8, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (24, 24), ((20, 26), (28, 28), (24, 30)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
