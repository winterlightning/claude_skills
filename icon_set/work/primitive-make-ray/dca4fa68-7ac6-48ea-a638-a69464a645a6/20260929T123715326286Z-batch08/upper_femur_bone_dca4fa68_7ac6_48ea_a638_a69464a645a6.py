'The rejected femur has a long curved outer shaft and a small head, reading like a bent tube.\nSymbol plan: Enlarge the rounded femoral head, restore the short inward neck and narrow the straight lower shaft.\nConstruction: No useful exact Lucide anatomy match; supplied femur reference owns the asymmetrical head and projection.\nOmissions: None.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dca4fa68-7ac6-48ea-a638-a69464a645a6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upper-femur-bone/20260929T122733Z-thuan-mac/reference/hip_dca4fa68-7ac6-48ea-a638-a69464a645a6.svg'
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
    icon_id = 'upper-femur-bone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upper', 'femur', 'bone')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'bone',(16,44),('C',(8,26),(16,32),(8,33)),('C',(18,21),(8,17),(14,17)),('C',(22,17),(22,24),(24,21)),('C',(30,4),(18,10),(23,4)),('C',(40,14),(36,4),(40,8)),('C',(31,24),(40,21),(36,24)),('C',(28,34),(27,24),(28,30)),('L',(28,44)))
