"""A rectangular conversation bubble formed by two alternating perimeter arrows. Restores long top edge, rounded corners, and lower-left speech tail. Bounds (6,6)-(42,42).
Construction reference: Lucide message-square and refresh-ccw: rounded bubble perimeter and shared arrow tips.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7e75641a-fc1e-57a5-be43-63afa022d2b8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__speech-bubble-cycle-arrows/20260924T100518Z-thuan-mac/reference/discussion converstion_7e75641a-fc1e-57a5-be43-63afa022d2b8.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='speech-bubble-cycle-arrows'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('discussion', 'converstion')
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
        path('upper',(38,12),[('L',(38,10)),('A',(34,6),4,4,False),('L',(16,6)),('A',(12,10),4,4,False),('L',(12,24))])
        poly('down-head',(6,18),(12,24),(18,18));join('upper','down-head')
        path('lower',(12,34),[('L',(12,42)),('L',(24,36)),('L',(32,36)),('A',(36,32),4,4,False),('L',(36,22))])
        poly('up-head',(30,28),(36,22),(42,28));join('lower','up-head')
