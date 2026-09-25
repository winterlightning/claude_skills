"""A two-handled trophy stands on a closed book. Lucide trophy informs the cup and paired handles; the stem is a single stroke and the book supplies the foot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acc1b2d8-095b-4533-9be6-ab94159c1b18'
SOURCE_PATH = 'pictographic-primitives/school-learning/school book trophy_acc1b2d8-095b-4533-9be6-ab94159c1b18.svg'
AUTHOR = 'gpt-6'


class TrophyOnBook(Solo48):
    icon_id = 'trophy-on-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('trophy', 'book', 'school', 'award', 'achievement', 'cup')

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

        self.run('cup-top',(16,18),(16,6),(32,6),(32,18))
        self.add_arc('cup-right',(32,18),(24,25),radius_x=8,radius_y=7)
        self.add_arc('cup-left',(24,25),(16,18),radius_x=8,radius_y=7)
        self.add_contour('cup','cup-top-1','cup-top-2','cup-top-3','cup-right','cup-left',closed=True)
        self.add_arc('handle-left',(16,6),(16,18),radius_x=10,radius_y=6,sweep=False)
        self.add_arc('handle-right',(32,18),(32,6),radius_x=10,radius_y=6,sweep=False)
        self.relate('connect','cup','handle-left')
        self.relate('connect','cup','handle-right')
        self.add_line('stem',(24,25),(24,34))
        self.relate('connect','cup','stem')
        self.run('book-top',(6,34),(24,34),(38,34))
        self.add_arc('book-tr',(38,34),(42,38),radius_x=4)
        self.add_arc('book-br',(42,38),(38,42),radius_x=4)
        self.add_line('book-bottom',(38,42),(6,42))
        self.add_contour('book','book-top-1','book-top-2','book-tr','book-br','book-bottom')
        self.relate('connect','book','stem')
