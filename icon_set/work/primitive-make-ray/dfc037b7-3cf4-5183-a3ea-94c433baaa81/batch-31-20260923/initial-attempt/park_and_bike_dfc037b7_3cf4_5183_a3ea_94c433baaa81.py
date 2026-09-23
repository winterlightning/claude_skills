from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dfc037b7-3cf4-5183-a3ea-94c433baaa81'
SOURCE_PATH = 'icon_set/work/todo-references/park and bike_dfc037b7-3cf4-5183-a3ea-94c433baaa81.svg'
AUTHOR = 'gpt-6'
PLAN = 'Park and bike represented by P plus B. Letters retain two B bowls.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; letter stems and tangent semicircular bowls authored on integer grid.'
OMISSIONS = 'None; complete P+B retained.'

class Drawing(Solo48):
    icon_id = 'park-and-bike'
    keyshape = Keyshape.HRECT_M
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
        self.letter_p('p',4,10,11,28)
        self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
        self.add_polyline('plus-vertical',(24,20),(24,24),(24,28));self.relate('connect','plus-horizontal','plus-vertical')
        self.add_polyline('b-stem',(33,38),(33,24),(33,10),(37,10))
        self.add_arc('b-upper',(37,10),(37,24),radius_x=7)
        self.add_arc('b-lower',(37,24),(37,38),radius_x=7)
        self.add_line('b-bottom',(37,38),(33,38));self.add_line('b-middle',(33,24),(37,24))
        for a,b in [('b-stem','b-upper'),('b-upper','b-lower'),('b-lower','b-bottom'),('b-bottom','b-stem'),('b-middle','b-stem'),('b-middle','b-upper'),('b-middle','b-lower')]:self.relate('connect',a,b)
