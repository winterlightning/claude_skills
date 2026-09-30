'The rejected cocoa pod reads as a generic pointed leaf and loses its stem and curved pod body.\nSymbol plan: Restore a short stem and an elongated round-shouldered pod containing three seeds.\nConstruction: Lucide leaf contributes one coherent outer contour; the three seeds use one repeat definition.\nOmissions: Omit the inset cut rim and render seeds as short rounded marks to meet clearance.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a38a1dfc-66a1-438a-847f-a5131386c188'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__opened-cocoa-pod-with-three-seeds/20260929T125815Z-thuan-mac/reference/cocoa_a38a1dfc-66a1-438a-847f-a5131386c188.svg'
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
    icon_id = 'opened-cocoa-pod-with-three-seeds'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('opened', 'cocoa', 'pod', 'with', 'three', 'seeds')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        line('stem',(24,4),(24,8))
        path(m,'pod',(24,8),('C',(40,25),(35,8),(40,16)),('C',(24,44),(40,34),(30,42)),('C',(8,25),(18,42),(8,34)),('C',(24,8),(8,16),(13,8)),closed=True)
        join('stem','pod')
        for n,y in enumerate((17,25,33)):
         line('seed'+str(n),(24,y),(25,y))
