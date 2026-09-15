"""Picture polaroid (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5670796b-af46-42b9-a9e2-150d0ad38aa3'
SOURCE_PATH = 'pictographic-primitives/photography/picture polaroid_5670796b-af46-42b9-a9e2-150d0ad38aa3.svg'
AUTHOR = 'gpt-6'

class PicturePolaroid(Solo48):
    icon_id = 'picture-polaroid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('picture', 'polaroid', 'photography')

    def build(self):
        self.add_line('sym-e0', (6, 33), (42, 33))
        self.add_line('sym-e1', (42, 33), (42, 40))
        self.add_line('sym-e2', (42, 40), (39, 42))
        self.add_line('sym-e4', (39, 42), (9, 42))
        self.add_line('sym-e7', (9, 42), (6, 40))
        self.add_line('sym-e8', (6, 40), (6, 8))
        self.add_line('sym-e10', (6, 8), (8, 6))
        self.add_line('sym-e11', (8, 6), (40, 6))
        self.add_line('sym-e13', (40, 6), (42, 8))
        self.add_line('sym-e14', (42, 8), (42, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', closed=False)
