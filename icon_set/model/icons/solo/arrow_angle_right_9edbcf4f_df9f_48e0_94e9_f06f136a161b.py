"""A centered chevron with equal arms; kept as SOLO48 by user request.
References: Lucide chevron-right: a single coherent two-arm stroke.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9edbcf4f-df9f-48e0-94e9-f06f136a161b'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow angle right_9edbcf4f-df9f-48e0-94e9-f06f136a161b.svg'
AUTHOR = 'gpt-6'

class ArrowAngleRight(Solo48):
    icon_id = 'arrow-angle-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'angle', 'right')

    def build(self):
        # Symbol plan: A centered chevron with equal arms; kept as SOLO48 by user request.

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
        poly('chevron',(6,6),(42,24),(6,42))
