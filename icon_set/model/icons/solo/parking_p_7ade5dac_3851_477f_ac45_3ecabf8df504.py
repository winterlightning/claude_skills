"""parking p: standalone SOLO48 repair.
Plan: Front-facing car partly covered by circular P badge.
Keyshape: VRECT_L; shared dimensions and nodes own repeated elements.
Reduction: Rebalanced to a tall envelope; omitted headlights and hidden roof/fascia strokes; retained P and both wheels. Circle attaches to roof at an exact 5-12-13 point.
Lucide originals and atomic-debug construction reference: car-front.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7ade5dac-3851-477f-ac45-3ecabf8df504'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/parking p_7ade5dac-3851-477f-ac45-3ecabf8df504.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'parking-p'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('parking', 'p')

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
        # Occluding badge dominates a front-facing car; joints are actual shared nodes.
        # Badge radius 13 gives the lower-left 5-12-13 attachment (15,22).
        self.add_arc('badge-a',(15,22),(27,4),radius_x=13)
        self.add_arc('badge-b',(27,4),(40,17),radius_x=13)
        self.add_arc('badge-c',(40,17),(27,30),radius_x=13)
        self.add_arc('badge-d',(27,30),(15,22),radius_x=13)
        self.add_contour('badge','badge-a','badge-b','badge-c','badge-d',closed=True)
        self.circle('p-bowl',27,15,2)
        self.add_line('p-stem',(25,15),(25,21))
        self.relate('connect','p-stem','p-bowl')
        self.add_polyline('car',(15,22),(8,32),(8,40),(12,40),(36,40),(40,40),(40,34))
        self.relate('connect','car','badge-a')
        self.relate('connect','car','badge-d')
        for i,x in enumerate((12,36)):
            self.add_line(f'wheel-{i}',(x,40),(x,44))
            self.relate('connect',f'wheel-{i}','car')
