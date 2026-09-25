'Front-facing brassiere. Mirrored teardrop cups, shared axis x24; straps and bridge join at explicit nodes. Bounds (4,8)-(44,40).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5380d751-85f9-4464-925b-e95585da15a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bra_5380d751-85f9-4464-925b-e95585da15a3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-cup-brassiere'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rounded', 'cup', 'brassiere')

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
        for k in range(2):
         def p(x,y): return (x if k==0 else 48-x,y)
         path(f'cup-{k}',p(6,22),[('C',p(20,33),p(13,22),p(20,27)),('C',p(12,40),p(20,37),p(16,40)),('C',p(4,32),p(7,40),p(4,37)),('C',p(6,22),p(4,28),p(6,25))],True)
         line(f'strap-{k}',p(6,8),p(6,22));join(f'strap-{k}',f'cup-{k}')
        line('bridge',(20,33),(28,33));join('bridge','cup-0');join('bridge','cup-1')
