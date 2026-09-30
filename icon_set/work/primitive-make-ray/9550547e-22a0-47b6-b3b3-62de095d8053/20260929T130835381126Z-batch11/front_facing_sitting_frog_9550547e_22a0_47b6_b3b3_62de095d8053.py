'The rejected frog has pinched eye bulges and tangled forelegs and haunches.\nSymbol plan: Use a wide frog head with smooth eye bulges over a broad seated body, two simple front legs and rounded haunches.\nConstruction: No useful Lucide animal match; shared mirrored eye and leg definitions preserve the front view.\nOmissions: Omit tiny eyes and mouth, as in the blank reference face; avoid extra foot loops.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9550547e-22a0-47b6-b3b3-62de095d8053'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-facing-sitting-frog/20260929T125815Z-thuan-mac/reference/frog_9550547e-22a0-47b6-b3b3-62de095d8053.svg'
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
    icon_id = 'front-facing-sitting-frog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('front', 'facing', 'sitting', 'frog')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'head',(14,26),('C',(10,17),(9,24),(8,20)),('C',(18,6),(9,8),(12,6)),('C',(24,10),(21,6),(22,10)),('C',(30,6),(26,10),(27,6)),('C',(38,17),(36,6),(39,8)),('C',(34,26),(40,20),(39,24)),('L',(14,26)),closed=True)
        path(m,'body',(14,26),('C',(6,36),(7,26),(6,31)),('C',(12,42),(6,40),(8,42)),('L',(36,42)),('C',(42,36),(40,42),(42,40)),('C',(34,26),(42,31),(41,26)))
        join('head','body')
        for n,x in [('left',18),('right',30)]:
         line(n,(x,34),(x,42));join(n,'body')
