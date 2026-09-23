from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7ade5dac-3851-477f-ac45-3ecabf8df504'
SOURCE_PATH = 'icon_set/work/todo-references/parking p_7ade5dac-3851-477f-ac45-3ecabf8df504.svg'
AUTHOR = 'gpt-6'
PLAN = 'Front-facing car under an overlapping circular P parking badge. Car sides and wheels mirror about x=21.'
CONSTRUCTION_REFERENCES = 'monitor: rounded car fascia; circle construction for the parking badge.'
OMISSIONS = 'Headlamp pair reduced to two dots; small tire outlines reduced to strokes.'

class Drawing(Solo48):
    icon_id = 'parking-p'
    keyshape = Keyshape.SQUARE
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
        self.circle('badge',32,16,10)
        self.letter_p('p',29,10,7,12)
        self.add_polyline('roof',(8,30),(12,23),(22,23))
        self.box('car',6,30,32,8,3)
        for i,x in enumerate((12,32)):
            self.add_line(f'wheel-{i}',(x,38),(x,42));self.relate('connect','car',f'wheel-{i}')
        for i,x in enumerate((13,31)):self.add_dot(f'lamp-{i}',(x,34))

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
