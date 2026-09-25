"""Arrows maximize (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e87f104-8fcb-4d6d-a74a-85d7b8aa530f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arrows maximize_7e87f104-8fcb-4d6d-a74a-85d7b8aa530f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowsMaximize(Solo48):
    icon_id = 'arrows-maximize'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrows', 'maximize', '_uncategorized_04')

    def build(self):
        self.add_line('sym-e0', (18, 29), (6, 42))
        self.add_line('sym-e1', (6, 42), (6, 32))
        self.add_line('sym-e2', (15, 42), (6, 42))
        self.add_line('sym-e3', (30, 29), (42, 42))
        self.add_line('sym-e4', (42, 42), (42, 32))
        self.add_line('sym-e5', (33, 42), (42, 42))
        self.add_line('sym-e6', (18, 19), (6, 6))
        self.add_line('sym-e7', (6, 6), (6, 16))
        self.add_line('sym-e8', (15, 6), (6, 6))
        self.add_line('sym-e9', (30, 19), (42, 6))
        self.add_line('sym-e10', (42, 6), (42, 16))
        self.add_line('sym-e11', (33, 6), (42, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c5', 'sym-e8')
        self.add_contour('sym-c6', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c7', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c6', 'sym-c7')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c6', 'sym-c7')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c6', 'sym-c7')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c4', 'sym-c5')
