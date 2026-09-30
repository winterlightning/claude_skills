'The rejected flow loses one rectangular output and most of the original branching data movement.\nSymbol plan: Restore two rectangular output bars, hollow input dots and curved rightward movement.\nConstruction: Lucide git-fork construction informs shared flow endpoints; deliberate left-to-right asymmetry.\nOmissions: Two input circles replace three; output rectangles become compact solid bars, preserving their pair and position; one rightward arrow remains.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd1e42083-a36c-4e25-bb45-512c8c5a0866'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__data-shapes-flowing-to-the-right/20260929T125815Z-thuan-mac/reference/amazon web service glue data brew visual data preparation_d1e42083-a36c-4e25-bb45-512c8c5a0866.svg'
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
    icon_id = 'data-shapes-flowing-to-the-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('data', 'shapes', 'flowing', 'to', 'the', 'right')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)

        circle(m,'input-top',7,21,3);circle(m,'input-bottom',7,35,3)
        line('output-left',(32,16),(32,24));line('output-right',(44,16),(44,24))
        path(m,'flow',(4,8),('L',(10,8)),('C',(19,20),(19,8),(19,14)),('L',(19,28)),('C',(44,36),(19,36),(30,36)))
        poly('arrow',((38,32),(44,36),(38,40)));join('flow','arrow')

