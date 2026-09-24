"""A skull with a smooth circular cranium, cheek transitions and a squared jaw. Bounds (8,4)-(40,44); bilateral symmetry about x24.
Construction reference: Lucide skull: circular crown, smooth cheek transitions, minimal paired eye sockets.
Omissions: No added nasal symbol absent from original."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bf02abda-c65a-4ff2-af41-3fdc5c490cc7'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__skull-bf02abda/20260924T100518Z-thuan-mac/reference/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='skull-bf02abda-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('skull',)
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('skull',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('C',(34,34),(40,26),(38,30)),('L',(34,40)),('A',(30,44),4,4,True),('L',(18,44)),('A',(14,40),4,4,True),('L',(14,34)),('C',(8,20),(10,30),(8,26))],True)
        for x in (17,31): self.add_dot('eye-'+str(x),(x,20))
        line('jaw-cleft',(24,36),(24,44));join('jaw-cleft','skull')
