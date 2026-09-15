"""An apple rests on a closed book. Lucide apple informs paired lobes and the curved stem; leaf and page mark are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8495c6bc-cdec-5e1b-9374-05a5efbc3c03'
SOURCE_PATH = 'pictographic-primitives/school-learning/school book apple_8495c6bc-cdec-5e1b-9374-05a5efbc3c03.svg'
AUTHOR = 'gpt-6'


class AppleOnBook(Solo48):
    icon_id = 'apple-on-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('apple', 'book', 'school', 'education', 'reading', 'fruit')

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

        self.add_arc('apple-ul',(24,14),(14,18),radius_x=6,sweep=False)
        self.add_arc('apple-ll',(14,18),(24,32),radius_x=10,radius_y=14,sweep=False)
        self.add_arc('apple-lr',(24,32),(34,18),radius_x=10,radius_y=14,sweep=False)
        self.add_arc('apple-ur',(34,18),(24,14),radius_x=6,sweep=False)
        self.add_contour('apple','apple-ul','apple-ll','apple-lr','apple-ur',closed=True)
        self.add_line('stem',(24,14),(24,10))
        self.add_arc('stem-tip',(24,10),(20,6),radius_x=4,sweep=False)
        self.add_contour('stalk','stem','stem-tip')
        self.relate('connect','apple','stalk')
        self.run('book-top',(6,32),(24,32),(37,32))
        self.add_arc('book-round-top',(37,32),(42,37),radius_x=5)
        self.add_arc('book-round-bottom',(42,37),(37,42),radius_x=5)
        self.add_line('book-bottom',(37,42),(6,42))
        self.add_contour('book','book-top-1','book-top-2','book-round-top','book-round-bottom','book-bottom')
        self.relate('connect','apple','book')
