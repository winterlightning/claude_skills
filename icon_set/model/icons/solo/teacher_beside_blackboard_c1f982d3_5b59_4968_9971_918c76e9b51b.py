"""A standing teacher occupies the open left edge of a blackboard. Lucide presentation informs the board corners and user-round the portrait. Hairline and shirt details are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1f982d3-5b59-4968-9971-918c76e9b51b'
SOURCE_PATH = 'pictographic-primitives/school-learning/school teacher_c1f982d3-5b59-4968-9971-918c76e9b51b.svg'
AUTHOR = 'gpt-6'


class TeacherBesideBlackboard(Solo48):
    icon_id = 'teacher-beside-blackboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('teacher', 'blackboard', 'school', 'classroom', 'person', 'lesson')

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

        self.add_line('board-top',(28,6),(38,6))
        self.add_arc('board-tr',(38,6),(42,10),radius_x=4)
        self.add_line('board-right',(42,10),(42,26))
        self.add_arc('board-br',(42,26),(38,30),radius_x=4)
        self.add_line('board-bottom',(38,30),(32,30))
        self.add_contour('board','board-top','board-tr','board-right','board-br','board-bottom')
        self.circle('head',14,11,5)
        self.add_arc('shoulder-left',(6,33),(14,25),radius_x=8)
        self.add_arc('shoulder-right',(14,25),(22,33),radius_x=8)
        self.run('torso',(22,33),(22,34),(18,34),(10,34),(6,34),(6,33))
        self.add_contour('shirt','shoulder-left','shoulder-right',*[f'torso-{j}' for j in range(1,6)],closed=True)
        for side,x in (('left',10),('right',18)):
            self.add_line('leg-'+side,(x,34),(x,42))
            self.relate('connect','shirt','leg-'+side)
