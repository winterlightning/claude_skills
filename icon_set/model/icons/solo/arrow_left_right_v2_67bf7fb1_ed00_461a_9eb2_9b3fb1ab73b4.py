"""One centered shaft and matched 45-degree heads; matched heads preserve clear direction.
References: Lucide move-horizontal: one shaft and matching heads.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right_67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4.svg'
AUTHOR = 'gpt-6'

class ArrowLeftRightVariant2(Solo48):
    icon_id = 'arrow-left-right-v2'
    variant_of = 'arrow-left-right'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'left', 'right')

    def build(self):
        # Symbol plan: One centered shaft and matched 45-degree heads; matched heads preserve clear direction.

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
        poly('left',(20,8),(4,24),(20,40));poly('right',(28,8),(44,24),(28,40));line('shaft',(4,24),(44,24));join('shaft','left');join('shaft','right')
