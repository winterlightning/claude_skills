'The rejected lemon is a small rounded bulb under a disproportionately distant leaf.\nSymbol plan: Elongate the lemon body, smooth its lower tip and bring its mass upward toward the single leaf.\nConstruction: Lucide leaf original/atomic-debug: pointed closed leaf and a short attached stem.\nOmissions: None.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2ce6dd5a-e886-4158-9462-4ec687e19a2f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whole-lemon-with-single-leaf/20260929T122733Z-thuan-mac/reference/citron_2ce6dd5a-e886-4158-9462-4ec687e19a2f.svg'
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
    icon_id = 'whole-lemon-with-single-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('whole', 'lemon', 'with', 'single', 'leaf')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'lemon',(6,42),('C',(6,30),(9,39),(6,35)),('C',(22,20),(6,23),(15,20)),('C',(28,35),(32,20),(34,27)),('C',(16,42),(24,40),(21,42)),('C',(6,42),(12,42),(12,38)),closed=True)
        path(m,'leaf',(32,14),('C',(42,6),(32,6),(36,6)),('C',(32,14),(42,14),(38,14)),closed=True)
        line('stem',(32,14),(22,20));join('stem','leaf');join('stem','lemon')
