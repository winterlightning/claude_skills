"""A diagonal eraser rests on a surface. Lucide eraser informs the angled body and seam; broad round joins replace finer corner fillets."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '653b6e95-6217-5c87-ba73-9e0f24cbd72f'
SOURCE_PATH = 'pictographic-primitives/school-learning/eraser_653b6e95-6217-5c87-ba73-9e0f24cbd72f.svg'
AUTHOR = 'gpt-6'


class Eraser(Solo48):
    icon_id = 'eraser'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('eraser', 'rubber', 'stationery', 'school', 'correction', 'drawing')

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

        self.add_polyline('eraser',(6,30),(14,22),(30,6),(42,18),(26,34),(18,42),(14,42),(6,34),closed=True)
        self.add_line('seam',(14,22),(26,34))
        self.add_line('surface',(18,42),(38,42))
        self.relate('connect','eraser','seam')
        self.relate('connect','eraser','surface')
