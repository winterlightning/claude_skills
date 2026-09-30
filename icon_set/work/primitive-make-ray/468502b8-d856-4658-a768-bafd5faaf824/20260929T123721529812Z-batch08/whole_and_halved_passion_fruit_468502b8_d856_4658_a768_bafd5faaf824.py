'The rejected passion fruit half is a flat circle, with no bowl depth.\nSymbol plan: Restore a horizontal cut opening and rounded lower shell in front of the whole fruit.\nConstruction: Lucide citrus original/atomic-debug: distinct cut face and shell; source owns the front-left cut half.\nOmissions: Scalloped supporting flourish and fine interior detail omitted; one seed mark retained.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '468502b8-d856-4658-a768-bafd5faaf824'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whole-and-halved-passion-fruit/20260929T122733Z-thuan-mac/reference/exotic food passion fruit_468502b8-d856-4658-a768-bafd5faaf824.svg'
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
    icon_id = 'whole-and-halved-passion-fruit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('whole', 'and', 'halved', 'passion', 'fruit')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        oval(m,'cut-face',18,26,12,8)
        path(m,'shell',(6,26),('C',(18,42),(6,37),(10,42)),('C',(30,26),(26,42),(30,37)))
        join('shell','cut-face')
        path(m,'whole',(18,18),('C',(30,6),(18,10),(24,6)),('C',(42,20),(38,6),(42,12)),('C',(30,26),(42,29),(36,31)))
        join('whole','cut-face');join('whole','shell');m.add_dot('seed',(18,26))
