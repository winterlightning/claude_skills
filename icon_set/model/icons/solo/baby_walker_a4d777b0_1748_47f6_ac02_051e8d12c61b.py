"""A broad tray and hanging seat supported by two curved wheeled legs. Open lower construction keeps the wheels distinct.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4d777b0-1748-47f6-ac02-051e8d12c61b'
SOURCE_PATH = 'pictographic-primitives/babies/walker waling car_a4d777b0-1748-47f6-ac02-051e8d12c61b.svg'
AUTHOR = 'gpt-6'

class BabyWalker(Solo48):
    icon_id = 'baby-walker'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('baby', 'walker')

    def build(self):
        # Symbol plan: A broad tray and hanging seat supported by two curved wheeled legs. Open lower construction keeps the wheels distinct.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
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
        path('seat',(16,16),[('L',(16,24)),('A',(32,24),8,5,False),('L',(32,16))]);join('tray','seat')
        for j,(x,c) in enumerate(((8,12),(40,36))):
         poly(f'leg-{j}',(x,16),(x,30),(c,34));join('tray',f'leg-{j}')
         circle(f'wheel-{j}',c,37,3);join(f'leg-{j}',f'wheel-{j}')
