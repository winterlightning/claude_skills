"""A matched upward chevron with equal arms; kept as SOLO48 by user request.
References: Lucide chevron-right: matched direction-independent arm construction.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95cae625-b690-4c5b-ade6-1ec2bc5b1e96'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow angle up_95cae625-b690-4c5b-ade6-1ec2bc5b1e96.svg'
AUTHOR = 'gpt-6'

class ArrowAngleUpVariant2(Solo48):
    icon_id = 'arrow-angle-up-v2'
    variant_of = 'arrow-angle-up'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'angle', 'up')

    def build(self):
        # Symbol plan: A matched upward chevron with equal arms; kept as SOLO48 by user request.

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
        poly('chevron',(6,42),(24,6),(42,42))
