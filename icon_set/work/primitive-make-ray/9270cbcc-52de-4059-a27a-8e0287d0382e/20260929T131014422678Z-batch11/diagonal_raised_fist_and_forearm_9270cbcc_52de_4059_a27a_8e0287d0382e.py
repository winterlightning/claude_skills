'The rejected fist reads as a wrench because the knuckles are straight and the thumb is unclear.\nSymbol plan: Shape rounded knuckles along the diagonal fist and preserve a folded thumb above the forearm.\nConstruction: Shared human hand reference and Lucide hand guide knuckle lobes and a coherent thumb crease.\nOmissions: Reduce internal finger creases to one to keep the fist open at 48 pixels.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9270cbcc-52de-4059-a27a-8e0287d0382e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-raised-fist-and-forearm/20260929T125815Z-thuan-mac/reference/artificial arm_9270cbcc-52de-4059-a27a-8e0287d0382e.svg'
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
    icon_id = 'diagonal-raised-fist-and-forearm'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diagonal', 'raised', 'fist', 'and', 'forearm')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)

        path(m,'arm',(6,34),('L',(18,22)),('C',(18,14),(14,18),(15,17)),('L',(24,8)),('C',(28,6),(25,6),(26,6)),('C',(31,10),(30,6),(31,8)),('C',(36,14),(35,9),(38,11)),('C',(42,20),(40,13),(42,16)),('C',(40,26),(42,22),(42,24)),('L',(30,34)),('C',(24,34),(28,36),(26,36)),('L',(16,42)))
        path(m,'thumb',(31,10),('L',(28,21)),('L',(34,27)))
        join('arm','thumb')

