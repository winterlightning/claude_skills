'The rejected wheelchair omits the armrest, footrest and rear-wheel hub, and its front caster looks detached.\nSymbol plan: Restore the armrest and projecting footrest with a smaller outlined caster below them and a visible rear-wheel hub.\nConstruction: Lucide accessibility original/atomic-debug: circular rear wheel and simple frame. Source owns the empty chair.\nOmissions: Extra parallel seat rail omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5e279196-338d-47df-9c7e-639098b008bb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheelchair-with-large-rear-wheel/20260929T122733Z-thuan-mac/reference/motorized wheelchair_5e279196-338d-47df-9c7e-639098b008bb.svg'
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
    icon_id = 'wheelchair-with-large-rear-wheel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wheelchair', 'with', 'large', 'rear', 'wheel')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'wheel',16,32,10);m.add_dot('hub',(16,32))
        poly('back',(8,6),(16,6),(16,14),(16,22));join('back','wheel')
        poly('seat',(16,22),(28,22),(32,22),(40,30),(42,30));join('seat','wheel');join('seat','back')
        poly('armrest',(16,14),(28,14),(28,22));join('armrest','back');join('armrest','seat')
        circle(m,'caster',40,40,2)
