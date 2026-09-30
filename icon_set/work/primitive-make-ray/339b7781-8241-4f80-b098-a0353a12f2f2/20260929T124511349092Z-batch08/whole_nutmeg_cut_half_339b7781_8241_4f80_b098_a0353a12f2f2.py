'The rejected nutmeg groove is a short tick and the cut kernel is a solid dot.\nSymbol plan: Lengthen the whole-nut groove and restore an irregular kernel mark in the foreground half.\nConstruction: No useful exact local Lucide nutmeg match. Source owns the asymmetric overlap and groove.\nOmissions: Irregular kernel outline simplified to a compact wavy stroke.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '339b7781-8241-4f80-b098-a0353a12f2f2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whole-nutmeg-cut-half/20260929T122733Z-thuan-mac/reference/nutmeg_339b7781-8241-4f80-b098-a0353a12f2f2.svg'
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
    icon_id = 'whole-nutmeg-cut-half'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('whole', 'nutmeg', 'cut', 'half')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'whole',(20,31),('C',(6,22),(10,34),(6,30)),('C',(24,6),(6,10),(16,6)),('C',(31,20),(32,6),(34,12)))
        circle(m,'half',31,31,11);path(m,'kernel',(29,32),('C',(33,30),(31,32),(31,30)));join('whole','half')
        line('groove',(15,20),(18,16))
