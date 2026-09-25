'Two falling bombs staggered diagonally. Each has an elongated capsule body and identical straight tail fins. Bounds (6,6)-(42,42).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a92b9733-23c6-4903-9f3a-c893edb5e9f4'
SOURCE_PATH = 'pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-falling-bombs-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('two', 'falling', 'bombs', 'solo')

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
        for i,(x,y) in enumerate(((6,6),(30,18))):
         path(f'bomb-{i}',(x,y+14),[('A',(x+6,y+8),6,6,True),('A',(x+12,y+14),6,6,True),('L',(x+12,y+18)),('A',(x+6,y+24),6,6,True),('A',(x,y+18),6,6,True),('L',(x,y+14))],True)
         poly(f'fins-{i}',(x,y+14),(x,y),(x+6,y+4),(x+12,y),(x+12,y+14));join(f'fins-{i}',f'bomb-{i}')
