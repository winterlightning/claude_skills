"""The rejected Iota mark used four short inward hooks around an empty center. Restore four longer sweeping open arcs with a consistent rotational flow.
Symbol plan: Original rotational mark; one shared sweeping curve rotated through four quarter turns.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '85afe198-8caf-4a8a-b751-b82fbc6bda8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__virtual-coin-crypto-iota/20260929T122443Z-thuan-mac/reference/virtual coin crypto iota_85afe198-8caf-4a8a-b751-b82fbc6bda8c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'virtual-coin-crypto-iota'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'iota')

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

        for j in range(4):
         def p(x,y):
          for _ in range(j):x,y=48-y,x
          return x,y
         self.add_bezier(f'arm-{j}',p(18,6),(p(31,6),p(42,10),p(42,20)),(p(42,27),p(39,31),p(33,33)))
