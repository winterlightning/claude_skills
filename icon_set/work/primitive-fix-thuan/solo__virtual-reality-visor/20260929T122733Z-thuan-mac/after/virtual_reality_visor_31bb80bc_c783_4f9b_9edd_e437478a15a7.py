'The rejected visor is too tall and has a deep narrow nose notch.\nSymbol plan: Flatten the wide upper visor and make a broad shallow mirrored nose notch.\nConstruction: Lucide glasses original and atomic-debug: mirrored eye-area balance; supplied reference owns the blank visor.\nOmissions: None.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '31bb80bc-c783-4f9b-9edd-e437478a15a7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__virtual-reality-visor/20260929T122733Z-thuan-mac/reference/vr headset 1_31bb80bc-c783-4f9b-9edd-e437478a15a7.svg'
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
    icon_id = 'virtual-reality-visor'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('virtual', 'reality', 'visor')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'visor',(24,10),('C',(4,24),(8,10),(4,12)),('C',(14,38),(4,32),(8,38)),('C',(24,30),(18,38),(20,30)),('C',(34,38),(28,30),(30,38)),('C',(44,24),(40,38),(44,32)),('C',(24,10),(44,12),(40,10)),closed=True)
