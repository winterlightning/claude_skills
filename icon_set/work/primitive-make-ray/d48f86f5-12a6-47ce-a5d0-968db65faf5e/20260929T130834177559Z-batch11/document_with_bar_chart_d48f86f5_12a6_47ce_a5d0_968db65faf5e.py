'The rejected document is square and compresses the page/chart proportions.\nSymbol plan: Restore a portrait page and a three-column chart anchored to a baseline.\nConstruction: Lucide chart-column informs equal bar spacing and a shared baseline; file-image informs the clipped page.\nOmissions: Omit tiny top corner fold seam.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd48f86f5-12a6-47ce-a5d0-968db65faf5e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__document-with-bar-chart/20260929T125815Z-thuan-mac/reference/file data bars_d48f86f5-12a6-47ce-a5d0-968db65faf5e.svg'
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
    icon_id = 'document-with-bar-chart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('document', 'with', 'bar', 'chart')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        poly('page',((8,4),(30,4),(40,14),(40,44),(8,44),(8,4)))
        poly('baseline',((16,34),(24,34),(32,34)))
        for name,x,y in [('tall',16,16),('mid',24,22),('short',32,27)]:
         line(name,(x,y),(x,34));join('baseline',name)
