"""The rejected draped woman used a dotlike bun and generic body. Restore a rounded bun, curved shoulders and a clear diagonal fold across the garment.
Symbol plan: human_ref/user.svg circular jaw and curved shoulders; jaw22, shoulders26 give touching ink. Diagonal fold attaches at a true shoulder node.
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

        path('hair',(16,14),[('A',(20,10),4,4,True),('A',(28,10),4,4,True),('A',(32,14),4,4,True)])
        self.add_arc('jaw',(16,14),(32,14),radius_x=8,sweep=False);join('hair','jaw')
        path('body',(6,42),[('L',(9,41)),('A',(15,29),15,15,True),('A',(24,26),15,15,True),('A',(33,29),15,15,True),('A',(39,41),15,15,True),('L',(42,42))]);join('body','jaw')
        line('drape',(33,29),(20,42));join('drape','body')
