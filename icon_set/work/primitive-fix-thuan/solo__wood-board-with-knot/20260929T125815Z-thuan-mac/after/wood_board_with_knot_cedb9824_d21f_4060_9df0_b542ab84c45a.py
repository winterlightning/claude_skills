'The rejected board omits the flowing wood grain and leaves only a knot in a frame.\nSymbol plan: Restore a flowing grain split around a larger oval knot.\nConstruction: No useful Lucide match; shared rounded board and mirrored grain owners preserve the landscape form.\nOmissions: One flowing grain stream joins the knot; omit extra parallel bands that would crowd it.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cedb9824-d21f-4060-9df0-b542ab84c45a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wood-board-with-knot/20260929T125815Z-thuan-mac/reference/wood material_cedb9824-d21f-4060-9df0-b542ab84c45a.svg'
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
    icon_id = 'wood-board-with-knot'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wood', 'board', 'with', 'knot')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)

        box(m,'board',4,8,44,40,4)
        oval(m,'knot',24,24,5,4)
        path(m,'grain-left',(4,17),('C',(19,24),(13,17),(10,24)))
        path(m,'grain-right',(29,24),('C',(44,31),(38,24),(35,31)))
        join('board','grain-left');join('board','grain-right');join('knot','grain-left');join('knot','grain-right')

