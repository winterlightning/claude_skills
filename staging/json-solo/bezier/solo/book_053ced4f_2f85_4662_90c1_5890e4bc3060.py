"""Book (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '053ced4f-2f85-4662-90c1-5890e4bc3060'
SOURCE_PATH = 'icons-json/content/book_053ced4f-2f85-4662-90c1-5890e4bc3060.json'
AUTHOR = 'json_to_solo'

class Book053ced4f(Solo48):
    icon_id = 'book-053ced4f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'content')

    def build(self):
        self.add_line('e0', (40, 15), (40, 43))
        self.add_line('e1', (39, 44), (13, 44))
        self.add_line('e2', (8, 41), (8, 11))
        self.add_line('e3', (40, 15), (14, 15))
        self.add_line('e4', (40, 15), (40, 5))
        self.add_line('e5', (39, 4), (11, 4))
        self.add_line('e6', (8, 9), (8, 11))
        self.add_bezier('e7', (40, 43), ((40, 43.055), (39.992, 43.2), (39.992, 43.255)), ((39.992, 43.591), (39.621, 43.982), (39.309, 43.982)), ((39.259, 43.991), (39.051, 43.991), (39, 44)))
        self.add_bezier('e8', (13, 44), ((12.629, 44), (12.312, 43.991), (11.941, 43.991)), ((10.392, 43.991), (8.008, 43.927), (8.008, 41.573)), ((8.008, 41.473), (8, 41.1), (8, 41)))
        self.add_bezier('e9', (14, 15), ((12.366, 15), (8.017, 14.109), (8.017, 11.6)), ((8.008, 11.491), (8.008, 11.109), (8, 11)))
        self.add_bezier('e10', (40, 5), ((40, 4.945), (39.992, 4.8), (39.992, 4.745)), ((39.992, 4.418), (39.621, 4), (39.309, 4)), ((39.259, 4), (39.051, 4), (39, 4)))
        self.add_bezier('e11', (11, 4), ((9.097, 4), (8.008, 6.182), (8.008, 8.127)), ((8.008, 8.264), (8, 8.864), (8, 9)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3', 'e9')
        self.add_contour('c2', 'e4', 'e10', 'e5', 'e11', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
