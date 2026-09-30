'The rejected eyedropper has a short bulb, a stubby nozzle and an oversized drop.\nSymbol plan: Lengthen the tube below a high collar, round the bulb and reduce the detached falling drop.\nConstruction: Lucide pipette original and atomic-debug: collar attached to a longer tube. Supplied reference owns vertical orientation.\nOmissions: Inner reservoir omitted; detached droplet simplified to a small circular drop.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9b04880c-4624-50fd-b4f4-8585f3d465cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-eyedropper-releasing-one-drop/20260929T122733Z-thuan-mac/reference/picker_9b04880c-4624-50fd-b4f4-8585f3d465cb.svg'
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
    icon_id = 'upright-eyedropper-releasing-one-drop'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'eyedropper', 'releasing', 'one', 'drop')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'tube',(18,10),('A',(30,10),6,6,True),('L',(30,14)),('L',(30,24)),('C',(24,32),(30,28),(24,28)),('C',(18,24),(24,28),(18,28)),('L',(18,14)),('L',(18,10)),closed=True)
        line('collar-left',(10,14),(18,14));line('collar-right',(30,14),(38,14));join('tube','collar-left');join('tube','collar-right')
        circle(m,'drop',24,42,2)
