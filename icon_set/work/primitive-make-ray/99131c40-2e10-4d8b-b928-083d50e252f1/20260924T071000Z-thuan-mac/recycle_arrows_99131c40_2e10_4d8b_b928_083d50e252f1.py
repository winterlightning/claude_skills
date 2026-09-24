"""Three bent arrows form a continuous clockwise recycling cycle.
Symbol plan: shared parameters and coherent contours.
Construction: recycle: three separate strokes and attached open arrowheads.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='99131c40-2e10-4d8b-b928-083d50e252f1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__recycle-arrows/20260924T065933Z-thuan-mac/reference/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='recycle-arrows'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('recycle', 'arrows')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Three distinct arrows with real endpoint joins; preserve triangular flow.
        self.path('top',(18,12),[('L',(20,8)),('A',(28,8),5,5,True),('L',(36,22))])
        self.add_polyline('top-head',(28,20),(36,22),(38,14));self.relate('connect','top','top-head')
        self.path('right',(42,28),[('L',(42,32)),('A',(38,36),4,4,True),('L',(24,36))])
        self.add_polyline('bottom-head',(30,30),(24,36),(30,42));self.relate('connect','right','bottom-head')
        self.path('left',(15,36),[('L',(10,36)),('A',(6,32),4,4,True),('L',(12,20))])
        self.add_polyline('left-head',(6,22),(12,20),(14,28));self.relate('connect','left','left-head')
