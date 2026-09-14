"""A reader holds an open book with both hands. Lucide book-open informs the central fold and paired pages; shoulders and page text are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe325198-e514-5925-9c27-0c5744e0e768'
SOURCE_PATH = 'pictographic-primitives/school-learning/read human_fe325198-e514-5925-9c27-0c5744e0e768.svg'
AUTHOR = 'gpt-6'


class PersonReadingBook(Solo48):
    icon_id = 'person-reading-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('person', 'reading', 'book', 'study', 'reader', 'learning')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+"-"+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Current centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40; VRECT 8,4-40,44.

        self.circle('head',24,11,5)
        self.add_polyline('book',(10,26),(24,30),(38,26),(38,32),(38,38),(24,42),(10,38),(10,32),closed=True)
        self.add_line('fold',(24,30),(24,42))
        self.relate('connect','book','fold')
        for side,x in (('left',8),('right',40)):
            self.circle('hand-'+side,x,32,2)
            self.relate('connect','book','hand-'+side)
