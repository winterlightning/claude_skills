'The rejected coconut half is a front-facing circle bisected by a horizontal line.\nSymbol plan: Tilt the cut rim and give the half a deeper rounded shell in front of the whole coconut.\nConstruction: Lucide citrus original/atomic-debug: clear cut-surface boundary. Reference owns the diagonal foreground half.\nOmissions: Fine concentric inner rim omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '56b93384-adbb-4bc0-859d-6bfa2c2ab4ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whole-and-halved-coconut/20260929T122733Z-thuan-mac/reference/coconut_56b93384-adbb-4bc0-859d-6bfa2c2ab4ef.svg'
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
    icon_id = 'whole-and-halved-coconut'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('whole', 'and', 'halved', 'coconut')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'whole',(9,29),('C',(6,20),(7,28),(6,24)),('C',(20,6),(6,12),(12,6)),('C',(27,8),(23,6),(25,7)))
        path(m,'half',(18,30),('C',(38,18),(16,21),(30,13)),('C',(42,30),(42,21),(42,25)),('C',(30,42),(42,38),(37,42)),('C',(18,30),(24,42),(20,37)),closed=True)
        path(m,'rim',(18,30),('C',(38,18),(26,34),(39,24)));join('rim','half')
