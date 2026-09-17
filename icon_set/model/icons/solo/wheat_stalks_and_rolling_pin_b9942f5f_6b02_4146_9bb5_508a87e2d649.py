"""Wheat Stalks and Rolling Pin.

Plan: Paired wheat stalks above horizontal rolling pin. Bounds (6,6)-(42,42).
Construction: Lucide wheat shared stem and repeated branches; source rolling pin.
Reduction: Two open grain forks replace fine branches; broad rolling barrel and simple handle strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'b9942f5f-6b02-4146-9bb5-508a87e2d649'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/shavuot feast of week_b9942f5f-6b02-4146-9bb5-508a87e2d649.svg'
AUTHOR = 'gpt-6'


class IconWheatStalksAndRollingPin(Solo48):
    icon_id = 'wheat-stalks-and-rolling-pin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('wheat', 'stalks', 'and', 'rolling', 'pin')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('barrel',(14,30),[('L',(34,30)),('L',(34,36)),('L',(34,42)),('L',(14,42)),('L',(14,36)),('L',(14,30))],True)
        self.add_line('handle-left',(6,36),(14,36));self.add_line('handle-right',(34,36),(42,36));self.relate('connect','handle-left','barrel');self.relate('connect','handle-right','barrel')
        for side in [-1,1]:
         def p(x,y):return (24+side*x,y)
         path('stem'+str(side),p(6,22),[('L',p(10,16)),('L',p(10,6))])
         self.add_line('grain-a'+str(side),p(10,16),p(18,12));self.add_line('grain-b'+str(side),p(10,16),p(4,10));self.relate('connect','grain-a'+str(side),'stem'+str(side));self.relate('connect','grain-b'+str(side),'stem'+str(side))
