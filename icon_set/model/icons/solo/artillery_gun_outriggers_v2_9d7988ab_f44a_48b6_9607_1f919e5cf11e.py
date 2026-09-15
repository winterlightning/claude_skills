"""A cannon barrel and wheel meet at the wheel top, with open space around its spokes and two outward carriage legs.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d7988ab-f44a-48b6-9607-1f919e5cf11e'
SOURCE_PATH = 'pictographic-primitives/war/tank machine gun_9d7988ab-f44a-48b6-9607-1f919e5cf11e.svg'
AUTHOR = 'gpt-6'

class ArtilleryGunOutriggersVariant2(Solo48):
    icon_id = 'artillery-gun-outriggers-v2'
    variant_of = 'artillery-gun-outriggers'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('artillery', 'gun', 'outriggers')

    def build(self):
        # Symbol plan: A cannon barrel and wheel meet at the wheel top, with open space around its spokes and two outward carriage legs.

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
        poly('barrel',(18,18),(36,8),(40,16),(22,26),closed=True)
        circle('wheel',22,33,7);join('barrel','wheel')
        line('left-leg',(15,33),(4,40));line('right-leg',(29,33),(44,40));join('wheel','left-leg');join('wheel','right-leg')
