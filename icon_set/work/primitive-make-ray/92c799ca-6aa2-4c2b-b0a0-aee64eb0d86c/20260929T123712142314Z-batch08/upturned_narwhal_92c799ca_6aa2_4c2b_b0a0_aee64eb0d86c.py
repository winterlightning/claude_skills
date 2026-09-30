'The rejected narwhal has a square tail block and omits the projecting flipper.\nSymbol plan: Round the tail into two lobes, recover a projecting lower flipper and lengthen the tusk.\nConstruction: No useful local Lucide narwhal match. Supplied reference owns the asymmetrical swimming silhouette.\nOmissions: Fine tusk outline reduced to a single stroke; eye retained.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '92c799ca-6aa2-4c2b-b0a0-aee64eb0d86c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upturned-narwhal/20260929T122733Z-thuan-mac/reference/narwhal_92c799ca-6aa2-4c2b-b0a0-aee64eb0d86c.svg'
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
    path(m,n,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'upturned-narwhal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upturned', 'narwhal')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'animal',(32,16),('C',(13,31),(22,8),(20,21)),('C',(6,28),(12,27),(8,26)),('C',(10,35),(6,32),(7,34)),('C',(6,42),(7,37),(6,39)),('C',(17,36),(12,42),(15,40)),('C',(25,38),(19,37),(22,38)),('C',(29,34),(25,41),(28,39)),('C',(40,24),(36,34),(40,30)),('C',(32,16),(40,19),(36,16)),closed=True)
        line('tusk',(32,16),(42,6));join('animal','tusk');m.add_dot('eye',(30,26))
