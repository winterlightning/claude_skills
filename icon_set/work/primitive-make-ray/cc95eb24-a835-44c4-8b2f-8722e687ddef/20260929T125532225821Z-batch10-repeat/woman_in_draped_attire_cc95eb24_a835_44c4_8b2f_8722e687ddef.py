"""The rejected draped portrait used a dot for a bun and lost the hairline. Restore the bun as a rounded upper lobe, circular jaw, swept hair and a diagonal garment fold.
Symbol plan: human_ref/user.svg circular jaw and shoulders; original bun and diagonal drape. Jaw28 and body32 make touching ink.
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
        path('body',(6,42),[('A',(20,32),14,10,True),('L',(28,32)),('A',(42,42),14,10,True)]);join('jaw','body')
        path('drape',(34,33),[('C',(17,42),(29,38),(23,40))]);join('body','drape')
