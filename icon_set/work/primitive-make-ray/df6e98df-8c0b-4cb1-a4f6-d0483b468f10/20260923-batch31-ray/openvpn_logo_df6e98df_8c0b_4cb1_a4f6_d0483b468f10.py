from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df6e98df-8c0b-4cb1-a4f6-d0483b468f10'
SOURCE_PATH = 'icon_set/work/todo-references/openvpn logo_df6e98df-8c0b-4cb1-a4f6-d0483b468f10.svg'
AUTHOR = 'gpt-6'
PLAN = 'OpenVPN circular arch around a keyhole; bilateral logo silhouette.'
OMISSIONS = 'Logo fill translated to consistent outline.'
LUCIDE_REFERENCE = None

class Drawing(Solo48):
    icon_id = 'openvpn-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('openvpn', 'logo')
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
        # Symbol plan: OpenVPN circular arch around a keyhole; bilateral logo silhouette.

        self.add_arc('ring',(8,36),(40,36),radius_x=20,large_arc=True)
        self.add_arc('key-head',(20,26),(28,26),radius_x=6,large_arc=True)
        self.add_polyline('key-base',(28,26),(31,40),(17,40),(20,26))
        self.relate('connect','key-head','key-base')

