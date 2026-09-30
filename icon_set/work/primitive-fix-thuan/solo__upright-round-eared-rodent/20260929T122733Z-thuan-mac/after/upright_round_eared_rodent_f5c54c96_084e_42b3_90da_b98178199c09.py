'The rejected gopher has pointed flared feet and no forepaws, unlike the rounded plump reference.\nSymbol plan: Round the lower body and feet and restore paired tucked forepaw marks below a small face.\nConstruction: Lucide mouse original and atomic-debug informs smooth rounded enclosure; reference owns ears, muzzle and paws.\nOmissions: Tiny toe and mouth details omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f5c54c96-084e-42b3-90da-b98178199c09'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-round-eared-rodent/20260929T122733Z-thuan-mac/reference/gopher_f5c54c96-084e-42b3-90da-b98178199c09.svg'
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
    icon_id = 'upright-round-eared-rodent'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'round', 'eared', 'rodent')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'body',(8,10),('A',(18,10),5,6,True),('C',(30,10),(21,8),(27,8)),('A',(40,10),5,6,True),('C',(40,32),(38,19),(40,24)),('C',(34,44),(40,38),(40,44)),('L',(28,44)),('C',(20,44),(26,41),(22,41)),('L',(14,44)),('C',(8,32),(8,44),(8,38)),('C',(8,10),(8,24),(10,19)),closed=True)
        m.add_dot('eye-left',(18,19));m.add_dot('eye-right',(30,19));line('muzzle',(24,27),(24,29))
        path(m,'paw-left',(17,33),('C',(18,35),(17,34),(17,35)))
        path(m,'paw-right',(31,33),('C',(30,35),(31,34),(31,35)))
