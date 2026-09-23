from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a6bc318-1415-407d-8cee-66dc95d8d15f'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg'
AUTHOR = 'gpt-6'
PLAN = 'A camp flame above a segmented brick fire pit.'
OMISSIONS = 'Six bricks reduced to two blocks to retain open spacing.'
LUCIDE_REFERENCE = 'flame'

class Drawing(Solo48):
    icon_id = 'outdoors-fire-camp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('outdoors', 'fire', 'camp')
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
        # Symbol plan: A camp flame above a segmented brick fire pit.

        self.add_bezier('flame',(24,4),((26,13),(36,16),(32,22)),((29,29),(18,29),(16,22)),((13,17),(17,13),(18,12)),((19,19),(24,16),(24,4)))
        self.box('pit',8,36,32,8,2)
        self.add_line('joint',(24,36),(24,44))
        self.relate('connect','joint','pit')

