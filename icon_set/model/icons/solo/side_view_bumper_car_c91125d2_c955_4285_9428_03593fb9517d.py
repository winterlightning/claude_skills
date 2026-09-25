'Bumper car side silhouette. Single rounded nose flowing into the seat recess, high rear body and vertical power pole. Bounds (6,6)-(42,42).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c91125d2-c955-4285-9428-03593fb9517d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bumper_c91125d2-c955-4285-9428-03593fb9517d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-bumper-car'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('side', 'view', 'bumper', 'car')

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
        path('bumper',(10,34),[('L',(38,34)),('A',(42,38),4,4,True),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('A',(10,34),4,4,True)],True)
        path('body',(10,34),[('C',(18,22),(10,26),(12,22)),('L',(20,22)),('A',(24,26),4,4,False),('L',(28,26)),('A',(32,22),4,4,False),('L',(32,20)),('A',(38,14),6,6,True),('L',(42,14)),('L',(42,34)),('L',(38,34))]);join('body','bumper')
        line('pole',(42,6),(42,14));join('pole','body')
