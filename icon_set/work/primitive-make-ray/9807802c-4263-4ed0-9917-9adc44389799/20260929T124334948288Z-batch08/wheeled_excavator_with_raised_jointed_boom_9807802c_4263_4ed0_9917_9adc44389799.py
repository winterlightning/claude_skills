'The rejected excavator bucket is a small hook and the wheels are undersized.\nSymbol plan: Rebalance the paired wheels, lower the cab/body band and open the bucket into a broad curved scoop.\nConstruction: No useful exact local Lucide excavator match; reference owns wheeled chassis, articulated boom and scoop.\nOmissions: Hydraulic lines and interior cab detail omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9807802c-4263-4ed0-9917-9adc44389799'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheeled-excavator-with-raised-jointed-boom/20260929T122733Z-thuan-mac/reference/digger_9807802c-4263-4ed0-9917-9adc44389799.svg'
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
    icon_id = 'wheeled-excavator-with-raised-jointed-boom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wheeled', 'excavator', 'with', 'raised', 'jointed', 'boom')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'rear-wheel',9,39,3);circle(m,'front-wheel',24,39,3)
        box(m,'body',6,18,28,26,3)
        poly('cab',(10,18),(10,10),(20,10),(24,18));join('cab','body')
        poly('boom',(28,18),(38,6),(42,24));join('boom','body')
        path(m,'bucket',(42,24),('L',(42,28)),('C',(34,34),(42,34),(38,36)),('L',(33,30)));join('bucket','boom')
