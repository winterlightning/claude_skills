"""A reader holds an open book with both hands. Lucide book-open informs the central fold and paired pages; shoulders and page text are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe325198-e514-5925-9c27-0c5744e0e768'
SOURCE_PATH = 'pictographic-primitives/school-learning/read human_fe325198-e514-5925-9c27-0c5744e0e768.svg'
AUTHOR = 'gpt-6'

class PersonReadingBook(Solo48):
    icon_id = 'person-reading-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'education/school'
    aliases = ()
    keywords = ('person', 'reading', 'book', 'study', 'reader', 'learning')

    def run(self, name, *points):
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(name + '-' + str(j), a, b)

    def circle(self, name, x, y, r):
        pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y), (x, y - r)]
        ids = []
        for j, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(j)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

    def build(self):
        """Use short gripping fingers and two open page curves with an explicit central spine; the head-to-page ink gap is exactly4."""
        self.circle('head', 24, 11, 5)
        self.add_bezier('page-top-left', (10, 22), ((14, 22), (16, 24), (20, 24)))
        self.add_polyline('page-spine', (20, 24), (24, 24), (28, 24))
        self.add_bezier('page-top-right', (28, 24), ((32, 24), (34, 22), (38, 22)))
        self.add_polyline('book-edge', (38, 22), (38, 30), (38, 38), (24, 42), (10, 38), (10, 30), (10, 22))
        self.add_line('fold', (24, 24), (24, 42))
        for a, b in [('page-top-left', 'page-spine'), ('page-top-right', 'page-spine'), ('page-top-left', 'book-edge'), ('page-top-right', 'book-edge'), ('fold', 'page-spine'), ('fold', 'book-edge')]:
            self.relate('connect', a, b)
        for side, x, end in (('left', 6, 10), ('right', 42, 38)):
            self.add_line('hand-' + side, (x, 30), (end, 30))
            self.relate('connect', 'book-edge', 'hand-' + side)
