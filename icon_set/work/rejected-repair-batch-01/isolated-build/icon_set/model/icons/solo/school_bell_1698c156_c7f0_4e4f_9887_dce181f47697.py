"""A bell has a flared rim, clapper, stem and circular pull. Lucide bell informs the dome and flare; the source supplies the extended pull."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1698c156-c7f0-4e4f-9887-dce181f47697'
SOURCE_PATH = 'pictographic-primitives/school-learning/school bell_1698c156-c7f0-4e4f-9887-dce181f47697.svg'
AUTHOR = 'gpt-6'


class SchoolBell(Solo48):
    icon_id = 'school-bell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('bell', 'school', 'ring', 'clapper', 'sound', 'signal')

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

        self.add_arc('dome-left',(12,16),(24,4),radius_x=12)
        self.add_arc('dome-right',(24,4),(36,16),radius_x=12)
        self.add_line('right-wall',(36,16),(36,20))
        self.add_arc('right-flare',(36,20),(40,28),radius_x=10,sweep=False)
        self.run('rim',(40,28),(24,28),(8,28))
        self.add_arc('left-flare',(8,28),(12,20),radius_x=10,sweep=False)
        self.add_line('left-wall',(12,20),(12,16))
        self.add_contour('bell','dome-left','dome-right','right-wall','right-flare','rim-1','rim-2','left-flare','left-wall',closed=True)
        self.circle('clapper',24,32,4)
        self.add_line('pull-stem',(24,36),(24,40))
        self.circle('pull',24,42,2)
        self.relate('connect','bell','clapper')
        self.relate('connect','clapper','pull-stem')
        self.relate('connect','pull','pull-stem')
