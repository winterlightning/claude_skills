from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7ade5dac-3851-477f-ac45-3ecabf8df504'
SOURCE_PATH = 'icon_set/work/todo-references/parking p_7ade5dac-3851-477f-ac45-3ecabf8df504.svg'
AUTHOR = 'gpt-6'
PLAN = 'A car under an overlapping circular P parking badge.'
OMISSIONS = 'Small bumper marks omitted.'
LUCIDE_REFERENCE = 'square-parking'

class Drawing(Solo48):
    icon_id = 'parking-p'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('parking', 'p')
    # Pantyhose anatomy reference: icon_set/references/human_ref/full_body_ref.png; no detached head.

    def circle(self, n, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(n+'-a', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(n+'-b', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(points):
            b=points[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2: self.add_arc(name,a,b,radius_x=r)
            else: self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def p(self,n,x,y,w,h):
        # Open P stem and a tangent semicircular bowl share the upper node.
        self.add_line(n+'-stem-1',(x,y+h),(x,y))
        self.add_line(n+'-stem-2',(x,y),(x+w//2,y))
        self.add_arc(n+'-bowl',(x+w//2,y),(x+w//2,y+h//2),radius_x=w//2,radius_y=h//4)
        self.add_line(n+'-return',(x+w//2,y+h//2),(x,y+h//2))
        self.add_contour(n,n+'-stem-1',n+'-stem-2',n+'-bowl',n+'-return')

    def build(self):
        # Symbol plan: A car under an overlapping circular P parking badge.

        self.circle('sign',30,18,12)
        self.p('p',27,12,8,12)
        self.add_polyline('car-roof',(6,32),(11,24),(18,24))
        self.box('car',6,32,28,10,3)
        self.add_line('right-roof',(30,30),(34,32));self.relate('connect','right-roof','sign');self.relate('connect','right-roof','car');self.relate('connect','car-roof','car')

