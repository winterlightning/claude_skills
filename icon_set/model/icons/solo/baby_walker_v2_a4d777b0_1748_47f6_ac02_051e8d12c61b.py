"""A broad walker tray, hanging seat and rounded base with two wheels. Shared left/right frame posts support the tray.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4d777b0-1748-47f6-ac02-051e8d12c61b'
SOURCE_PATH = 'pictographic-primitives/babies/walker waling car_a4d777b0-1748-47f6-ac02-051e8d12c61b.svg'
AUTHOR = 'gpt-6'

class BabyWalkerVariant2(Solo48):
    icon_id = 'baby-walker-v2'
    variant_of = 'baby-walker'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('baby', 'walker')

    def build(self):
        # Symbol plan: A broad walker tray, hanging seat and rounded base with two wheels. Shared left/right frame posts support the tray.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        box('tray',4,8,44,16,3)
        path('seat',(16,16),[('L',(16,20)),('A',(32,20),8,8,False),('L',(32,16))]);join('tray','seat')
        for side,x in [('left',8),('right',40)]:
         line('post-'+side,(x,16),(x,32));join('tray','post-'+side)
        poly('base',(8,32),(40,32));join('base','post-left');join('base','post-right')
        for j,x in enumerate((12,36)):
         circle(f'wheel-{j}',x,37,3)
         line(f'wheel-link-{j}',(x,32),(x,34));join('base',f'wheel-link-{j}');join(f'wheel-{j}',f'wheel-link-{j}')
