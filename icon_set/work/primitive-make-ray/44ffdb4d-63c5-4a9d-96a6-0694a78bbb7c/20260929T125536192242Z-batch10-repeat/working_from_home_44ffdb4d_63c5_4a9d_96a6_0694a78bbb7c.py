"""The rejected remote worker had a tiny bent torso disconnected visually from the laptop. Restore broad seated shoulders under the roof and a clear laptop screen and keyboard.
Symbol plan: human_ref/user.svg round head and seated shoulders; exact4 ink gap from head30 to shoulders38; original roof and laptop.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '44ffdb4d-63c5-4a9d-96a6-0694a78bbb7c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__working-from-home/20260929T124732Z-thuan-mac/reference/work from home user laptop 2_44ffdb4d-63c5-4a9d-96a6-0694a78bbb7c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'working-from-home'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('working', 'from', 'home')

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

        poly('roof',(6,16),(24,6),(42,16))
        circle('head',14,26,4)
        path('body',(6,42),[('A',(14,38),8,4,True),('A',(22,42),8,4,True)])
        poly('laptop',(24,42),(30,26),(42,26),(38,42),closed=True)
        line('keyboard',(14,42),(24,42));join('keyboard','body');join('keyboard','laptop')
