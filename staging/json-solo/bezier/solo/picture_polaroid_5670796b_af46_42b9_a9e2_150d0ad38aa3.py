"""Picture polaroid (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5670796b-af46-42b9-a9e2-150d0ad38aa3'
SOURCE_PATH = 'icons-json/photography/picture polaroid_5670796b-af46-42b9-a9e2-150d0ad38aa3.json'
AUTHOR = 'json_to_solo'

class PicturePolaroidPhotography(Solo48):
    icon_id = 'picture-polaroid-photography'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('picture', 'polaroid', 'photography')

    def build(self):
        self.add_line('sym-e0', (6, 33), (42, 33))
        self.add_line('sym-e1', (42, 33), (42, 40))
        self.add_bezier('sym-e2', (42, 40), ((41.493, 41.244), (40.481, 42), (39, 42)))
        self.add_bezier('sym-e3', (39, 42), ((38.975, 42), (39.025, 41.992), (39, 42)))
        self.add_line('sym-e4', (39, 42), (24, 42))
        self.add_line('sym-e5', (24, 42), (9, 42))
        self.add_bezier('sym-e6', (9, 42), ((8.975, 41.992), (9.025, 42), (9, 42)))
        self.add_bezier('sym-e7', (9, 42), ((7.519, 42), (6.507, 41.244), (6, 40)))
        self.add_line('sym-e8', (6, 40), (6, 33))
        self.add_line('sym-e9', (6, 33), (6, 8))
        self.add_bezier('sym-e10', (6, 8), ((6.393, 6.961), (6.658, 6), (8, 6)))
        self.add_line('sym-e11', (8, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (40, 6))
        self.add_bezier('sym-e13', (40, 6), ((41.342, 6), (41.607, 6.961), (42, 8)))
        self.add_line('sym-e14', (42, 8), (42, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
