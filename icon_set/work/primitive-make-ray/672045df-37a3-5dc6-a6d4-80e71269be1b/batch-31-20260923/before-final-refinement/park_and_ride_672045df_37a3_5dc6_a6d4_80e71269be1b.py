from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '672045df-37a3-5dc6-a6d4-80e71269be1b'
SOURCE_PATH = 'icon_set/work/todo-references/park and ride_672045df-37a3-5dc6-a6d4-80e71269be1b.svg'
AUTHOR = 'gpt-6'
PLAN = 'Park and ride represented by P plus R. Shared uppercase height and bowl geometry.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; hand-authored P/R with shared bowl parameters.'
OMISSIONS = 'No letters omitted; narrow semicircular bowls make room for the plus.'

class Drawing(Solo48):
    icon_id = 'park-and-ride'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('park', 'and', 'ride')

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
        for name,x in (('p',4),('r',36)):
         self.add_polyline(name+'-stem',(x,40),(x,24),(x,8))
         self.add_arc(name+'-bowl',(x,8),(x,24),radius_x=8);self.relate('connect',name+'-stem',name+'-bowl')
        self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
        self.add_polyline('plus-vertical',(24,20),(24,24),(24,28));self.relate('connect','plus-horizontal','plus-vertical')
        self.add_line('r-leg',(36,24),(44,40));self.relate('connect','r-stem','r-leg');self.relate('connect','r-bowl','r-leg')
