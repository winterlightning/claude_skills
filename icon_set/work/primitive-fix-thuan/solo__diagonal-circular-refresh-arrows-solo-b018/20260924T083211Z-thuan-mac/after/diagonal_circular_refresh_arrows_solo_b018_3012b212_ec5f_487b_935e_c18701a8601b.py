"""Two clockwise circular arrows in diagonal opposition with broad open gaps. Equal quarter-circle radii and a single shared arrow-tip node; Lucide undo-2 construction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3012b212-ec5f-487b-935e-c18701a8601b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-circular-refresh-arrows-solo-b018/20260924T083211Z-thuan-mac/reference/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-circular-refresh-arrows-solo-b018'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Two clockwise circular arrows in diagonal opposition with broad open gaps. Equal quarter-circle radii and a single shared arrow-tip node; Lucide undo-2 construction.

        def path(n,start,commands,closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                m=f'{n}-{i}'
                if kind=='L': self.add_line(m,start,end)
                elif kind=='A': self.add_arc(m,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,start,(args[0],args[1],end))
                members.append(m);start=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry=None):
            ry=rx if ry is None else ry
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        for s in (1,-1):
            p=lambda x,y:(x,y) if s==1 else (48-x,48-y)
            path(f'arc{s}',p(6,24),[('A',p(24,6),18,18,True),('C',p(36,10),p(28,6),p(33,7))])
            self.add_polyline(f'head{s}',p(26,10),p(36,10),p(36,18));join(f'arc{s}',f'head{s}')
