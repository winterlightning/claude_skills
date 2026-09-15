"""Square brackets (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'acfbd10d-de12-4626-bd35-5e7b02ef616f'
SOURCE_PATH = 'pictographic-primitives/symbol/square brackets_acfbd10d-de12-4626-bd35-5e7b02ef616f.svg'
AUTHOR = 'gpt-6'

class SquareBrackets(Solo48):
    icon_id = 'square-brackets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('square', 'brackets', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 24), (42, 40))
        self.add_line('sym-e2', (42, 40), (41, 42))
        self.add_line('sym-e3', (41, 42), (36, 42))
        self.add_line('sym-e5', (6, 24), (6, 40))
        self.add_line('sym-e6', (6, 40), (8, 42))
        self.add_line('sym-e7', (8, 42), (11, 42))
        self.add_line('sym-e8', (42, 24), (42, 8))
        self.add_line('sym-e10', (42, 8), (41, 6))
        self.add_line('sym-e11', (41, 6), (36, 6))
        self.add_line('sym-e13', (6, 24), (6, 8))
        self.add_line('sym-e14', (6, 8), (8, 6))
        self.add_line('sym-e15', (8, 6), (11, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', closed=False)
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', closed=False)
        self.add_contour('sym-c2', 'sym-e8', 'sym-e10', 'sym-e11', closed=False)
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
