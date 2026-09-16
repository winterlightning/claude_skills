"""Two equal short dashes, consistent eight-unit clearances and a 45-degree arrowhead; solo family retained.
References: Lucide move-horizontal: equal diagonal arrowheads.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ebf9acc-12df-4295-afb7-797830fc7f91'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.svg'
AUTHOR = 'gpt-6'

class ArrowDotLeft(Solo48):
    icon_id = 'arrow-dot-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'left')

    def build(self):
        # Symbol plan: Two equal short dashes, consistent eight-unit clearances and a 45-degree arrowhead; solo family retained.

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
        orient='left'
        def pt(x,y):
            if orient=='down':return (x,y)
            if orient=='up':return (x,48-y)
            if orient=='left':return (48-y,x)
            return (y,x)
        poly('head',pt(8,28),pt(24,44),pt(40,28))
        line('shaft',pt(24,28),pt(24,44));join('head','shaft')
        for j,y in enumerate((4,16)):line(f'dash-{j}',pt(24,y),pt(24,y+4))
