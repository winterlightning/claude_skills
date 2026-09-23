from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9847ce4b-7c8d-4186-a368-17c9b4b2e18a'
SOURCE_PATH = 'icon_set/work/todo-references/parking sign_9847ce4b-7c8d-4186-a368-17c9b4b2e18a.svg'
AUTHOR = 'gpt-6'
PLAN = 'Parking sign with tall left post, top bar, short right side and letter P.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; open sign and semicircular letter bowl.'
OMISSIONS = 'None.'

class Drawing(Solo48):
    icon_id = 'parking-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('parking', 'sign')

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
        self.add_polyline('sign',(10,44),(10,4),(38,4),(38,27))
        self.letter_p('p',20,13,9,20)

KEYSHAPE_INK_BOUNDS = (8, 2, 40, 46)
KEYSHAPE_REASON = 'The tall, narrow subject uses the 28×40 centerline envelope.'
