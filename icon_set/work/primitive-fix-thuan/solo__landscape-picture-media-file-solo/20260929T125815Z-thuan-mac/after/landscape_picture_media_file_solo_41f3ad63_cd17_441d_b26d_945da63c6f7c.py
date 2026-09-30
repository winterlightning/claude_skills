'The rejected landscape page has only a single open mountain peak.\nSymbol plan: Restore two unequal mountain peaks beneath the sun on a portrait file with a clipped corner.\nConstruction: Lucide file-image supplies page and landscape nesting; unequal peaks match the source.\nOmissions: Keep the mountain ridge open so a small enclosed triangle does not fill in.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41f3ad63-cd17-441d-b26d-945da63c6f7c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__landscape-picture-media-file-solo/20260929T125815Z-thuan-mac/reference/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg'
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
    icon_id = 'landscape-picture-media-file-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('landscape', 'picture', 'media', 'file', 'solo')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        poly('page',((8,4),(30,4),(40,14),(40,44),(8,44),(8,4)))
        circle(m,'sun',20,16,3)
        poly('ridge',((16,35),(20,30),(24,34),(29,27),(32,35)))
