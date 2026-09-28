"""Three-merlon rook with equally spaced battlements, rounded crown corners, tapered trunk and rounded pedestal. A broader envelope preserves every notch at legal spacing."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6827ce25-bda1-54bb-bc4b-11e435eb0b3f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__chess-rook-batch-013-15/20260924T083211Z-thuan-mac/reference/chess rook_6827ce25-bda1-54bb-bc4b-11e435eb0b3f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='chess-rook-batch-013-15'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Three-merlon rook with equally spaced battlements, rounded crown corners, tapered trunk and rounded pedestal. A broader envelope preserves every notch at legal spacing.

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

        path('crown',(4,8),[('L',(12,8)),('L',(12,16)),('L',(20,16)),('L',(20,8)),('L',(28,8)),('L',(28,16)),('L',(36,16)),('L',(36,8)),('L',(44,8)),('L',(44,20)),('A',(40,24),4,4,True),('L',(32,24)),('L',(16,24)),('L',(8,24)),('A',(4,20),4,4,True),('L',(4,8))],True)
        self.add_polyline('trunk',(16,24),(14,32),(34,32),(32,24));join('trunk','crown')
        path('base',(14,32),[('L',(8,32)),('A',(4,36),4,4,False),('L',(4,40)),('L',(44,40)),('L',(44,36)),('A',(40,32),4,4,False),('L',(34,32))]);join('trunk','base')
