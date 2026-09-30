"""The rejected coin used an upright closed D and a single tick. Restore the slanted D stem and two currency ticks, keeping the coin rim.
Symbol plan: Original Digibyte currency mark: open slanted stem, smooth D bowl and paired ticks.
Keyshape CIRCLE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__virtual-coin-crypto-digibyte/20260929T122443Z-thuan-mac/reference/virtual coin crypto digibyte_c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'virtual-coin-crypto-digibyte'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'digibyte')

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

        circle('coin',24,24,20)
        path('d',(16,16),[('L',(25,16)),('A',(25,32),8,8,True),('L',(16,32)),('L',(20,21))])
        for x in (20,28):
         line(f'top-{x}',(x,13),(x,16));join(f'top-{x}','d')
         line(f'bottom-{x}',(x,32),(x,35));join(f'bottom-{x}','d')
