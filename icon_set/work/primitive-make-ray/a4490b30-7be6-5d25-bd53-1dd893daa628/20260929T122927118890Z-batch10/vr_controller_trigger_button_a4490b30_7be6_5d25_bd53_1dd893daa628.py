"""The rejected trigger controller replaced the oval tracking window with a bar and used an angular grip. Restore the open window and a smooth handle with a lower trigger mark.
Symbol plan: Original VR controller with shared oval tracking window and lower trigger stroke.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a4490b30-7be6-5d25-bd53-1dd893daa628'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vr-controller-trigger-button/20260929T122443Z-thuan-mac/reference/vr controller_a4490b30-7be6-5d25-bd53-1dd893daa628.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vr-controller-trigger-button'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vr', 'controller', 'trigger', 'button')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('body',(8,18),[('A',(24,4),16,14,True),('A',(40,18),16,14,True),('C',(32,28),(40,24),(37,26)),('L',(28,39)),('C',(18,44),(26,43),(23,44)),('C',(8,36),(12,44),(8,42)),('C',(12,25),(8,32),(11,28)),('C',(8,18),(10,23),(8,21))],True)
        path('window',(18,16),[('A',(30,16),6,4,True),('A',(18,16),6,4,True)],True)
        line('trigger',(18,35),(20,31))