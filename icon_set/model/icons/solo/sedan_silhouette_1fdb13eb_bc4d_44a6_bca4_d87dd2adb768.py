"""A broad sedan with low curved roof, rounded bumpers and two integrated wheel arcs. Envelope (4,10)-(44,38); shared wheel radius 4.
Construction reference: Lucide car: rounded body contour and wheel integration.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1fdb13eb-bc4d-44a6-bca4-d87dd2adb768'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sedan-silhouette'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "transportation"
    aliases=()
    keywords=('car',)
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
        path('silhouette',(8,30),[('L',(7,30)),('A',(4,27),3,3,True),('L',(4,24)),('A',(8,20),4,4,True),('L',(10,20)),('C',(18,10),(13,20),(14,10)),('L',(28,10)),('C',(36,18),(31,10),(33,16)),('L',(40,19)),('C',(44,23),(43,20),(44,20)),('L',(44,27)),('A',(40,31),4,4,True),('L',(40,34)),('A',(32,34),4,4,True),('L',(32,32)),('L',(16,32)),('L',(16,34)),('A',(8,34),4,4,True),('L',(8,30))],True)
