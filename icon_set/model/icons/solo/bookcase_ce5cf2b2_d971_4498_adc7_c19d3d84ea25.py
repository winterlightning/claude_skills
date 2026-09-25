"""Two shelves hold upright and leaning books. Lucide library-big informs the spine rhythm and leaning volume. Book counts and spine decoration are reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce5cf2b2-d971-4498-adc7-c19d3d84ea25'
SOURCE_PATH = 'pictographic-primitives/school-learning/library_ce5cf2b2-d971-4498-adc7-c19d3d84ea25.svg'
AUTHOR = 'gpt-6'


class Bookcase(Solo48):
    icon_id = 'bookcase'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('bookcase', 'books', 'library', 'shelf', 'reading', 'storage')

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

        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.run('right',(42,10),(42,24),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.run('bottom',(38,42),(32,42),(22,42),(14,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.run('left',(6,38),(6,24),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('case','top','tr','right-1','right-2','br','bottom-1','bottom-2','bottom-3','bottom-4','bl','left-1','left-2','tl',closed=True)
        self.add_polyline('shelf',(6,24),(14,24),(22,24),(36,24),(42,24))
        self.relate('connect','case','shelf')
        self.add_polyline('upper-book',(14,24),(14,15),(22,15),(22,24))
        self.add_line('leaning-book',(32,15),(36,24))
        self.relate('connect','upper-book','shelf')
        self.relate('connect','leaning-book','shelf')
        self.add_polyline('lower-book',(14,42),(14,33),(22,33),(22,42))
        self.add_line('lower-spine',(32,34),(32,42))
        self.relate('connect','case','lower-book')
        self.relate('connect','case','lower-spine')
