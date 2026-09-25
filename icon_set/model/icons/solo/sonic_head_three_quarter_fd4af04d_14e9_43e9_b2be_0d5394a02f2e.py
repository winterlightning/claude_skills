'Sonic hedgehog head in three-quarter view. Swept curved spines, projecting muzzle, pointed ear and oval eye. Bounds (6,6)-(42,42).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: Fine eye/muzzle partition and second pupil omitted to keep the face open at 48px.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fd4af04d-14e9-43e9-b2be-0d5394a02f2e'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-10/sonic_fd4af04d-14e9-43e9-b2be-0d5394a02f2e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sonic-head-three-quarter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('sonic', 'head', 'three', 'quarter')

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
        path('head',(10,20),[('L',(10,8)),('L',(19,12)),('C',(39,6),(25,8),(33,6)),('L',(35,16)),('C',(42,23),(39,17),(42,20)),('L',(35,26)),('C',(42,35),(40,29),(42,32)),('C',(26,42),(35,36),(33,42)),('L',(18,42)),('A',(6,30),12,12,True),('L',(10,28)),('L',(10,20))],True)
        line('eye-left',(19,22),(19,23))
        line('eye-right',(27,22),(27,23))
        path('smile',(18,33),[('C',(28,32),(22,34),(25,34))])
