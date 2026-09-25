'Ice cream scoop above a tapered cone. Circular dome, mirrored lip lobes and straight cone sides. Bounds (8,4)-(40,44).\nConstruction: Lucide ice-cream-cone: coherent scoop and tapered cone.\nOmissions: Small lower scallops simplified into the scoop lip.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c8779f6f-62fb-4888-8a71-929e3faf4151'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-scoop-ice-cream-cone/20260924T160658Z-thuan-mac/reference/ice cream_c8779f6f-62fb-4888-8a71-929e3faf4151.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-scoop-ice-cream-cone-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rounded', 'scoop', 'ice', 'cream', 'cone')

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
        path('scoop',(12,16),[('A',(24,4),12,12,True),('A',(36,16),12,12,True),('C',(40,21),(36,19),(40,18)),('A',(35,26),5,5,True),('L',(13,26)),('A',(8,21),5,5,True),('C',(12,16),(8,18),(12,19))],True)
        poly('cone',(13,26),(24,44),(35,26));join('cone','scoop')
