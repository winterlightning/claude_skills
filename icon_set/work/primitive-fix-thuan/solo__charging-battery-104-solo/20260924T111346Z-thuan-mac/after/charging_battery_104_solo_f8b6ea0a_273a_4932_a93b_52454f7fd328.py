"""Closed horizontal battery and centered lightning stroke with external terminal; extremes 4,10,44,38.
Construction: battery-charging: angular bolt and rounded corners
Reduction: Terminal is a single short stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__charging-battery-104-solo/20260924T111346Z-thuan-mac/reference/battery 1_f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'charging-battery-104-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('charging', 'battery', '104', 'solo')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('case',(8,8),[('L',(32,8)),('A',(36,12),4,4,True),('L',(36,36)),('A',(32,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
        poly('bolt',(24,17),(16,25),(25,25),(18,31));line('terminal',(44,20),(44,28))
