'The rejected coin replaces the reference central ring with a solid dot.\nSymbol plan: Restore a small hollow central ring and four evenly paired satellite dots inside the coin.\nConstruction: No useful exact Lucide match; concentric circular construction from the supplied reference.\nOmissions: Satellite count reduced to four to preserve the hollow central ring.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bdc115ba-5634-462f-867b-442517f1252f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__virtual-coin-crypto-cardano/20260929T122733Z-thuan-mac/reference/virtual coin crypto cardano_bdc115ba-5634-462f-867b-442517f1252f.svg'
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
    path(m,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'virtual-coin-crypto-cardano'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'cardano')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'coin',24,24,20);circle(m,'center-ring',24,24,3)
        for j,p in enumerate(((16,16),(32,16),(32,32),(16,32))):m.add_dot('satellite-'+str(j),p)
