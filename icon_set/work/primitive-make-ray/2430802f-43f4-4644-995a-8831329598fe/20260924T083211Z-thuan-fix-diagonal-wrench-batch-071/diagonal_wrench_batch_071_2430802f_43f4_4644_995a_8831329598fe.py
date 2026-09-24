"""Open-end wrench on a diagonal with circular jaw shoulders, a roomy mouth and a rounded handle end. Lucide circular construction informs smooth neck and head transitions."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2430802f-43f4-4644-995a-8831329598fe'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-wrench-batch-071/20260924T083211Z-thuan-mac/reference/tool_2430802f-43f4-4644-995a-8831329598fe.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-wrench-batch-071'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Open-end wrench on a diagonal with circular jaw shoulders, a roomy mouth and a rounded handle end. Lucide circular construction informs smooth neck and head transitions.

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

        path('wrench',(18,22),[('C',(32,6),(14,12),(23,6)),('L',(26,14)),('C',(34,22),(26,18),(30,22)),('L',(42,14)),('C',(28,30),(42,26),(36,32)),('L',(16,40)),('C',(12,42),(15,41),(14,42)),('A',(6,36),6,6,True),('C',(8,32),(6,34),(7,33)),('L',(18,22))],True)
