"""One centered shaft and matched 45-degree heads; matched heads preserve clear direction.
References: Lucide move-horizontal: one shaft and matching heads.
Authored directly on SOLO48; original retained for comparison."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-left-right/20260926T073831Z-thuan-mac/reference/arrows left right_67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4.svg'
AUTHOR = "claude-opus-5-5"

class ArrowLeftRight(Solo48):
    icon_id = 'arrow-left-right'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('arrow', 'left', 'right')

    def build(self):
        # Symbol plan (revision per review): both arrowheads are shorter and narrower - 45-degree arms 8 each
        # way (were 16) - on the full-width centred shaft (4, 24)-(44, 24). The icon is now only 16
        # tall, so it uses the CIRCLE keyshape (shaft tips exactly on radius 20).

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
        poly('left',(12,16),(4,24),(12,32));poly('right',(36,16),(44,24),(36,32));line('shaft',(4,24),(44,24));join('shaft','left');join('shaft','right')
