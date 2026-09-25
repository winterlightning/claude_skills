"""A symmetrical school has a domed central tower, flag and arched entrance. Lucide school informs the facade and door. Clock and wing window marks are omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91c383ff-71de-5f74-8a28-750c25f94e52'
SOURCE_PATH = 'pictographic-primitives/school-learning/school building_91c383ff-71de-5f74-8a28-750c25f94e52.svg'
AUTHOR = 'gpt-6'


class SchoolBuilding(Solo48):
    icon_id = 'school-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('school', 'building', 'flag', 'education', 'campus', 'entrance')

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

        self.add_polyline('flag',(24,18),(24,14),(24,6),(36,6),(36,14),(24,14))
        self.add_arc('roof-left',(12,26),(24,18),radius_x=12,radius_y=8)
        self.add_arc('roof-right',(24,18),(36,26),radius_x=12,radius_y=8)
        self.run('facade',(36,26),(36,30),(42,30),(42,42),(28,42),(20,42),(6,42),(6,30),(12,30),(12,26))
        self.add_contour('building','roof-left','roof-right',*[f'facade-{i}' for i in range(1,10)],closed=True)
        self.relate('connect','flag','building')
        self.add_line('door-left',(20,42),(20,36))
        self.add_arc('door-top',(20,36),(28,36),radius_x=4)
        self.add_line('door-right',(28,36),(28,42))
        self.add_contour('door','door-left','door-top','door-right')
        self.relate('connect','door','building')
