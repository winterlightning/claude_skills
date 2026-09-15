"""A sloping parallel-sided barrel on a circular wheel and two outward carriage supports.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '472cd9f4-5cc8-4752-9e89-ec6fa6da408b'
SOURCE_PATH = 'pictographic-primitives/war/symbol artillery_472cd9f4-5cc8-4752-9e89-ec6fa6da408b.svg'
AUTHOR = 'gpt-6'

class ArtilleryFieldGunVariant2(Solo48):
    icon_id = 'artillery-field-gun-v2'
    variant_of = 'artillery-field-gun'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('artillery', 'field', 'gun')

    def build(self):
        # Symbol plan: A sloping parallel-sided barrel on a circular wheel and two outward carriage supports.

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
        poly('barrel',(10,16),(34,8),(37,17),(13,25),closed=True)
        circle('wheel',13,33,7);join('wheel','barrel')
        line('rear-trail',(20,33),(44,40));join('wheel','rear-trail')
        line('left-foot',(6,33),(4,40));join('wheel','left-foot')
