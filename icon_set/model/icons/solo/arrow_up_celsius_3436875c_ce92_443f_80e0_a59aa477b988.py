"""A readable rising arrow next to the Celsius C and degree dot; preserve upward meaning and restore the missing temperature notation.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3436875c-ce92-443f-80e0-a59aa477b988'
SOURCE_PATH = 'pictographic-primitives/state/arrow up celsius_3436875c-ce92-443f-80e0-a59aa477b988.svg'
AUTHOR = 'gpt-6'

class ArrowUpCelsius(Solo48):
    icon_id = 'arrow-up-celsius'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('arrow', 'up', 'celsius')

    def build(self):
        # Symbol plan: A readable rising arrow next to the Celsius C and degree dot; preserve upward meaning and restore the missing temperature notation.

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
        poly('arrow',(6,18),(14,6),(22,18));line('shaft',(14,6),(14,42));join('arrow','shaft')
        path('celsius',(42,26),[('A',(30,34),12,8,False),('A',(42,42),12,8,False)])
        dot('degree',(36,12))
