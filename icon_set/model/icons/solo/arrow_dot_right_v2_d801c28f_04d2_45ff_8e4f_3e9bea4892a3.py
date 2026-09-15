"""Two equal short dashes, consistent eight-unit clearances and a 45-degree arrowhead; solo family retained.
References: Lucide move-horizontal: equal diagonal arrowheads.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd801c28f-04d2-45ff-8e4f-3e9bea4892a3'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot right_d801c28f-04d2-45ff-8e4f-3e9bea4892a3.svg'
AUTHOR = 'gpt-6'

class ArrowDotRightVariant2(Solo48):
    icon_id = 'arrow-dot-right-v2'
    variant_of = 'arrow-dot-right'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'right')

    def build(self):
        # Symbol plan: Two equal short dashes, consistent eight-unit clearances and a 45-degree arrowhead; solo family retained.

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
        orient='right'
        def pt(x,y):
            if orient=='down':return (x,y)
            if orient=='up':return (x,48-y)
            if orient=='left':return (48-y,x)
            return (y,x)
        poly('head',pt(8,28),pt(24,44),pt(40,28))
        line('shaft',pt(24,28),pt(24,44));join('head','shaft')
        for j,y in enumerate((4,16)):line(f'dash-{j}',pt(24,y),pt(24,y+4))
