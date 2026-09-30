"""The rejected draped woman used a dot-like bun and generic circular head. Restore a rounded bun above the circular jaw and a clear diagonal garment fold across broad shoulders.
Symbol plan: human_ref/user.svg; circular jaw and rounded shoulders with true shared drape node. Jaw28, shoulder32 give touching ink.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cc95eb24-a835-44c4-8b2f-8722e687ddef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-in-draped-attire/20260929T124732Z-thuan-mac/reference/gokul ashtami_cc95eb24-a835-44c4-8b2f-8722e687ddef.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-in-draped-attire'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'in', 'draped', 'attire')
    human_construction = "bust"
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

        path('hair',(14,18),[('A',(20,10),6,8,True),('A',(28,10),4,4,True),('A',(34,18),6,8,True)])
        self.add_arc('jaw',(14,18),(34,18),radius_x=10,sweep=False);join('hair','jaw')
        path('body',(6,42),[('L',(9,42)),('A',(15,34),15,10,True),('A',(24,32),15,10,True),('A',(33,34),15,10,True),('A',(39,42),15,10,True),('L',(42,42))]);join('jaw','body')
        line('drape',(33,34),(20,42));join('drape','body')
