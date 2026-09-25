'Three equal circular atoms form a triangle joined by three exact straight bonds. Bounds (6,6)-(42,42).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f6112893-74f5-4941-8d09-471ef8c89a26'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ozone_f6112893-74f5-4941-8d09-471ef8c89a26.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangular-ozone-molecule'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('triangular', 'ozone', 'molecule')

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
        # Cardinal circle nodes keep all bonds attached exactly.
        circle('left',12,24,6);circle('top',36,12,6);circle('bottom',36,36,6)
        line('upper-bond',(12,18),(30,12));join('upper-bond','left');join('upper-bond','top')
        line('lower-bond',(12,30),(30,36));join('lower-bond','left');join('lower-bond','bottom')
        line('right-bond',(36,18),(36,30));join('right-bond','top');join('right-bond','bottom')
