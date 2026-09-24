from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f422872b-42cf-4b74-aa1f-bf870f557d7a'
SOURCE_PATH = 'icon_set/work/todo-references/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg'
AUTHOR = 'gpt-6'
PLAN = 'Pantyhose with one straight leg and one bent crossing leg, open at the waist.'
CONSTRUCTION_REFERENCES = 'Shared human-reference.md/full_body_ref.png: coherent bent limb strokes and simple anatomy. No detached head.'
OMISSIONS = 'Fine ankle wrinkles omitted; crossing leg and toe shapes retained.'

class Drawing(Solo48):
    icon_id = 'pantyhose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('pantyhose',)

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
        # Human-reference.md: coherent bent limb; no head or detached-head rule applies.
        self.add_line('waist-1',(16,4),(28,4));self.add_line('waist-2',(28,4),(28,12))
        self.add_bezier('outer-thigh',(28,12),((32,15),(40,17),(40,22)),((40,26),(34,30),(28,34)))
        self.add_line('outer-calf',(28,34),(12,44))
        self.add_line('toe-1',(12,44),(8,36));self.add_line('toe-2',(8,36),(28,24))
        self.add_bezier('inner-thigh',(28,24),((24,23),(17,22),(14,19)),((10,15),(16,9),(16,4)))
        self.add_contour('bent-leg','waist-1','waist-2','outer-thigh','outer-calf','toe-1','toe-2','inner-thigh',closed=True)
        self.add_line('rear-thigh',(14,19),(14,24));self.relate('connect','bent-leg','rear-thigh')
        self.add_bezier('rear-shin',(28,34),((28,40),(30,44),(34,44)),((35,44),(37,44),(38,44)))
        self.relate('connect','bent-leg','rear-shin')

KEYSHAPE_INK_BOUNDS = (8, 2, 40, 46)
KEYSHAPE_REASON = 'The tall, narrow subject uses the 28×40 centerline envelope.'
