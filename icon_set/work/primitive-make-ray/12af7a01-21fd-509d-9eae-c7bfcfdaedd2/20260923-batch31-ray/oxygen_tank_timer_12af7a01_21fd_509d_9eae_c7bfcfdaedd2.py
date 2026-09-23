from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '12af7a01-21fd-509d-9eae-c7bfcfdaedd2'
SOURCE_PATH = 'icon_set/work/todo-references/oxygen tank timer_12af7a01-21fd-509d-9eae-c7bfcfdaedd2.svg'
AUTHOR = 'gpt-6'
PLAN = 'An oxygen cylinder with top valve and an offset timer gauge.'
OMISSIONS = 'Gauge numerals omitted.'
LUCIDE_REFERENCE = None

class Drawing(Solo48):
    icon_id = 'oxygen-tank-timer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('oxygen', 'tank', 'timer')
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
        # Symbol plan: An oxygen cylinder with top valve and an offset timer gauge.

        self.box('tank',6,18,16,24,8)
        self.add_polyline('valve',(10,18),(10,10),(18,10),(18,18))
        # Valve contact remains uncertified in this dense candidate.
        self.add_line('stem',(14,10),(14,6));self.add_line('handle',(10,6),(18,6));self.relate('connect','stem','valve');self.relate('connect','stem','handle')
        self.circle('timer',34,14,8)
        self.add_polyline('hands',(34,10),(34,14),(38,14));
        self.add_line('hose',(18,10),(26,10));self.relate('connect','hose','valve')

