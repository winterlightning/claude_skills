from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dfc037b7-3cf4-5183-a3ea-94c433baaa81'
SOURCE_PATH = 'icon_set/work/todo-references/park and bike_dfc037b7-3cf4-5183-a3ea-94c433baaa81.svg'
AUTHOR = 'gpt-6'
PLAN = 'P plus B lettering for park and bike.'
OMISSIONS = 'No letters omitted.'
LUCIDE_REFERENCE = 'square-parking'

class Drawing(Solo48):
    icon_id = 'park-and-bike'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('park', 'and', 'bike')
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
        # Symbol plan: P plus B lettering for park and bike.

        self.p('p',4,10,12,28)
        self.add_line('plus-h',(20,24),(28,24));self.add_line('plus-v',(24,20),(24,28));self.relate('connect','plus-h','plus-v')
        self.add_line('b-stem-1',(32,38),(32,10));self.add_line('b-stem-2',(32,10),(38,10))
        self.add_arc('b-upper',(38,10),(38,24),radius_x=6,radius_y=7)
        self.add_arc('b-lower',(38,24),(38,38),radius_x=6,radius_y=7)
        self.add_line('b-foot',(38,38),(32,38));self.add_contour('b','b-stem-1','b-stem-2','b-upper','b-lower','b-foot',closed=True)
        self.add_line('b-middle',(32,24),(38,24));self.relate('connect','b-middle','b')

