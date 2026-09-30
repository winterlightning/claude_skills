'The rejected egg is a thin tube and the bird nest silhouette has a harsh angular beak.\nSymbol plan: Broaden the egg and smooth the bird body into a round nesting bowl with a small left-facing beak.\nConstruction: Lucide bird and egg inform a coherent bowl silhouette and asymmetric egg arc.\nOmissions: Omit tiny facial detail already absent in the reference.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '24877473-aa74-4eb9-a2ef-3b61dec1c3f5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bird-egg-nest/20260929T125815Z-thuan-mac/reference/eyrie_24877473-aa74-4eb9-a2ef-3b61dec1c3f5.svg'
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
    icon_id = 'bird-egg-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bird', 'egg', 'nest')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'bird',(4,25),('C',(14,26),(8,24),(10,24)),('C',(28,29),(19,29),(23,31)),('L',(28,21)),('L',(24,18)),('C',(33,14),(27,17),(30,14)),('C',(44,25),(40,14),(44,18)),('C',(24,40),(44,34),(35,40)),('C',(4,25),(12,40),(4,34)),closed=True)
        path(m,'egg',(14,26),('C',(17,8),(9,18),(11,8)),('C',(23,19),(22,8),(24,13)))
        join('egg','bird')
