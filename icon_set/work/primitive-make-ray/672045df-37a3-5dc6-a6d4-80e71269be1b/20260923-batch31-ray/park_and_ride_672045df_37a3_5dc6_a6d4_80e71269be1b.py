from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '672045df-37a3-5dc6-a6d4-80e71269be1b'
SOURCE_PATH = 'icon_set/work/todo-references/park and ride_672045df-37a3-5dc6-a6d4-80e71269be1b.svg'
AUTHOR = 'gpt-6'
PLAN = 'P plus R lettering for park and ride.'
OMISSIONS = 'No letters omitted.'
LUCIDE_REFERENCE = 'square-parking'

class Drawing(Solo48):
    icon_id = 'park-and-ride'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('park', 'and', 'ride')
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
        # Symbol plan: P plus R lettering for park and ride.

        self.p('p',4,10,12,28)
        self.add_line('plus-h',(20,24),(28,24));self.add_line('plus-v',(24,20),(24,28));self.relate('connect','plus-h','plus-v')
        self.p('r',32,10,12,28)
        self.add_line('r-leg',(32,24),(44,38));self.relate('connect','r-leg','r')

