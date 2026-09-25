'Shop with three scalloped awning panels over a centered doorway. Shared panel width and mirror symmetry. Bounds (6,6)-(42,42).\nConstruction: Lucide store: consistent repeated scallops and centered entrance.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a142829-c797-44e6-bde7-efc15341b72d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/store_8a142829-c797-44e6-bde7-efc15341b72d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'storefront'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('storefront',)

    def build(self):

        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        path('awning',(6,18),[('L',(10,6)),('L',(38,6)),('L',(42,18)),('A',(30,18),6,6,True),('A',(18,18),6,6,True),('A',(6,18),6,6,True)],True)
        for x in (18,30):line(f'seam-{x}',(x,6),(x,18));join(f'seam-{x}','awning')
        poly('shop',(12,24),(12,42),(20,42),(28,42),(36,42),(36,24));join('shop','awning')
        poly('door',(20,42),(20,33),(28,33),(28,42));join('door','shop')
