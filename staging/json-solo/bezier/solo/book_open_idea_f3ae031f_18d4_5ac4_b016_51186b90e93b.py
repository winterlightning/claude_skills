"""Book open idea (content), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3ae031f-18d4-5ac4-b016-51186b90e93b'
SOURCE_PATH = 'icons-json/content/book open idea_f3ae031f-18d4-5ac4-b016-51186b90e93b.json'
AUTHOR = 'json_to_solo'

class BookOpenIdeaContent(Solo48):
    icon_id = 'book-open-idea-content'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'idea', 'content')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 10))
        self.add_line('sym-e1', (24, 42), (24, 22))
        self.add_line('sym-e2', (24, 22), (24, 22))
        self.add_bezier('sym-e3', (24, 22), ((23.345, 21.1), (22.835, 19.761), (22, 19)))
        self.add_bezier('sym-e4', (22, 19), ((19.161, 16.423), (14.682, 15.196), (11, 15)))
        self.add_bezier('sym-e5', (11, 15), ((10.116, 14.951), (9.884, 14.984), (9, 15)))
        self.add_bezier('sym-e6', (9, 15), ((7.732, 15.016), (6, 15.274), (6, 17)))
        self.add_bezier('sym-e7', (6, 17), ((6, 17.074), (6, 16.926), (6, 17)))
        self.add_bezier('sym-e8', (6, 17), ((6, 17.082), (6, 16.918), (6, 17)))
        self.add_line('sym-e9', (6, 17), (6, 35))
        self.add_bezier('sym-e10', (6, 35), ((6, 35.172), (6, 35.828), (6, 36)))
        self.add_bezier('sym-e11', (6, 36), ((6, 37.996), (8.625, 37.935), (10, 38)))
        self.add_bezier('sym-e12', (10, 38), ((13.453, 38.172), (16.809, 37.527), (20, 39)))
        self.add_bezier('sym-e13', (20, 39), ((21.448, 39.671), (22.699, 41.092), (24, 42)))
        self.add_bezier('sym-e14', (24, 42), ((25.301, 41.092), (26.552, 39.671), (28, 39)))
        self.add_bezier('sym-e15', (28, 39), ((31.191, 37.527), (34.547, 38.172), (38, 38)))
        self.add_bezier('sym-e16', (38, 38), ((39.375, 37.935), (42, 37.996), (42, 36)))
        self.add_bezier('sym-e17', (42, 36), ((42, 35.828), (42, 35.172), (42, 35)))
        self.add_line('sym-e18', (42, 35), (42, 17))
        self.add_bezier('sym-e19', (42, 17), ((42, 16.918), (42, 17.082), (42, 17)))
        self.add_bezier('sym-e20', (42, 17), ((42, 16.926), (42, 17.074), (42, 17)))
        self.add_bezier('sym-e21', (42, 17), ((42, 15.274), (40.268, 15.016), (39, 15)))
        self.add_bezier('sym-e22', (39, 15), ((38.116, 14.984), (37.884, 14.951), (37, 15)))
        self.add_bezier('sym-e23', (37, 15), ((33.318, 15.196), (28.839, 16.423), (26, 19)))
        self.add_bezier('sym-e24', (26, 19), ((25.165, 19.761), (24.655, 21.1), (24, 22)))
        self.add_line('sym-e25', (15, 7), (17, 9))
        self.add_line('sym-e26', (33, 7), (31, 9))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c2', 'sym-e25')
        self.add_contour('sym-c3', 'sym-e26')
