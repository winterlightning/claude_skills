'The rejected diamonds overwhelm the junction and reduce its vertical stem to a stub.\nSymbol plan: Rebalance two compact diamonds above diagonal branches and a long stem ending in a circle.\nConstruction: Lucide diamond and git-fork inform mirrored nodes and explicit shared attachment points.\nOmissions: No secondary details omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'be7a207d-fbb5-43cc-8ca3-45bc04189f5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__y-junction-with-diamond-ends/20260929T125815Z-thuan-mac/reference/cable split_be7a207d-fbb5-43cc-8ca3-45bc04189f5c.svg'
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
    icon_id = 'y-junction-with-diamond-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('y', 'junction', 'with', 'diamond', 'ends')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        for side,x in [('left',12),('right',36)]:
         poly(side,((x,6),(x+6,12),(x,18),(x-6,12),(x,6)))
         line(side+'-branch',(x,18),(24,26));join(side,side+'-branch')
        line('stem',(24,26),(24,32));join('left-branch','right-branch');join('left-branch','stem');join('right-branch','stem')
        path(m,'terminal',(24,32),('A',(24,42),5,5,True),('A',(24,32),5,5,True),closed=True)
        join('terminal','stem')
