from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df632f40-c8e3-4ae9-9986-caca559c4210'
SOURCE_PATH = 'icon_set/work/todo-references/passport globe_df632f40-c8e3-4ae9-9986-caca559c4210.svg'
AUTHOR = 'gpt-6'
PLAN = 'Passport in front of a globe with a second globe on its cover.'
OMISSIONS = 'Fine geographic border simplified; meridian count reduced.'
LUCIDE_REFERENCE = 'globe'

class Drawing(Solo48):
    icon_id = 'passport-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('passport', 'globe')
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
        # Symbol plan: Passport in front of a globe with a second globe on its cover.

        self.add_arc('earth',(20,34),(34,20),radius_x=14,large_arc=True)
        self.add_polyline('land',(6,16),(16,16),(16,24),(12,26),(12,32))
        self.box('passport',24,18,18,24,3)
        self.circle('globe',33,29,7)
        self.add_line('equator',(26,29),(40,29));self.relate('connect','equator','globe')
        self.add_line('meridian',(33,22),(33,36));self.relate('connect','meridian','globe');self.relate('connect','meridian','equator')

