"""Ascending passenger plane above one separate horizontal runway. Smooth nose and swept wings retain the reference; tail stays a true part of the aircraft, not joined to the runway."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c2782429-745d-5835-abe8-ed5499875d12'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__plane-on-runway/20260924T083211Z-thuan-mac/reference/plane on runway_c2782429-745d-5835-abe8-ed5499875d12.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='plane-on-runway'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Ascending passenger plane above one separate horizontal runway. Smooth nose and swept wings retain the reference; tail stays a true part of the aircraft, not joined to the runway.

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

        path('plane',(6,28),[('L',(6,20)),('L',(12,23)),('L',(19,19)),('L',(11,11)),('L',(20,6)),('L',(28,14)),('L',(35,9)),('C',(42,12),(38,8),(42,8)),('C',(40,17),(42,14),(42,16)),('L',(16,32)),('C',(6,28),(12,35),(9,32))],True)
        line('runway',(6,42),(42,42))
