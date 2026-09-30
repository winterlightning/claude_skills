"""The rejected infinity symbol had tall narrow loops. Restore broad horizontal bowls and a smooth diagonal crossover, preserving exact mirrored loops.
Symbol plan: Original infinity; shared mirrored bowls with continuous crossover tangents.
Keyshape HRECT_M: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a3462919-e2c3-488f-97ad-cc3959be0886'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__virtual-coin-crypto-infinite/20260929T122443Z-thuan-mac/reference/virtual coin crypto infinite_a3462919-e2c3-488f-97ad-cc3959be0886.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'virtual-coin-crypto-infinite'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'infinite')

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

        path('infinity',(24,24),[('C',(13,10),(19,18),(18,10)),('C',(4,24),(7,10),(4,15)),('C',(13,38),(4,33),(7,38)),('C',(24,24),(18,38),(19,30)),('C',(35,10),(29,18),(30,10)),('C',(44,24),(41,10),(44,15)),('C',(35,38),(44,33),(41,38)),('C',(24,24),(30,38),(29,30))],True)
