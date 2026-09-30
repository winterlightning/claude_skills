'The rejected helmet face has tiny filled eyes and a smiling jaw, opposite to the reference expression.\nSymbol plan: Make the helmet broader and flatter, restore hollow eyes and a downturned mouth.\nConstruction: No useful Lucide character match; mirrored helmet corners and paired round eyes.\nOmissions: Omit the separate inner cheek contour to give the eyes and expression room.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '598d228b-5936-4dbd-bec8-6034163e03d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__keroro-face-in-helmet/20260929T125815Z-thuan-mac/reference/keroro frog alien_598d228b-5936-4dbd-bec8-6034163e03d3.svg'
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
    icon_id = 'keroro-face-in-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('keroro', 'face', 'in', 'helmet')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'helmet',(4,40),('L',(4,20)),('A',(16,8),12,12,True),('L',(32,8)),('A',(44,20),12,12,True),('L',(44,40)))
        circle(m,'left-eye',16,23,3);circle(m,'right-eye',32,23,3)
        path(m,'frown',(18,36),('C',(30,36),(20,31),(28,31)))
