from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b569bafc-f80a-44b7-a43f-233891818936'
SOURCE_PATH = 'icon_set/work/todo-references/passport hand_b569bafc-f80a-44b7-a43f-233891818936.svg'
AUTHOR = 'gpt-6'
PLAN = 'A passport booklet with top cover flap and a latitude-longitude globe.'
OMISSIONS = 'Latitude bands reduced to one equator; curved meridians reduced to a central vertical meridian.'
LUCIDE_REFERENCE = 'globe'

class Drawing(Solo48):
    icon_id = 'passport-hand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('passport', 'hand')
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
        # Symbol plan: A passport booklet with top cover flap and a latitude-longitude globe.

        self.box('cover',8,4,32,40,3)
        self.add_line('flap',(8,12),(40,12));self.relate('connect','flap','cover')
        self.circle('globe',24,28,7)
        self.add_line('meridian',(24,21),(24,35));self.relate('connect','meridian','globe')
        self.add_line('equator',(17,28),(31,28));self.relate('connect','equator','globe');self.relate('connect','equator','meridian')

