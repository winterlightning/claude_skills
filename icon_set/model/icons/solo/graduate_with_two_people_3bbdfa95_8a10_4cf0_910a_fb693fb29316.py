"""A central graduate is flanked by two smaller people. Lucide graduation-cap and user-round inform the cap and portraits. Collar, hair band and tassel are omitted; mirrored shoulder curves connect the group."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bbdfa95-8a10-4cf0-910a-fb693fb29316'
SOURCE_PATH = 'pictographic-primitives/school-learning/study virtual classroom_3bbdfa95-8a10-4cf0-910a-fb693fb29316.svg'
AUTHOR = 'gpt-6'


class GraduateWithTwoPeople(Solo48):
    icon_id = 'graduate-with-two-people'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('graduate', 'people', 'group', 'education', 'mortarboard', 'classroom')

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

        self.add_polyline('cap',(12,12),(24,6),(36,12),(30,15),(24,18),(18,15),closed=True)
        self.add_line('face-left',(18,15),(18,22))
        self.add_arc('face-bottom',(18,22),(30,22),radius_x=6,sweep=False)
        self.add_line('face-right',(30,22),(30,15))
        self.add_contour('face','face-left','face-bottom','face-right')
        self.relate('connect','cap','face')
        self.add_arc('central-left',(14,42),(24,37),radius_x=10,radius_y=5)
        self.add_arc('central-right',(24,37),(34,42),radius_x=10,radius_y=5)
        self.add_contour('central-shoulders','central-left','central-right')
        for side,x in (('left',9),('right',39)):
            self.circle(side+'-head',x,30,2)
        self.add_arc('left-outer',(6,37),(9,32),radius_x=3,radius_y=5)
        self.add_arc('left-inner',(9,32),(14,42),radius_x=5,radius_y=10)
        self.add_contour('left-shoulders','left-outer','left-inner')
        self.add_arc('right-inner',(34,42),(39,32),radius_x=5,radius_y=10)
        self.add_arc('right-outer',(39,32),(42,37),radius_x=3,radius_y=5)
        self.add_contour('right-shoulders','right-inner','right-outer')
        for side in ('left','right'):
            self.relate('connect',side+'-head',side+'-shoulders')
            self.relate('connect',side+'-shoulders','central-shoulders')
