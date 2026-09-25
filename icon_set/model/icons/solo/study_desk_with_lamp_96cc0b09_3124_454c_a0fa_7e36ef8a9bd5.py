"""A study desk supports a book and bent-stem lamp. Lucide lamp-desk informs the lamp construction. The stack becomes one book and the shade faces downward to preserve clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96cc0b09-3124-454c-a0fa-7e36ef8a9bd5'
SOURCE_PATH = 'pictographic-primitives/school-learning/study desk_96cc0b09-3124-454c-a0fa-7e36ef8a9bd5.svg'
AUTHOR = 'gpt-6'


class StudyDeskWithLamp(Solo48):
    icon_id = 'study-desk-with-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('desk', 'lamp', 'books', 'study', 'school', 'furniture')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+'-'+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Live centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40.

        self.add_polyline('desktop',(6,30),(10,30),(20,30),(36,30),(38,30),(42,30))
        for side,x,end in (('left',10,8),('right',38,40)):
            self.add_line('leg-'+side,(x,30),(end,42))
            self.relate('connect','desktop','leg-'+side)
        self.add_polyline('book',(6,30),(6,22),(20,22),(20,30))
        self.relate('connect','book','desktop')
        self.add_arc('shade-left',(24,13),(32,6),radius_x=8,radius_y=7)
        self.add_arc('shade-right',(32,6),(40,13),radius_x=8,radius_y=7)
        self.add_line('shade-mouth',(40,13),(24,13))
        self.add_contour('shade','shade-left','shade-right','shade-mouth',closed=True)
        self.add_line('neck',(40,13),(40,20))
        self.add_arc('elbow',(40,20),(36,24),radius_x=4)
        self.add_line('stem',(36,24),(36,30))
        self.add_contour('lamp-arm','neck','elbow','stem')
        self.relate('connect','shade','lamp-arm')
        self.relate('connect','desktop','lamp-arm')
