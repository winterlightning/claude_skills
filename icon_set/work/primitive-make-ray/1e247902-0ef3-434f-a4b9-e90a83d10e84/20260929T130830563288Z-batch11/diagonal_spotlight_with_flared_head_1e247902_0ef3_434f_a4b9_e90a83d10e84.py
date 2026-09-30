'The rejected spotlight has a diamond-shaped housing and loses the rounded rear connector and light marks.\nSymbol plan: Round the back housing while preserving the flared angled reflector and clear light rays.\nConstruction: Lucide flashlight: separate reflector and body with a shared slanted seam.\nOmissions: Reduce the rear connector to a rounded housing end; one ray replaces two.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1e247902-0ef3-434f-a4b9-e90a83d10e84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-spotlight-with-flared-head/20260929T125815Z-thuan-mac/reference/spotlight_1e247902-0ef3-434f-a4b9-e90a83d10e84.svg'
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
    icon_id = 'diagonal-spotlight-with-flared-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diagonal', 'spotlight', 'with', 'flared', 'head')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        poly('head',((16,23),(24,6),(42,24),(25,32),(16,23)))
        path(m,'housing',(16,23),('L',(8,31)),('C',(8,37),(5,34),(6,35)),('L',(11,40)),('C',(17,40),(14,43),(15,42)),('L',(25,32)))
        join('housing','head')
        line('ray',(35,38),(39,42))
