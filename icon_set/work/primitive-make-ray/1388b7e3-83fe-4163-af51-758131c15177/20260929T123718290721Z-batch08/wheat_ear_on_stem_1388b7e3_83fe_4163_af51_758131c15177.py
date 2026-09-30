'The rejected wheat grains form stacked semicircular bowls instead of pointed kernels.\nSymbol plan: Use a pointed terminal kernel and a mirrored pair of slanted pointed side kernels on a long stem.\nConstruction: Lucide wheat original and atomic-debug: pointed repeated grain loops attached to a shared stem.\nOmissions: Three pairs reduced to one broad pair to preserve open grain interiors.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1388b7e3-83fe-4163-af51-758131c15177'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheat-ear-on-stem/20260929T122733Z-thuan-mac/reference/gran_1388b7e3-83fe-4163-af51-758131c15177.svg'
AUTHOR = 'gpt-6'

def path(m,n,start,*steps,closed=False):
    names=[]; here=start
    for j,(kind,end,*args) in enumerate(steps):
        k=f'{n}-{j}'
        if kind=='L':m.add_line(k,here,end)
        elif kind=='C':m.add_bezier(k,here,(args[0],args[1],end))
        elif kind=='A':m.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        names.append(k);here=end
    m.add_contour(n,*names,closed=closed)
def circle(m,n,x,y,r):
    path(m,n,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'wheat-ear-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wheat', 'ear', 'on', 'stem')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'terminal',(24,4),('C',(30,12),(27,7),(30,8)),('C',(24,20),(30,16),(27,18)),('C',(18,12),(21,18),(18,16)),('C',(24,4),(18,8),(21,7)),closed=True)
        line('stem',(24,20),(24,44));join('stem','terminal')
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         path(m,'grain'+str(side),p(0,36),('C',p(16,24),p(0,28),p(10,24)),('C',p(0,36),p(16,34),p(10,36)),closed=True)
         join('grain'+str(side),'stem')
        join('grain-1','grain1')
