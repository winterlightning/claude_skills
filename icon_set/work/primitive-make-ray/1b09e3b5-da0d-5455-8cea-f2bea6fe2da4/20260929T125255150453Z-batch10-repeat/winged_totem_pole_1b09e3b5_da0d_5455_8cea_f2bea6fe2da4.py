"""The rejected totem became a wide head with small slanted arms. Restore a tall narrow pole with a rounded crown and broad horizontal wings.
Symbol plan: Original totem; narrow crown and paired quarter-circle wings. Tiny face marks omitted.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1b09e3b5-da0d-5455-8cea-f2bea6fe2da4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winged-totem-pole/20260929T124732Z-thuan-mac/reference/totem pole_1b09e3b5-da0d-5455-8cea-f2bea6fe2da4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'winged-totem-pole'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('winged', 'totem', 'pole')

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

        path('pole',(18,12),[('A',(30,12),6,6,True),('L',(30,42)),('L',(18,42)),('L',(18,12))],True)
        path('wing-left',(18,18),[('L',(6,18)),('A',(14,26),8,8,False),('L',(18,26))]);join('wing-left','pole')
        path('wing-right',(30,18),[('L',(42,18)),('A',(34,26),8,8,True),('L',(30,26))]);join('wing-right','pole')
