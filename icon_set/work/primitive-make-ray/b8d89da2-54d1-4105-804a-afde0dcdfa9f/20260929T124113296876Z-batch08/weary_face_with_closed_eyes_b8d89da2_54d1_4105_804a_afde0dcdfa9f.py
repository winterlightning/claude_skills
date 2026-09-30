'The rejected weary face uses straight eye dashes and a cramped tiny frown.\nSymbol plan: Curve both closed eyelids, soften the worried brows and widen the frown.\nConstruction: No useful exact Lucide expression match; supplied face reference owns the expression and symmetry.\nOmissions: None.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b8d89da2-54d1-4105-804a-afde0dcdfa9f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__weary-face-with-closed-eyes/20260929T122733Z-thuan-mac/reference/face weary_b8d89da2-54d1-4105-804a-afde0dcdfa9f.svg'
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
    icon_id = 'weary-face-with-closed-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('weary', 'face', 'with', 'closed', 'eyes')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'face',24,24,20)
        path(m,'brow-left',(17,15),('C',(20,14),(18,15),(19,15)))
        path(m,'brow-right',(31,15),('C',(28,14),(30,15),(29,15)))
        path(m,'eye-left',(14,23),('C',(19,23),(15,25),(18,25)))
        path(m,'eye-right',(29,23),('C',(34,23),(30,25),(33,25)))
        m.add_arc('frown',(18,34),(30,34),radius_x=6,radius_y=2,sweep=True)
