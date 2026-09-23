from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '186ecce7-6734-413e-9fd9-e45cba4787b3'
SOURCE_PATH = 'icon_set/work/todo-references/outpost 1_186ecce7-6734-413e-9fd9-e45cba4787b3.svg'
AUTHOR = 'gpt-6'
PLAN = 'A small outpost hut behind a front security terminal.'
OMISSIONS = 'Terminal dash omitted to keep the small opening clear.'
LUCIDE_REFERENCE = 'house'

class Drawing(Solo48):
    icon_id = 'outpost-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('outpost', '1')
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
        # Symbol plan: A small outpost hut behind a front security terminal.

        self.add_polyline('roof',(6,20),(8,18),(24,6),(40,18),(42,20))
        for side,x in [('left',8),('right',40)]: self.add_line(side,(x,18),(x,34)); self.relate('connect',side,'roof')
        self.box('terminal',17,26,14,16,3)
        self.add_line('screen-rule',(17,34),(31,34));self.relate('connect','screen-rule','terminal')

