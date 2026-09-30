'The rejected stick is a broad pill with almost no straight shaft.\nSymbol plan: Restore a slender upright capsule with long parallel sides and equal round ends, touching the radial envelope at top and bottom.\nConstruction: No useful exact Lucide stick match; equal semicircle ends and parallel sides.\nOmissions: None.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f1812b29-5916-4da7-b92a-60c32ffd784f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-rounded-stick/20260929T122733Z-thuan-mac/reference/stick_f1812b29-5916-4da7-b92a-60c32ffd784f.svg'
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
    icon_id = 'upright-rounded-stick'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'rounded', 'stick')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'stick',(20,8),('A',(28,8),4,4,True),('L',(28,40)),('A',(20,40),4,4,True),('L',(20,8)),closed=True)
