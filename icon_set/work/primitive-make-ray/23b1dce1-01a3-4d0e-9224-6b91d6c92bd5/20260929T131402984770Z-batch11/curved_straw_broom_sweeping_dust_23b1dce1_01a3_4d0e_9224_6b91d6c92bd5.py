'The rejected broom reads as a banana with no handle collar or straw structure; dust is a plain circle.\nSymbol plan: Add an explicit handle collar and a flowing straw fan beside a rounded dust puff.\nConstruction: Lucide broom construction: handle separated from a flaring fan, with asymmetry following the sweep.\nOmissions: Omit narrow internal bristles; dust reduced to a single puff.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '23b1dce1-01a3-4d0e-9224-6b91d6c92bd5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-straw-broom-sweeping-dust/20260929T125815Z-thuan-mac/reference/broom sweep 1_23b1dce1-01a3-4d0e-9224-6b91d6c92bd5.svg'
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
    icon_id = 'curved-straw-broom-sweeping-dust'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curved', 'straw', 'broom', 'sweeping', 'dust')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'broom',(6,36),('C',(30,16),(18,30),(26,22)),('L',(34,8)),('C',(39,6),(35,6),(38,6)),('C',(42,12),(42,6),(42,9)),('L',(38,23)),('C',(20,42),(35,33),(28,40)))
        line('collar',(30,16),(38,23));join('collar','broom')
        circle(m,'dust',11,15,5)
