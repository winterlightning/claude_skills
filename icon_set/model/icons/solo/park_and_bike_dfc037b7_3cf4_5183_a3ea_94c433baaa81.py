from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfc037b7-3cf4-5183-a3ea-94c433baaa81'
SOURCE_PATH = 'icon_set/work/todo-references/park and bike_dfc037b7-3cf4-5183-a3ea-94c433baaa81.svg'
AUTHOR = 'gpt-6'
PLAN = 'Park and bike represented by P plus B. Letters retain two B bowls.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; letter stems and tangent semicircular bowls authored on integer grid.'
OMISSIONS = 'No letters omitted; narrow semicircular bowls make room for the plus.'

class Drawing(Solo48):
    icon_id = 'park-and-bike'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('park', 'and', 'bike')

    def circle(self, name, cx, cy, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; members.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')

    def build(self):
        self.add_polyline('p-stem',(4,40),(4,24),(4,8))
        self.add_arc('p-bowl',(4,8),(4,24),radius_x=8);self.relate('connect','p-stem','p-bowl')
        self.add_polyline('plus-horizontal',(21,24),(24,24),(27,24))
        self.add_polyline('plus-vertical',(24,21),(24,24),(24,27));self.relate('connect','plus-horizontal','plus-vertical')
        self.add_polyline('b-stem',(36,40),(36,24),(36,8))
        for i,y in enumerate((8,24)):
         self.add_arc(f'b-bowl-{i}',(36,y),(36,y+16),radius_x=8)
         self.relate('connect','b-stem',f'b-bowl-{i}')
        self.relate('connect','b-bowl-0','b-bowl-1')

KEYSHAPE_INK_BOUNDS = (2, 6, 46, 42)
KEYSHAPE_REASON = 'The side-by-side lettering uses the wide 40×32 centerline envelope.'
