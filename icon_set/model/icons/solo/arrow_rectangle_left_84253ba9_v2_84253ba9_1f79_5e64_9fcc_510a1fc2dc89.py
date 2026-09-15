"""A coherent tag-shaped arrow sign and centered inset chevron, retained as a solo subject by explicit request.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '84253ba9-1f79-5e64-9fcc-510a1fc2dc89'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow rectangle left_84253ba9-1f79-5e64-9fcc-510a1fc2dc89.svg'
AUTHOR = 'gpt-6'

class ArrowRectangleLeft84253ba9Variant2(Solo48):
    icon_id = 'arrow-rectangle-left-84253ba9-v2'
    variant_of = 'arrow-rectangle-left-84253ba9'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', '84253ba9')

    def build(self):
        # Symbol plan: A coherent tag-shaped arrow sign and centered inset chevron, retained as a solo subject by explicit request.

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
        path('sign',(18,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(18,40)),('L',(4,24)),('L',(18,8))],True)
        poly('chevron',(31,17),(24,24),(31,31))
